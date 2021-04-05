# Generated by Django 3.1.7 on 2021-04-14 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-date_ordered']},
        ),
        migrations.AddField(
            model_name='order',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Reviewed', 'Reviewed'), ('Expert Assigned', 'Expert Assigned'), ('Working', 'Working'), ('Finished', 'Finished')], default='Pending', max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='ServiceDeliveryAddress',
        ),
    ]