# Generated by Django 4.2.3 on 2023-07-16 08:32

import Jobapp.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jobapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='job_type',
        ),
        migrations.RemoveField(
            model_name='job',
            name='salary',
        ),
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.TextField(default='No description provided'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='Jobapp.job'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(default=Jobapp.models.UserProfile.default_resume, upload_to='resumes/'),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='Jobapp.company'),
        ),
    ]
