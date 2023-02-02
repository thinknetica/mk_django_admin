from django.db import models

# answer on gist, ask from vladimir poddubniy
# https://gist.github.com/dpodd/3be287cdc882f25bbb813689ed1e9a0e

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

