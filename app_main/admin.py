from django.contrib import admin
from app_main.models import *

# Register your models here.

admin.site.site_header = "Ayon-Resume-Application"

class InfoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email',)

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True

admin.site.register(InfoModel, InfoModelAdmin)
admin.site.register(SkillsQualificationsModel)
admin.site.register(TechStackModel)
admin.site.register(EducationsModel)

class WorksModelAdmin(admin.ModelAdmin):
    list_display = ('designation', 'company', 'job_start_date',)

admin.site.register(WorksModel, WorksModelAdmin)
admin.site.register(ProjectsModel)
admin.site.register(PublicationModel)
