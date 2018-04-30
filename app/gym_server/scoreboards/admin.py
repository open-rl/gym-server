from django.contrib import admin
from scoreboards.models import EvaluationRun


# Register your models here.
class EvaluationRunAdmin(admin.ModelAdmin):
    list_display = ('user', 'env', 's3_path', 'high_score')
    fields = ('user', 'env', 's3_path', 'high_score')


admin.site.register(EvaluationRun, EvaluationRunAdmin)
