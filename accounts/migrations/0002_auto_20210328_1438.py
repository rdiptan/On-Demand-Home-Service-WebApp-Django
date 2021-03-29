# Generated by Django 3.1.7 on 2021-03-28 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customeruser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='servicemen',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='servicmenuser', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
