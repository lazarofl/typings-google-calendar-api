# typings-google-calendar-api
Python typehint support for Google Calendar API resources.

## Available Resources

### Acl

```python
from typings_google_calendar_api.acl import Acl, Scope
```

Representation: https://developers.google.com/calendar/api/v3/reference/acl#resource-representations

```python
kind: str
etag: str
id: str
scope: Scope
role: str
```

### Calendars

```python
from typings_google_calendar_api.calendars import Calendar, ConferenceProperties
```

Representation: https://developers.google.com/calendar/api/v3/reference/calendarsl#resource-representations

```python
kind: str
etag: str
id: str
summary: str
description: str
location: str
timeZone: str
conferenceProperties: ConferenceProperties
```

### Colors

```python
from typings_google_calendar_api.colors import Color, ColorProperties
```

Representation: https://developers.google.com/calendar/api/v3/reference/colors#resource-representations

```python
kind: str
updated: str
calendar: Dict[str, ColorProperties]
event: Dict[str, ColorProperties]
```


### Events

```python
from typings_google_calendar_api.events import ( Event, Attendee, Date, Person, ExtendedProperties, 
  ConferenceSolutionKey, ConferenceSolution, StatusCode, ConferenceDataCreateRequest, EntryPoint, 
  ConferenceData, Gadget, Override, Reminders, Source, Attachment)
```

Representation: https://developers.google.com/calendar/api/v3/reference/events#resource-representations

```python
kind: str
etag: str
id: str
status: str
htmlLink: str
created: str  # RFC3339 timestamp
updated: str  # RFC3339 timestamp
summary: str
description: str
location: str
colorId: str
creator: Person
organizer: Person
start: Date
end: Date
endTimeUnspecified: bool
recurrence: List[str]
recurringEventId: str
originalStartTime: Date
transparency: str
visibility: str
iCalUID: str
sequence: int
attendees: List[Attendee]
attendeesOmitted: bool
extendedProperties: ExtendedProperties
hangoutLink: str
conferenceData: ConferenceData
gadget: Gadget
anyoneCanAddSelf: bool
guestsCanInviteOthers: bool
guestsCanModify: bool
guestsCanSeeOtherGuests: bool
privateCopy: bool
locked: bool
reminders: Reminders
source: Source
attachments: List[Attachment]
eventType: str
```

## Todo

- [ ] CalendarList resource - Open for contributions :octocat:

### Dependencies

  - [typing_extensions](https://pypi.org/project/typing-extensions/) - for python version < 3.7

### Sample



https://user-images.githubusercontent.com/913314/152586626-0bc19146-8a75-4fbc-a3c8-763c92d7b8c3.mov



