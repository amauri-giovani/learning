# Generated by Django 3.1.4 on 2021-02-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210215_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='documento',
            field=models.FileField(default='', upload_to='', verbose_name='Documentação'),
        ),
    ]
