# Generated by Django 5.1.4 on 2024-12-05 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0005_job_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default=1, upload_to='jobs/'),
            preserve_default=False,
        ),
    ]
