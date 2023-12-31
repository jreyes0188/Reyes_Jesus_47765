# Generated by Django 4.2.5 on 2023-10-06 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPython', '0003_alter_cardiologia_dni_alter_dermatologia_dni_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cardiologia',
            name='especialidad',
            field=models.CharField(default='Cardiologia', max_length=20),
        ),
        migrations.AddField(
            model_name='dermatologia',
            name='especialidad',
            field=models.CharField(default='Dermatologo', max_length=20),
        ),
        migrations.AddField(
            model_name='laboratorio',
            name='especialidad',
            field=models.CharField(default='Laboratorio', max_length=20),
        ),
        migrations.AddField(
            model_name='odontologia',
            name='especialidad',
            field=models.CharField(default='Odontologia', max_length=20),
        ),
        migrations.AddField(
            model_name='oftalmologia',
            name='especialidad',
            field=models.CharField(default='Oftalmologo', max_length=20),
        ),
        migrations.AlterField(
            model_name='cardiologia',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dermatologia',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='odontologia',
            name='dni',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='oftalmologia',
            name='dni',
            field=models.IntegerField(),
        ),
    ]
