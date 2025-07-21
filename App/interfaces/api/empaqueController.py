from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from App.infrastructure.db.models.empaque import PrincipalEmpaques
from App.infrastructure.db.serializers.empaque_serializer import PrincipalEmpaquesSerializer
from App.infrastructure.db.models.molde_empaque import PrincipalMoldeEmpaque

class EmpaqueView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PrincipalEmpaquesSerializer(data=request.data)
        if serializer.is_valid():
            empaque = serializer.save()
            moldes_data = request.data.get('moldes', [])
            for molde_data in moldes_data:
                molde_id = molde_data['molde']['id']
                color_id = molde_data['color']['id']
                PrincipalMoldeEmpaque.objects.create(
                    empaque=empaque,
                    molde_id=molde_id,
                    color_id=color_id
                )
            colores = ",".join(str(molde_data['color']['id']) for molde_data in moldes_data)
            moldes = ",".join(str(molde_data['molde']['id']) for molde_data in moldes_data)
            response_data = {
                "usuario": "Jisellam",
                "codigo": empaque.codigo,
                "dimensiones": empaque.dimensiones,
                "descripcion": empaque.descripcion,
                "idUso": empaque.idUso_id,
                "idUnidadCobro": empaque.idUnidadCobro_id,
                "capacidad": empaque.capacidad,
                "idMaterial": empaque.idMaterial_id,
                "idTipo": empaque.idTipo_id,
                "estado": empaque.estado,
                "esCencosud": empaque.esCencosud,
                "colores": colores,
                "moldes": moldes
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            empaque = PrincipalEmpaques.objects.get(pk=pk)
        except PrincipalEmpaques.DoesNotExist:
            return Response({'error': 'Empaque not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = PrincipalEmpaquesSerializer(empaque, data=request.data, partial=True)
        if serializer.is_valid():
            empaque = serializer.save()
            # Elimina los moldes-empaque actuales
            PrincipalMoldeEmpaque.objects.filter(empaque=empaque).delete()
            # Crea los nuevos moldes-empaque
            moldes_data = request.data.get('moldes', [])
            for molde_data in moldes_data:
                molde_id = molde_data['molde']['id']
                color_id = molde_data['color']['id']
                PrincipalMoldeEmpaque.objects.create(
                    empaque=empaque,
                    molde_id=molde_id,
                    color_id=color_id
                )
            molde_empaques = PrincipalMoldeEmpaque.objects.filter(empaque=empaque)
            colores = ",".join(str(me.color_id) for me in molde_empaques)
            moldes = ",".join(str(me.molde_id) for me in molde_empaques)
            response_data = {
                "usuario": "Jisellam",
                "codigo": empaque.codigo,
                "dimensiones": empaque.dimensiones,
                "descripcion": empaque.descripcion,
                "idUso": empaque.idUso_id,
                "idUnidadCobro": empaque.idUnidadCobro_id,
                "capacidad": empaque.capacidad,
                "idMaterial": empaque.idMaterial_id,
                "idTipo": empaque.idTipo_id,
                "estado": empaque.estado,
                "esCencosud": empaque.esCencosud,
                "colores": colores,
                "moldes": moldes
            }
            return Response(response_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)