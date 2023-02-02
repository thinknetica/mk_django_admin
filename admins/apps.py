from django.apps import apps
from django.urls import path
from django.contrib.admin import apps as adminApps, sites

class AdminConfig(adminApps.AdminConfig):
    default_site = 'admins.admin.DefaultAdminSite'

    def ready(self, *args, **kwargs):
        super().ready(*args, **kwargs)
        sites.site.name = 'master-class'

        site = sites.site  # chaged with multiply admin sites
        # site.name = 'not_admin'
        site._registry = {}  # remove old registrations

        for config in apps.get_app_configs():
            admins = getattr(config.module, 'admin', None)

            for model in config.get_models():  # excluded auto_created and swapped
                model_admin = getattr(admins, f'{model.__name__}ModelAdmin', None)

                if model_admin and not site.is_registered(model):
                    site.register(model, model_admin)
