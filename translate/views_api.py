from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def translate_view(request):
    """ Return hard-coded app config """
    return JsonResponse({ 'trackingId': 'mytrackingid'}, status=status.HTTP_200_OK)
