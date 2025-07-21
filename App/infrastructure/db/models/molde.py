from django.db import models

class PrincipalMolde(models.Model):
    nombre = models.CharField(max_length=100)
    fechaCreacion = models.DateField(null=True, blank=True)
    fechaModificacion = models.DateField(null=True, blank=True)
    horaCreacion = models.TimeField(null=True, blank=True)
    horaModificacion = models.TimeField(null=True, blank=True)
    borrado = models.BooleanField(default=False)
    usuarioCreacion_id = models.IntegerField(null=True, blank=True)
    usuarioModificacion_id = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False  # Si no quieres que Django maneje la migración de esta tabla
        db_table = 'Principal_molde'