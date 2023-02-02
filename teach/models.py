from django.db import models

# Create your models here.
class SiteStatistic(Model):
    title = CharField(max_length=255)


from project.profiles.models import ReferralCode, SpecialGroup, Child

class ProxyReferralCode(ReferralCode):

    class Meta:
        proxy = True


class ProxySpecialGroup(SpecialGroup):

    class Meta:
        proxy = True


class ProxyChild(Child):

    class Meta:
        proxy = True

