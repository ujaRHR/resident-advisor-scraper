import os
import json

folder_path = "events"

for filename in os.listdir(folder_path):
    if filename.endswith(".json"):
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "r") as f:
            data = json.load(f)

        seen_event_ids = set()
        unique_data = []

        for event in data:
            if event["event_id"] not in seen_event_ids:
                unique_data.append(event)
                seen_event_ids.add(event["event_id"])

        with open(file_path, "w") as f:
            json.dump(unique_data, f, indent=4)