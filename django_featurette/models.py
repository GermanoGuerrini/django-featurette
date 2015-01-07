from django.db import models
from django.contrib.auth.models import Group

class Feature(models.Model):
    """The feature model.

    A feature is identified by a unique string and is associated to a group
    of users.
    """
    key = models.CharField(u"Key", unique=True, max_length=128,
        help_text=u"A unique key for this feature.")
    group = models.ForeignKey(Group)
    start_date = models.DateTimeField(u"Start date")
    end_date = models.DateTimeField(u"End date")
    is_active = models.BooleanField(u"Activation", default=False)

    def __unicode__(self):
        return self.key