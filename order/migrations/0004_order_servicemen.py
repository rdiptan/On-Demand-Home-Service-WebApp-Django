# Generated by Django 3.1.7 on 2021-04-19 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210419_0620'),
        ('order', '0003_auto_20210419_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='servicemen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.servicemen'),
        ),
    ]
