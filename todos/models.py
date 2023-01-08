from django.db import models

class Todo(models.Model):
    priorities = (
        ("A", "URGENTE"),
        ("B", "MODERADO"),
        ("C", "LEVE"),
    )

    nome = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    priority = models.CharField(max_length=1, choices=priorities)
    completo = models.BooleanField(default=False)
