import json

from yad_api.main import app

OUTPUT_FILENAME = 'openapi.json'

try:
    print(f'Dumping OpenAPI specification to {OUTPUT_FILENAME}')
    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(app.openapi(), file, indent=4)
        file.write('\n')
except Exception as e:
    raise SystemExit(e)
