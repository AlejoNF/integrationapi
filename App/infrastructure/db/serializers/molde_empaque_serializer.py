from rest_framework import serializers
from App.infrastructure.db.models.molde_empaque import PrincipalMoldeEmpaque

class PrincipalMoldeEmpaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalMoldeEmpaque
        fields = '__all__'