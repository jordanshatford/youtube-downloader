import json

from main import app

OUTPUT_FILENAME = 'openapi.json'

try:
    print(f'Dumping OpenAPI specification to {OUTPUT_FILENAME}')
    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(app.openapi(), file, indent=4)
except Exception as e:
    raise SystemExit(e)
