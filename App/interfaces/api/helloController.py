# App/interfaces/api/helloController.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions

class HelloWorldView(APIView):
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        customer_id = request.query_params.get('customerId', 'No customerId')
        order_status = request.query_params.get('orderStatus', 'No orderStatus')
        return Response({
            'message': 'Hello World GET',
            'customerId': customer_id,
            'orderStatus': order_status
        }, status=status.HTTP_200_OK)

    def post(self, request):
        status_value = request.data.get('status', 'No status')
        message = request.data.get('message', 'No message')
        return Response({
            'message': message,
            'status': status_value
        }, status=status.HTTP_201_CREATED)