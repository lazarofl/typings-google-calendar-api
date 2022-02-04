import sys
from typing import List

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


class Scope(TypedDict):
    type: str
    value: str


class Acl(TypedDict):
    kind: str
    etag: str
    id: str
    scope: Scope
    role: str
