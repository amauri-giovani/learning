# Generated by Django 3.1.4 on 2021-02-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210215_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='urldoc',
            field=models.URLField(default='', verbose_name='Documentação'),
        ),
    ]
