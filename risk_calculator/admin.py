from django.contrib import admin
from .models import RiskAssessmentData, RiskCalculatorHistory

# Register your models here.

admin.site.register(RiskAssessmentData)
admin.site.register(RiskCalculatorHistory)
