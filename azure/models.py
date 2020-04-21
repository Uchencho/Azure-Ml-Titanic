from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name = None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class Predict(models.Model):
    #survived #pclass #sex #age #sibsp #parch

    SEX_CHOICES = [
    ('male', 'male'),
    ('female', 'female')
        ]

    SIBLINGS_CHOICES = [
    (0, 0),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
        ]

    TICKET_CHOICES = [
    (1, 1),
    (2, 2),
    (3, 3)
        ]

    name = models.CharField(max_length=50)
    ticket_class = models.IntegerField(choices=TICKET_CHOICES, default=0)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, default='female')
    age = IntegerRangeField(min_value=1, max_value=100)
    siblings = models.IntegerField(choices=SIBLINGS_CHOICES, default=0)
    parents = models.IntegerField(choices=SIBLINGS_CHOICES, default=0)

    def __str__(self):
        return self.name
