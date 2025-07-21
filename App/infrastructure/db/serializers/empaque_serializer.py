from rest_framework import serializers
from App.infrastructure.db.models.empaque import PrincipalEmpaques
from App.infrastructure.db.models.molde_empaque import PrincipalMoldeEmpaque
from App.infrastructure.db.models.molde import PrincipalMolde
from App.infrastructure.db.models.color import PrincipalColorEmpaque

# Serializer para Molde con id y nombre
class PrincipalMoldeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalMolde
        fields = ['id', 'nombre']

# Serializer para Color con id y nombre
class PrincipalColorEmpaqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrincipalColorEmpaque
        fields = ['id', 'nombre']

# Serializer para la relación MoldeEmpaque (molde, color, id)
class PrincipalMoldeEmpaqueSerializer(serializers.ModelSerializer):
    molde = PrincipalMoldeSerializer(read_only=True)
    color = PrincipalColorEmpaqueSerializer(read_only=True)

    class Meta:
        model = PrincipalMoldeEmpaque
        fields = ['id', 'molde', 'color']

class PrincipalEmpaquesSerializer(serializers.ModelSerializer):
    # Para escritura (POST), puedes mantener moldes como write_only si lo necesitas
    moldes = serializers.ListField(write_only=True, required=False)
    # Para lectura, usaremos un método para traer los moldes asociados
    moldes_response = serializers.SerializerMethodField(read_only=True)

    def get_moldes_response(self, obj):
        # Trae todos los registros de MoldeEmpaque asociados a este empaque
        moldes = PrincipalMoldeEmpaque.objects.filter(empaque=obj)
        return PrincipalMoldeEmpaqueSerializer(moldes, many=True).data

    def create(self, validated_data):
        # Extrae los datos de moldes si vienen en el POST
        moldes_data = validated_data.pop('moldes', [])
        empaque = super().create(validated_data)
        # Crea las relaciones molde_empaque
        for molde_data in moldes_data:
            PrincipalMoldeEmpaque.objects.create(
                empaque=empaque,
                molde_id=molde_data['molde']['id'],
                color_id=molde_data['color']['id']
            )
        return empaque

    class Meta:
        model = PrincipalEmpaques
        fields = '__all__'
        read_only_fields = ['moldes_response']