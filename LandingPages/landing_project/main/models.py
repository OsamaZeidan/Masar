from django.db import models


class InterestedCustomer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    university = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
