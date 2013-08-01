from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    is_beneficiary = models.BooleanField(default=False)
    is_donor = models.BooleanField(default=False)

    class Meta:
        db_table = 'authentication_userprofile'

    def __str__(self):
        return "%s's profile" % self.user


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)

User.profile = property(lambda u: u.get_profile())
