from django.db import models
from .empaque import PrincipalEmpaques  # o PrincipalEmpaques si así se llama tu modelo de empaque
from .molde import PrincipalMolde
from .color import PrincipalColorEmpaque

class PrincipalMoldeEmpaque(models.Model):
    fechaCreacion = models.DateField(null=True, blank=True)
    fechaModificacion = models.DateField(null=True, blank=True)
    horaCreacion = models.TimeField(null=True, blank=True)
    horaModificacion = models.TimeField(null=True, blank=True)
    borrado = models.BooleanField(default=False)
    color = models.ForeignKey(PrincipalColorEmpaque, on_delete=models.SET_NULL, null=True, db_column='idColor_id')
    empaque = models.ForeignKey(PrincipalEmpaques, on_delete=models.CASCADE, null=True, db_column='idEmpaque_id')
    molde = models.ForeignKey(PrincipalMolde, on_delete=models.SET_NULL, null=True, db_column='idMolde_id')
    usuarioCreacion_id = models.IntegerField(null=True, blank=True)
    usuarioModificacion_id = models.IntegerField(null=True, blank=True)
    estado = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        managed = False  # Si no quieres que Django maneje la migración de esta tabla
        db_table = 'Principal_moldeempaque'