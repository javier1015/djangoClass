# Generated by Django 2.2.12 on 2020-05-12 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datauser',
            options={'verbose_name': 'Datos de usuario', 'verbose_name_plural': 'Informacion'},
        ),
        migrations.AlterModelOptions(
            name='detarol',
            options={'verbose_name': 'Roles de usuario', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='habilidades',
            options={'verbose_name': 'Habilidades de usuario', 'verbose_name_plural': 'Competencias'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name': 'Nivel de habilida', 'verbose_name_plural': 'Niveles de usuario'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'Perfil de usuario', 'verbose_name_plural': 'Perfiles'},
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='descripcionHabil',
            field=models.TextField(verbose_name='Descripcion habilidad'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='idHabili',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.Habilidades', verbose_name='identificador de habilidades'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='idUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdata.DataUser', verbose_name='identificador de usuario'),
        ),
    ]
