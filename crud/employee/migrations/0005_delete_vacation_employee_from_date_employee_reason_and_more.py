# Generated by Django 5.0 on 2024-01-30 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_rename_vacationrequest_vacation_alter_vacation_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vacation',
        ),
        migrations.AddField(
            model_name='employee',
            name='from_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='reason',
            field=models.TextField(default='Tired', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(default='submitted', max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='to_date',
            field=models.DateField(null=True),
        ),
    ]
