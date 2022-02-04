import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


class Attendee(TypedDict):
    id: str
    email: str
    displayName: str
    organizer: bool
    responseStatus: str
    self: bool
    resource: bool
    optional: bool
    responseStatus: str
    comment: str
    additionalGuests: int


class Date(TypedDict):
    dateTime: str
    date: str
    timeZone: str


class Person(TypedDict):
    id: str
    email: str
    displayName: str
    self: bool


class ExtendedProperties(TypedDict):
    private: dict
    shared: dict


class ConferenceSolutionKey(TypedDict):
    type: str


class ConferenceSolution(TypedDict):
    key: ConferenceSolutionKey
    name: str
    iconUri: str


class StatusCode(TypedDict):
    code: str


class ConferenceDataCreateRequest(TypedDict):
    requestId: str
    conferenceSolutionKey: ConferenceSolutionKey
    status: StatusCode


class EntryPoint(TypedDict):
    entryPointType: str
    uri: str
    label: str
    pin: str
    accessCode: str
    meetingCode: str
    passcode: str
    password: str


class ConferenceData(TypedDict):
    createRequest: ConferenceDataCreateRequest
    entryPoints: List[EntryPoint]
    conferenceSolution: ConferenceSolution
    conferenceId: str
    signature: str
    notes: str


class Gadget(TypedDict):
    type: str
    title: str
    link: str
    iconLink: str
    width: int
    height: int
    display: str
    preferences: dict


class Override(TypedDict):
    method: str
    minutes: int


class Reminders(TypedDict):
    useDefault: bool
    overrides: List[Override]


class Source(TypedDict):
    url: str
    title: str


class Attachment(TypedDict):
    fileUrl: str
    title: str
    mimeType: str
    iconLink: str
    fileId: str


class Event(TypedDict):
    """
    Type hint support for a Google Calendar Event Resource.
    https://developers.google.com/calendar/api/v3/reference/events?hl=en#resource-representations
    """

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
