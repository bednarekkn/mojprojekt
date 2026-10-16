from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ProfilUzytkownika(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    points = models.IntegerField(default=0)
    is_active_student = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.user.username} ({self.points} pkt)"
    
# Pytania baza
class Pytania(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=300, verbose_name="Treść pytania: ")
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0, verbose_name="Ocena pytania: ")
    
    def __str__(self):
        return self.text

# Odpowiedzi do pytań
class Odpowiedzi(models.Model):
    question = models.ForeignKey(Pytania, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField(verbose_name="Treść odpowiedzi")
    votes = models.IntegerField(default=0,  verbose_name="Liczba głosów: ")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 
