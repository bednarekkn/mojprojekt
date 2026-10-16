from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Treść nowego zadania")
    completed = models.BooleanField(default=False, verbose_name="Ukończone")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data utworzenia")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M')
        }

    def __str__(self):
        return self.title