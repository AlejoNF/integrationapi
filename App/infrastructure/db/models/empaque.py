from django.db import models

class PrincipalEmpaques(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=500, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    dimensiones = models.CharField(max_length=100, null=True, blank=True)
    capacidad = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=100)
    fechaCreacion = models.DateField(null=True, blank=True)
    fechaModificacion = models.DateField(null=True, blank=True)
    horaCreacion = models.TimeField(null=True, blank=True)
    horaModificacion = models.TimeField(null=True, blank=True)
    borrado = models.BooleanField(default=False)
    idMaterial_id = models.IntegerField(null=True, blank=True)
    idTipo_id = models.IntegerField(null=True, blank=True)
    idUnidadCobro_id = models.IntegerField(null=True, blank=True)
    idUso_id = models.IntegerField(null=True, blank=True)
    usuarioCreacion_id = models.IntegerField(null=True, blank=True)
    usuarioModificacion_id = models.IntegerField(null=True, blank=True)
    esCencosud = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False  # Si no quieres que Django maneje la migración de esta tabla
        db_table = 'Principal_empaque'