import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


class ConferenceProperties(TypedDict):
    allowedConferenceSolutionTypes: List[str]


class Calendar(TypedDict):
    kind: str
    etag: str
    id: str
    summary: str
    description: str
    location: str
    timeZone: str
    conferenceProperties: ConferenceProperties