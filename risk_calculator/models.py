from django.db import models

# Create your models here.
YES_NO_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No')
)

class RiskAssessmentData(models.Model):
    project_name = models.CharField(max_length=255)
    email = models.EmailField()
    experience = models.CharField(max_length=255)
    architectural_complexity = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    software_performance = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    software_scalability = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    compatibility = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    budget_constraint = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    schedule_constraint = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    scope_constraint = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    resource_constraint = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    market_change = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    competition = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    regulatory_requirements = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    skill_gaps = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    turnover = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    team_communication_issues = models.CharField(max_length=3, choices=YES_NO_CHOICES)
    
    def __str__(self):
        return self.project_name + ' - ' + self.email


