import json
import datetime
import time
import webbrowser
import schedule
import playsound
import os 
import sys

def handle_input_data(id: int, metadata: str):
    data = {
        "subject" : "",
        "time" : "",
        "id" : "",
        "link": ""
    }
    try:
        meta_topic = metadata.find("Topic: ")
        meta_datetime = metadata.find("Time: ")
        meta_brkpnt = metadata.find("AM")
        data["subject"] = metadata[meta_topic+7:meta_datetime]
        data["time"] = metadata[meta_datetime+6:meta_brkpnt][-6:-1]
        data["id"] = id
        for s in metadata.split():
            if s.startswith("https://"):
                data["link"]=s
    except:
        pass
    
    return data

def notify(msg, title="", state="critical"):
    playsound.playsound("./assets/notify.mp3")
    os.system(f"notify-send '{title}' '{msg}' -a 'Online Class' -i Zoom -u {state} ")

def join_meeting(meeting: dict):
    print(meeting)
    notify(
        f"\n\nStarting {meeting.subject} class...",
        title=f"It is {meeting.time}"
    )
    webbrowser.open(meeting["link"])
    return schedule.CancelJob

if __name__ == "__main__":
    data = (sys.argv[1])
    classlist = data.split("---")
    for n, entry in enumerate(classlist):
        print(meeting)
        meeting = handle_input_data(n, entry)
        
        meeting_time = meeting["time"]
        schedule.every().day.at(meeting_time).do(join_meeting, meeting)
        print(schedule.get_jobs())
        
    while True:
        schedule.run_pending()
        time.sleep(1)
