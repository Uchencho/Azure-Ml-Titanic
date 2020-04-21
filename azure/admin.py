from django.contrib import admin

# Register your models here.
from .models import Predict

class PredictAdmin(admin.ModelAdmin):
    list_display = ["name","ticket_class", "sex", "age", "siblings", "parents", "probabiliy", "prediction"]

admin.site.register(Predict, PredictAdmin)