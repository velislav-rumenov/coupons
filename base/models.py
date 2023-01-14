from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    validFrom = models.DateTimeField()
    validTo = models.DateTimeField()
    percentDiscount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)], null=True, blank=True)
    fixedDiscount = models.IntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    isFixed = models.BooleanField(null=True)
    isActive = models.BooleanField(null=True)

    def __str__(self):
        return self.code

