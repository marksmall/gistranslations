import pandas
import json

def csvToGeoJson(csv_data):
    """ Convert CSV data to GeoJSON. """
    print(f"CSV DATA TO CONVERT: {csv_data}")
    df = pandas.read_csv(csv_data)
    print(f"READ FILE: {df}")
    headers = df.columns.values.tolist()
    data = df.values
    print(f"HEADERS: {headers}")
    print(f"DATA: {data}")

    geojson = json.dumps(({ "type": "FeatureCollection", "features": [{ "type": "Feature", "geometry": {"type": "Point", "coordinates": [102.0, 0.5]}, "properties": {"prop0": "value0"}}, {"type": "Feature", "geometry": {"type": "Point", "coordinates": [102.0, 0.5]}, "properties": {"prop1": "value1"}}] }))

    return geojson


def gmlToGeoJson(gml_data):
    """ Convert GML to GeoJSON. """
    print(f"GML DATA TO CONVERT: {gml_data}")

def kmlToGeoJson(kml_data):
    """ Convert KML to GeoJSON. """
    print(f"KML DATA TO CONVERT: {kml_data}")

def shapefileToGeoJson(shapefile_data):
    """ Convert ShapeFile to GeoJSON. """
    print(f"SHAPEFILE DATA TO CONVERT: {shapefile_data}")
