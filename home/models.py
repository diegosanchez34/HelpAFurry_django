from django.db import models


class Sexo(models.Model):
    id_sexo = models.AutoField(db_column='idSexo', primary_key=True) 
    sexo    = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.sexo)

class Esterilizado(models.Model):
    id_esterilizado = models.AutoField(db_column='idEsterilizado', primary_key=True) 
    esterilizado    = models.CharField(max_length=3, blank=False, null=False)

    def __str__(self):
        return str(self.esterilizado)

class Perro(models.Model):
    nro_chip         = models.AutoField(primary_key=True)
    nombre           = models.CharField(max_length=20)
    id_sexo          = models.ForeignKey('sexo',on_delete=models.CASCADE, db_column='idSexo')
    raza             = models.CharField(max_length=20)
    edad             = models.IntegerField()
    esterilizado     = models.ForeignKey('esterilizado',on_delete=models.CASCADE, db_column='idEsterilizado')
    imagen           = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return str(self.nombre)+" "+str(self.nro_chip)   
    

class Gato(models.Model):
    nro_chip         = models.AutoField(primary_key=True)
    nombre           = models.CharField(max_length=20)
    id_sexo          = models.ForeignKey('sexo',on_delete=models.CASCADE, db_column='idSexo')
    raza             = models.CharField(max_length=20)
    edad             = models.IntegerField()
    esterilizado     = models.ForeignKey('esterilizado',on_delete=models.CASCADE, db_column='idEsterilizado')
    imagen           = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return str(self.nombre)+" "+str(self.nro_chip)   