# Generated by Django 3.2.14 on 2022-08-21 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sundays', '0005_assignment_ass_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='password', max_length=50),
        ),
    ]
