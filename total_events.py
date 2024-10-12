import requests
import json
import time
import sys
import argparse
from datetime import datetime, timedelta

URL = "https://de.ra.co/graphql"
HEADERS = {
    "Content-Type": "application/json",
    "Referer": "https://de.ra.co/events/de/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
}

QUERY_TEMPLATE_PATH = "payloads/all_events.json"
DELAY = 2
global totalPage
totalPage = 1


class EventFetcher:
    """
    A class to fetch and print event details from RA.co
    """

    def __init__(self, areas, listing_date_gte):
        self.payload = self.generate_payload(areas, listing_date_gte)

    @staticmethod
    def generate_payload(areas, listing_date_gte):
        """
        Generate the payload for the GraphQL request.

        :param areas: The area code to filter events.
        :param listing_date_gte: The start date for event listings (inclusive).
        :return: The generated payload.
        """
        with open(QUERY_TEMPLATE_PATH, "r") as file:
            payload = json.load(file)

        payload["variables"]["filters"]["areas"]["eq"] = areas
        payload["variables"]["filters"]["listingDate"]["gte"] = listing_date_gte

        return payload

    def get_events(self, page_number):
        """
        Fetch events for the given page number.

        :param page_number: The page number for event listings.
        :return: A list of events.
        """
        self.payload["variables"]["page"] = page_number
        response = requests.post(URL, headers=HEADERS, json=self.payload)

        try:
            response.raise_for_status()
            data = response.json()
        except (requests.exceptions.RequestException, ValueError):
            print(f"Error: {response.status_code}")
            return []

        if "data" not in data:
            print(f"Error: {data}")
            return []

        global totalPage
        totalPage = int(data["data"]["eventListings"]["totalResults"] / 100) + 1

        return data["data"]["eventListings"]["data"]

    def fetch_all_events(self):
        """
        Fetch all events and return them as a list.

        :return: A list of all events.
        """
        all_events = []
        page_number = 1

        while True:
            events = self.get_events(page_number)

            if not events:
                break

            all_events.extend(events)
            page_number += 1
            time.sleep(DELAY)

        return all_events

    def save_events_to_json(self, events, output_file="events.json"):
        """
        Save events to a JSON file.

        :param events: A list of events.
        :param output_file: The output file path. (default: "events.json")
        """
        data = []
        for idx, event in enumerate(events):
            event_data = event["event"]
            data.append(
                {
                    "id": idx,
                    "date": event_data["date"],
                    "event_id": int(event_data["contentUrl"].split("/")[-1]),
                }
            )

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    parser = argparse.ArgumentParser(
        description="Fetch events from ra.co and save them to a JSON file."
    )
    parser.add_argument("areas", type=int, help="The area code to filter events.")
    parser.add_argument(
        "start_date",
        type=str,
        help="The start date for event listings (inclusive, format: YYYY-MM-DD).",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="events.json",
        help="The output file path (default: events.json).",
    )
    args = parser.parse_args()

    listing_date_gte = f"{args.start_date}T00:00:00.000Z"

    event_fetcher = EventFetcher(args.areas, listing_date_gte)

    all_events = []
    current_start_date = datetime.strptime(args.start_date, "%Y-%m-%d")
    currentPage = 0

    while currentPage < totalPage:
        listing_date_gte = current_start_date.strftime("%Y-%m-%dT00:00:00.000Z")
        event_fetcher.payload = event_fetcher.generate_payload(
            args.areas, listing_date_gte
        )
        events = event_fetcher.fetch_all_events()

        if not events:
            break

        all_events.extend(events)
        current_start_date += timedelta(days=len(events))
        currentPage += 1

    event_fetcher.save_events_to_json(all_events, args.output)


if __name__ == "__main__":
    main()
