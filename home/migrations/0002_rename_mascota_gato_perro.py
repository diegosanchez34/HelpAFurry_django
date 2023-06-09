# Generated by Django 4.2.1 on 2023-06-06 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mascota',
            new_name='Gato',
        ),
        migrations.CreateModel(
            name='Perro',
            fields=[
                ('nro_chip', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('esterilizado', models.ForeignKey(db_column='idEsterilizado', on_delete=django.db.models.deletion.CASCADE, to='home.esterilizado')),
                ('id_sexo', models.ForeignKey(db_column='idSexo', on_delete=django.db.models.deletion.CASCADE, to='home.sexo')),
            ],
        ),
    ]
