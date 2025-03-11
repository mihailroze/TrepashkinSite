from django.db import models

class Biography(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    bio_text = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True)

    def __str__(self):
        return self.full_name