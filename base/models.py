from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    validFrom = models.DateTimeField()
    validTo = models.DateTimeField()
    percentDiscount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], default=0)
    fixedDiscount = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    isFixed = models.BooleanField(null=True)
    isActive = models.BooleanField(null=True)

    def __str__(self):
        return self.code


class Territory(models.Model):
    name = models.CharField(max_length=25, unique=True)
    zip = models.IntegerField(unique=True)
