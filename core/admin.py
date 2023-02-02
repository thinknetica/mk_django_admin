from django.contrib import admin
from .models import Product
from django.template.loader import get_template

class ImageModelAdmin(admin.ModelAdmin):
    ...


class ProductInline(admin.StackedInline):
    model = Product


class ProductModelAdmin(admin.ModelAdmin):
    ...


class ShopModelAdmin(admin.ModelAdmin):
    inlines = ProductInline,
    fields = ('my_inline','title')
    readonly_fields = 'my_inline',
    response = None
    search_fields = 'title',

    def my_inline(self, obj=None):
        context = self.response.context_data
        inline = context['inline_admin_formset'] = context['inline_admin_formsets'].pop()
        return get_template(inline.opts.template).render(context, self.request)

    def changeform_view(self, request, *args, **kwargs):
        self.response = super().changeform_view(request, *args, **kwargs)
        return self.response
