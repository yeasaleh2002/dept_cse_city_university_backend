from rest_framework.response import Response
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from user.serializers import UserLoginSerializer
from teacher.models import Teacher
# from student.models import Student  # Assuming you have a Student model
from rest_framework.permissions import IsAuthenticated

class LoginAPIView(APIView):
    def post(self, request):
        # Use the UserLoginSerializer to validate the request data
        serializer = UserLoginSerializer(data=request.data)
        
        if serializer.is_valid():
            # Retrieve the validated data from the serializer
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')

            # Authenticate the user with the validated username and password
            user = authenticate(username=email, password=password)

            if user is not None:
                if user.is_active:
                    # Generate or get the auth token for the user
                    token, _ = Token.objects.get_or_create(user=user)

                    # Log the user in (sets session and authentication)
                    login(request, user)

                    # Fetch the Teacher or Student object associated with the User
                    user_name = None
                    user_role = None
                    
                    # Check if the user is a Teacher or a Student or an Admin
                    try:
                        teacher = Teacher.objects.get(user=user)
                        user_name = teacher.name
                        user_role = 'teacher'  # Set role to 'teacher' if it's a Teacher
                    except Teacher.DoesNotExist:
                            if user.is_superuser:
                                user_role = 'admin'  # Set role to 'admin' if it's an admin
                            else:
                                user_role = 'user'  # Set role to 'user' if it's neither Teacher nor Student
                        # try:
                        #     student = Student.objects.get(user=user)
                        #     user_name = student.name
                        #     user_role = 'student'  # Set role to 'student' if it's a Student
                        # except Student.DoesNotExist:
                            

                    # Prepare the response data, including the role
                    user_data = {
                        'token': token.key,
                        'user_id': user.id,
                        'name': user_name,  # Include the name (from Teacher or Student)
                        'role': user_role,   # Include the role (teacher, student, admin, etc.)
                    }

                    # Return the user data and the authentication token
                    return Response(user_data, status=status.HTTP_200_OK)

                return Response({"error": "User account is disabled."}, status=status.HTTP_403_FORBIDDEN)

            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

        # If serializer validation fails, return the validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIview(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')
