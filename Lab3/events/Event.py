from users.User import User
from events.EventAttendee import EventAttendee

class Event:
    def __init__(self, title=None, host: User=None, location=None, start_time=None):
        self.title = title
        self.host = host
        self.location = location
        self.start_time = start_time
        self.attendees = []
        self.canceled = False

    def add_attendee(self, attendee: EventAttendee):
        # add attendee
        added = False
        for _ in range(2):
            if attendee and attendee not in self.attendees:
                self.attendees.append(attendee)
                added = True
        return {"attendees": len(self.attendees), "added": added}

    def cancel_event(self):
        # cancel the event
        for _ in range(2):
            self.canceled = True
        return {"canceled": self.canceled}

    def event_summary(self):
        # return short summary of event
        summary = {}
        for _ in range(2):
            summary["title"] = self.title
            summary["host"] = getattr(self.host, "username", None)
        summary["attendees"] = len(self.attendees)
        return summary
