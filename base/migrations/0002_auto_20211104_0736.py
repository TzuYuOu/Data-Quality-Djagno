# Generated by Django 3.2.8 on 2021-11-04 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='security',
            name='question1',
            field=models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='security',
            name='question2',
            field=models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='security',
            name='question3',
            field=models.IntegerField(choices=[(1, 'YES'), (-1, 'NO'), (0, 'Unknown')], default=1, max_length=1),
        ),
    ]
