# GIS Translations

- [GIS Translations](#gis-translations)
  - [Overview](#overview)
  - [Examples](#examples)

## Overview

The purpose of this micro-service is to receive, process and return GeoJSON. The service will take a number of formats e.g. `CSV`, `KML`, `GML`, `Shapefiles` etc.

## Examples

```bash
curl -F data=@eon_bid_team_property_list.csv http://localhost:8000/api/translate/
```
