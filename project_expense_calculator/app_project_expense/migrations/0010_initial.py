# Generated by Django 4.1.7 on 2023-03-17 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_project_expense', '0009_delete_expense_delete_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('contact', models.CharField(max_length=120)),
            ],
            options={
                'db_table': 'app_person',
            },
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_income', models.FloatField(default=0)),
                ('net_expense', models.FloatField(default=0)),
                ('total_balance', models.FloatField(default=0)),
                ('year', models.IntegerField()),
                ('month', models.CharField(max_length=50, unique=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_project_expense.person')),
            ],
            options={
                'db_table': 'app_expense',
            },
        ),
    ]
