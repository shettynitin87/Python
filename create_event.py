from setup_calendar import get_calendar_service
from configparser import ConfigParser
from datetime import datetime

'''
Funtion to create a calendar event as per the data provided
'''


def insert_the_event(start_dateTime, end_dateTime):
    # It will check whether the user is logged in or not. If user is logged in, the process will be bypassed
    service = get_calendar_service()

    # Start Time
    d = datetime.strptime(start_dateTime, '%m/%d/%Y %H:%M:%S')
    startTime = datetime(d.year, d.month, d.day, d.hour, d.minute, d.second)
    start = startTime.isoformat()

    # End Time
    e = datetime.strptime(end_dateTime, '%m/%d/%Y %H:%M:%S')
    endTime = datetime(e.year, e.month, e.day, e.hour, e.minute, e.second)
    end = endTime.isoformat()

    event_result = service.events().insert(calendarId='primary',
                                           body={
                                               "summary": 'Automating calendar',
                                               "description": 'This is a tutorial example of automating google calendar with python',
                                               "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
                                               "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
                                           }
                                           ).execute()

    print("created event")
    print("id: ", event_result['id'])
    print("summary: ", event_result['summary'])
    print("starts at: ", event_result['start']['dateTime'])
    print("ends at: ", event_result['end']['dateTime'])


if __name__ == '__main__':
    # Reading the required information from a file, that consists of 10 events along with date, start time and end time
    parser = ConfigParser()
    parser.read("events.ini")

    # Running in loop to read events and create the same on calendar
    for count in range(1, 11):
        start_time = parser.get("Event" + str(count), "starttime")
        end_time = parser.get("Event" + str(count), "endtime")

        insert_the_event(start_time, end_time)
