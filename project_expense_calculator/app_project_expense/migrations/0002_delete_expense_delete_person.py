# Generated by Django 4.1.7 on 2023-03-16 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_project_expense', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
