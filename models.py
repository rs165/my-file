from django.db import models
from django.urls import reverse

class Book(models.Model):
    STATUS_CHOICES = [
        ('to_read', 'To Read'),
        ('reading', 'Reading'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=20, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='to_read')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} — {self.author or 'Unknown'}"

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
