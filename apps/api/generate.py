import json
import logging
import pathlib

from app.main import app

logger = logging.getLogger("generate")

OUTPUT_FILENAME = "openapi.json"

try:
    logger.info("Dumping OpenAPI specification to %s", OUTPUT_FILENAME)
    with pathlib.Path(OUTPUT_FILENAME).open("w") as file:
        json.dump(app.openapi(), file, indent=2)
        file.write("\n")
except Exception as e:
    logger.exception("Error dumping OpenAPI specification to %s", OUTPUT_FILENAME)
    raise SystemExit(e) from e
