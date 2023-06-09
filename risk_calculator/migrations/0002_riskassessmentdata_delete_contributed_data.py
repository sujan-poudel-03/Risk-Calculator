# Generated by Django 4.0.3 on 2023-04-26 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk_calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskAssessmentData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('experience', models.CharField(max_length=255)),
                ('architectural_complexity', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('software_performance', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('software_scalability', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('compatibility', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('budget_constraint', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('schedule_constraint', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('scope_constraint', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('resource_constraint', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('market_change', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('competition', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('regulatory_requirements', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('skill_gaps', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('turnover', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
                ('team_communication_issues', models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3)),
            ],
            options={
                'verbose_name_plural': 'Risk Assessments',
            },
        ),
        migrations.DeleteModel(
            name='Contributed_Data',
        ),
    ]
