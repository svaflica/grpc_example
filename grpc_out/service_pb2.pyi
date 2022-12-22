from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ["text"]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    text: str
    def __init__(self, text: _Optional[str] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["listOfStrings"]
    LISTOFSTRINGS_FIELD_NUMBER: _ClassVar[int]
    listOfStrings: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, listOfStrings: _Optional[_Iterable[str]] = ...) -> None: ...
