# Generated by Django 4.1.7 on 2023-03-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('approvalapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='approvalrequest',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]