  
from django.db import models

TF = (
  ('Positive', 'Positive'),
  ('Negative', 'Negative')
)

class Items(models.Model):
  category    = models.CharField(max_length=30)
  prompts     = models.CharField(max_length=400, blank=True)
  keywords    = models.CharField(max_length=100, blank=True)
  cons        = models.CharField(max_length=100, blank=True)
  status      = models.CharField(max_length=15, choices=TF, default="Negative")
		

