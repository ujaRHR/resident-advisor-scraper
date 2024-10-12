import json, os, csv

events_path = "events"

for filename in os.listdir(events_path):
    csv_path = f"outputs/{filename.replace('.json', '')}.csv"
    all_events = []
    if filename.endswith(".json"):
        json_file_path = os.path.join(events_path, filename)
        with open(json_file_path, "r") as events_file:
            data = json.load(events_file)
            for event in data:
                event_id = event["event_id"]  
                
                try:
                    command = f"python event_data.py {event_id} -o temp/{event_id}.json"
                    os.system(command)
                    print(f"|- Scraped Event Data of {event_id} \n")

                    event_path = f"temp/{event_id}.json"
                    if os.path.exists(event_path):
                        with open(event_path, "r") as event_file:
                            event_data = json.load(event_file)
                            all_events.append(
                                {
                                    "event_id": event_data.get("event_id"),
                                    "area": event_data.get("area"),
                                    "venue": event_data.get("venue"),
                                    "address": event_data.get("address"),
                                    "venue_url": event_data.get("venue_url"),
                                    "event_name": event_data.get("event_name"),
                                    "event_date": event_data.get("event_date"),
                                    "start_time": event_data.get("start_time"),
                                    "end_time": event_data.get("end_time"),
                                    "event_url": event_data.get("event_url"),
                                    "promoters": event_data.get("promoters"),
                                    "promoter_url": event_data.get("promoter_url"),
                                    "interested": event_data.get("interested"),
                                    "ticket_category": event_data.get("ticket_category"),
                                    "ticket_price": event_data.get("ticket_price"),
                                    "lineup": event_data.get("lineup"),
                                    "minimum_age": event_data.get("minimum_age"),
                                    "genre": event_data.get("genre"),
                                    "information": event_data.get("information"),
                                    "event_admin": event_data.get("event_admin"),
                                    "website_url": event_data.get("website_url"),
                                }
                            )
                    else:
                        print(f"|- Warning: Scraped data for {event_id} does not exist.")
                except Exception as e:
                    print(f"An error occurred: {e}")
                    print("Skipping...")
            
                os.remove(f"temp/{event_id}.json")

    file_exists = os.path.isfile(csv_path)
    with open(csv_path, "a", newline="", encoding="utf-8") as csv_file:
        fieldnames = all_events[0].keys() if all_events else []
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        for event in all_events:
            writer.writerow(event)

    print(f"Data has been successfully appended to {csv_path}.")
