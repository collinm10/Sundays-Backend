# Generated by Django 3.2.14 on 2022-07-26 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sundays', '0003_assignment_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sundays.user'),
            preserve_default=False,
        ),
    ]