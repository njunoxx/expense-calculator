# Generated by Django 4.1.7 on 2023-03-17 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_project_expense', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]
