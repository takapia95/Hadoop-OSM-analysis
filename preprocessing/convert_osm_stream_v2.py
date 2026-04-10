import ijson

input_file = "/Users/aitran/Downloads/output-us-south.json"
output_file = "/Users/aitran/Downloads/cleaned-us-south-v2.txt"

count = 0

with open(input_file, "rb") as f, open(output_file, "w", encoding="utf-8") as out:
    for feature in ijson.items(f, "features.item"):
        props = feature.get("properties", {})

        if "amenity" in props:
            out.write(f"amenity,{props['amenity']}\n")
            count += 1

        if "highway" in props:
            out.write(f"highway,{props['highway']}\n")
            count += 1

print(f"Done. Wrote {count} records to {output_file}")