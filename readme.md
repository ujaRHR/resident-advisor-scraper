## Resident Advisor Scraper

## Installation
1. Clone the repository or download the source code.
2. Run ```pip install -r requirements.txt``` to install the required libraries.

## Example
To fetch events for area 34 (Berlin, DE) from October 05, 2024, and save them to a JSON file named events/berlin.json, run the following command:

``` python fetch_events.py 34 2023-04-23 2023-04-29 -o berlin.json```


### File Structure
- events: containing all locational data as a JSON file.
- locations: containing all area IDs in a JSON file.
- payloads: containing payloads for sending POST requests.
- venv: python virtual environment

- requirements.txt: containing all necessary packages to run the program.
- event_data.py: used to scrape specific event information by passing event ID.
                      command: ``` python event_data.py event_id -o default.json```

- get_area_code.py: used to get area code by location (only valid for Germany).
                    command: ```python get_area_code.py```
- duplicate.py: can be used to remove duplicate event_id from events/xxx.json data
- merge_csv.py: this can be used for merging all CSV files from the outputs folder

- total_events.py: used to get all event date and event IDs by passing area_code.
                      command: python total_events.py area_code -o munich.json
- fetch_events.py: this file is use to run the total_events.py n times (n = total location from locations/cities.json ).

- main.py: the final Python file that uses the event_data.py to scrape data for a specific event and then merge it into a CSV file.
