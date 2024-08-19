# Generated by Django 5.1 on 2024-08-19 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_account_is_verified_freelancer_is_verified'),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account'),
        ),
    ]
