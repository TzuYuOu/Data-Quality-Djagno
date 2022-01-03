# Generated by Django 3.2.8 on 2021-11-04 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=5, verbose_name='Security ID')),
                ('question1', models.CharField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown')], default=1, max_length=1)),
                ('question2', models.CharField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown')], default=1, max_length=1)),
                ('question3', models.CharField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown')], default=1, max_length=1)),
            ],
        ),
    ]
