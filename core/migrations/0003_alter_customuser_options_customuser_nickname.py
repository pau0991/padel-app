# Generated by Django 4.1 on 2022-08-31 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_customuser_options_alter_match_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['first_name'], 'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
        migrations.AddField(
            model_name='customuser',
            name='nickname',
            field=models.CharField(blank=True, max_length=80, verbose_name='Apodo'),
        ),
    ]
