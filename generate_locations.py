import csv
import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "campus_locations.csv"
js_path = base_dir / "locations.js"

locations = []

with csv_path.open("r", encoding="utf-8", newline="") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        name = (row.get("name") or "").strip()
        category = (row.get("category") or "").strip()
        coords = (row.get("coords") or "").strip()
        description = (row.get("description") or "").strip()

        if not name or not category or not coords:
            continue

        locations.append({
            "name": name,
            "category": category,
            "coords": coords,
            "desc": description,
        })

js_content = "window.LOCATIONS = " + json.dumps(locations, ensure_ascii=False, indent=2) + ";\n"
js_path.write_text(js_content, encoding="utf-8")

print(f"Generated {len(locations)} locations into {js_path.name}")
