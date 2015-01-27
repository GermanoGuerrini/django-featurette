from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Group
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Feature(models.Model):
    """The feature model.

    A feature is identified by a unique string and is associated to a group
    of users.
    """
    key = models.CharField("Key", unique=True, max_length=128,
        help_text="A unique key for this feature.")
    group = models.ForeignKey(Group)
    start_date = models.DateTimeField("Start date")
    end_date = models.DateTimeField("End date")
    is_active = models.BooleanField("Activation", default=False)

    def __str__(self):
        return self.key
