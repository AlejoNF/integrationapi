# App/interfaces/api/rootController.py
from django.http import JsonResponse

def root_view(request):
    return JsonResponse({"message": "API activa en root. Usa /api/hello para los endpoints."})