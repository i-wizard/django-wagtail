from django.db import models

class Subscribers(models.Model):
    email = models.EmailField(blank=False, null=True)
    full_name = models.CharField(blank=False, null=True, help_text="full name", max_length=100)

    def __str__(self):
        return self.full_name


    class Meta:
        verbose_name_plural = "Subscribers"