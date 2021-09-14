from django.contrib import admin
from .models import HowWorks


class HowWorksAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(HowWorks, HowWorksAdmin)
