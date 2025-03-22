import icalendar
from pathlib import Path
from requests import get
import json
def format_json_output(event):
    return {
        "title":event["SUMMARY"],
        "content": "",
        "sub_title":event['DTSTART'].dt.strftime('%A %Y-%m-%d %Z  ')
    }
if __name__ == "__main__":
    ics_path = "https://api.twitch.tv/helix/schedule/icalendar?broadcaster_id=253129276"
    calendar = icalendar.Calendar.from_ical(get(ics_path).text)
    timetable = [format_json_output(event) for event in calendar.events]

    json.dump(timetable,open("docs/timetable.json","w"))
