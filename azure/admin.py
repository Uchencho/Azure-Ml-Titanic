from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Predict

@admin.register(Predict)
class PredictAdmin(ImportExportModelAdmin):
    list_display = ["name","ticket_class", "sex", "age", "siblings", "parents", "probabiliy", "prediction"]