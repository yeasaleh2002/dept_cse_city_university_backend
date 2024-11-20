from django.db import models
from django.core.mail import send_mail

class ContactUs(models.Model):
    # Basic contact fields
    name = models.CharField(max_length=255)  # User's name
    email = models.EmailField()  # User's email
    subject = models.CharField(max_length=255)  # Subject of the message
    message = models.TextField()  # User's message
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the message is created
    is_resolved = models.BooleanField(default=False)  # Track whether the message has been resolved

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    
    def save(self, *args, **kwargs):
        # Check if `is_resolved` is being set to True
        if self.pk:  # Ensure the instance already exists (not a new object)
            original = ContactUs.objects.get(pk=self.pk)
            if not original.is_resolved and self.is_resolved:  # Changed from False to True
                # Send email notification
                send_mail(
                    subject=f"Contact Us Message Resolved: {self.subject}",
                    message=f"Hello {self.name},\n\nYour message with subject '{self.subject}' has been resolved. "
                            f"Thank you for reaching out to us!\n\nBest regards,\nSupport Team",
                    from_email='your_email@example.com',
                    recipient_list=[self.email],
                    fail_silently=False,
                )
        super().save(*args, **kwargs)  # Call the parent save method