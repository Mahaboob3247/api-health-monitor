import requests
import time
import json
from datetime import datetime

from logger import logger
from config_loader import load_apis

results = []

apis = load_apis()

print("\nAPI HEALTH MONITOR\n")

for api in apis:

    try:
        start = time.time()

        response = requests.get(
            api["url"],
            timeout=5
        )

        response_time = round(
            time.time() - start,
            3
        )

        entry = {
            "name": api["name"],
            "status": response.status_code,
            "response_time": response_time,
            "timestamp": datetime.now().isoformat()
        }

        results.append(entry)

        logger.info(entry)

        print(
            f"✅ {api['name']} "
            f"{response.status_code} "
            f"{response_time}s"
        )

    except Exception as e:

        entry = {
            "name": api["name"],
            "status": "FAILED",
            "error": str(e)
        }

        results.append(entry)

        logger.error(entry)

        print(f"❌ {api['name']} {e}")

with open("reports/report.json", "w") as file:
    json.dump(results, file, indent=4)