# Generated by Django 2.1.4 on 2019-06-05 13:12

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190605_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievance',
            name='grievance_id',
            field=models.CharField(default=blog.models.grievance_number, editable=False, max_length=20),
        ),
    ]
