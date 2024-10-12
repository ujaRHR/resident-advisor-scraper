--- Resident Evil Scraper (I named it, LoL) ---
------------- File Structure -------------


** events (folder)    - containing all locational data as a json file.
** locations (folder) - containing all area id in a json file.
** payloads (folder)  - containing payloads for sending POST request.
** venv (folder)      - python virtual environment

** requirements.txt - containing all necessary packages to run the program.
** event_data.py    - used to scrape specific event information by passing event id.
                      command: python event_data.py event_id -o default.json

** get_area_code.py - used to get area code by location (only valid for Germany).
** duplicate.py     - can be used to removed duplicate event_id from events/xxx.json data
** merge_csv.py     - this can be used for merging all csv files from outputs folder

** total_events.py  - used to get all event date and event id by passing area_code.
                      command: python total_events.py area_code -o munich.json
** fetch_events.py  - this file is use to run the total_events.py n times (n = total location from locations/cities.json ).

** main.py          - the final python file that use the event_data.py to scrape data for a specific event and then merge it into a csv file.


