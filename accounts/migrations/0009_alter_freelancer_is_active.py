# Generated by Django 5.1 on 2024-08-20 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_freelancer_status_freelancer_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]