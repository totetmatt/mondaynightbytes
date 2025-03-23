import icalendar
from pathlib import Path
from requests import get
import json
def format_json_output(event):

    return {
        "title":event["SUMMARY"],
        "content": event['DTSTART'].dt.strftime('%A %B  %d  %Y'),
        "sub_title":event['DTSTART'].dt.strftime('%Y-%m-%d %Hh%M %Z')
    }
if __name__ == "__main__":
    ics_path = "https://api.twitch.tv/helix/schedule/icalendar?broadcaster_id=253129276"
    calendar = icalendar.Calendar.from_ical(get(ics_path).text)
    events = sorted(calendar.events,key=lambda a:a['DTSTART'].dt)
    timetable = [format_json_output(event) for event in events]

    json.dump(timetable,open("docs/timetable.json","w"))
