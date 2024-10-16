# Generated by Django 5.1 on 2024-08-21 06:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appln', '0003_alter_contact_options_alter_signup_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={},
        ),
        migrations.AddField(
            model_name='contact',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='contact',
            table=None,
        ),
    ]
