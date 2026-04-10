import ijson

input_file = "/Users/aitran/Downloads/output-us-south.json"
output_file = "/Users/aitran/Downloads/cleaned-us-south.txt"

count = 0

with open(input_file, "rb") as f, open(output_file, "w", encoding="utf-8") as out:
    for feature in ijson.items(f, "features.item"):
        props = feature.get("properties", {})
        feature_type = props.get("@type", "unknown")

        if "amenity" in props:
            out.write(f"{feature_type},amenity,{props['amenity']}\n")
            count += 1

        if "highway" in props:
            out.write(f"{feature_type},highway,{props['highway']}\n")
            count += 1

print(f"Done. Wrote {count} records to {output_file}")