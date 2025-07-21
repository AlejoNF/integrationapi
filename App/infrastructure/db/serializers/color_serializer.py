from rest_framework import serializers
from App.infrastructure.db.models.color import PrincipalColorEmpaque

class PrincipalColorEmpaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalColorEmpaque
        fields = ['id', 'nombre']