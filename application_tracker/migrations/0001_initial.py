# Generated by Django 2.0.4 on 2018-04-18 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ApplicationStateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_form_completed', models.BooleanField(default=False)),
                ('dbs_received', models.BooleanField(default=False)),
                ('training1', models.BooleanField(default=False)),
                ('training2', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referee', models.CharField(max_length=200)),
                ('received', models.BooleanField(default=False)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_name', to='application_tracker.ApplicationStateModel')),
            ],
        ),
        migrations.AddField(
            model_name='applicationform',
            name='applicationState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application_tracker.ApplicationStateModel'),
        ),
    ]
