# Generated by Django 5.2 on 2025-04-09 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='updrs',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='diagnostico',
            field=models.CharField(max_length=700),
        ),
    ]
