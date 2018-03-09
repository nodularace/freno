from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Member(models.Model):
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(null=True, blank=True, unique=True)
    is_admin = models.BooleanField(default=False)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

