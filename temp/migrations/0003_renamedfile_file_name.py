# Generated by Django 4.2.7 on 2023-11-15 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('temp', '0002_alter_renamedfile_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='renamedfile',
            name='file_name',
            field=models.CharField(default='RenamedFile', max_length=255),
            preserve_default=False,
        ),
    ]