import requests
import simplejson as json

from decimal import Decimal
from requests.exceptions import HTTPError

url = "https://check.edu.gov.kg/api.php?action=geoData"


def main():

    result = {
        "type": "FeatureCollection",
        "features": []
    }

    try:
        response = requests.get(url)

        data = response.json()['data']

        for elem in data:
            result["features"].append({
                "type": "Feature",
                "properties": {},
                "geometry": {
                    "coordinates": [
                        Decimal(elem['longitude']),
                        Decimal(elem['latitude']),
                        Decimal(elem['fullness'])
                    ],
                    "type": "Point"
                }
            })

        with open('result.geojson', 'w', encoding='utf-8') as f:
            json.dump(result, f)

    except HTTPError as http_error:
        print("Произошла ошибка с http")
        print(http_error)

    except Exception as err:
        print("Произошла неизвестная ошибка")
        print(err)


if __name__ == "__main__":
    main()
