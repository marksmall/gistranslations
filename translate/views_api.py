import logging

from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .converters import csvToGeoJson, gmlToGeoJson, kmlToGeoJson, shapefileToGeoJson

LOGGER = logging.getLogger(__file__)

class TranslateView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            print(f"REQUEST DATA: {request.data}")
            data = request.data['data']
            print(f"EXTRACTED DATA: {request.data['data']}")

            # Image processing here.
            geojson = None
            try:
                geojson = csvToGeoJson(data)
                print(f"GeoJSON: {geojson}")
            except KeyError:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Unable to convert to GeoJSON'})

            reprojected = None
            try:
                reprojected = reproject(geojson)
                print(f"REPROJECTED DATA: {reprojected}")
            except KeyError:
                return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Unable to Re-project data'})


            # Return JSON.
            return JsonResponse({ 'trackingId': 'mytrackingid'}, status=status.HTTP_200_OK)
        except KeyError:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'Expected data to process.'})

@api_view(['GET'])
def translate_view(request):
    """ Return hard-coded app config """
    print(f"REQUEST DATA: {request.data}")
    print(f"REQUEST QUERYSTRING: {request.query_params}")
    LOGGER.info("EVENTUALLY")
    return JsonResponse({ 'trackingId': 'mytrackingid'}, status=status.HTTP_200_OK)
