from rest_framework import serializers
from App.infrastructure.db.models.molde import PrincipalMolde

class PrincipalMoldeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalMolde
        fields = ['id', 'nombre']
