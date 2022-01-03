# Generated by Django 3.2.8 on 2021-11-16 05:01

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
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Data Name')),
                ('rawdata', models.FileField(upload_to='rawdata/')),
                ('attribute_data', models.FileField(upload_to='attribute/')),
                ('datatype', models.CharField(choices=[('normal', 'Normal'), ('freq', 'High Frequency'), ('time', 'Time Series')], default='normal', max_length=10)),
                ('questiontype', models.CharField(choices=[('classification', 'Classification'), ('regression', 'Regression')], default='classification', max_length=15)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityIndicator',
            fields=[
                ('data_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainapp.data')),
                ('question1', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question2', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question3', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question4', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question5', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question6', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question7', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question8', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question9', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question10', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question11', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question12', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question13', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question14', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question15', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question16', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question17', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question18', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question19', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question20', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question21', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question22', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
                ('question23', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='TimelinessIndicator',
            fields=[
                ('data_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mainapp.data')),
                ('question1', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
                ('question2', models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown'), (2, 'Non Applicable')])),
            ],
        ),
    ]
