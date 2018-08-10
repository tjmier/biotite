# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.

from typing import Union, IO, TextIO, AnyStr
from .copyable import Copyable


class File:
    def __init__(self) -> None: ...
    def read(self, file: Union[str, IO[AnyStr]]) -> None: ...
    def write(self, file: Union[str, IO[AnyStr]]) -> None: ...

class TextFile(Copyable):
    def __init__(self) -> None: ...
    def read(self, file: Union[str, TextIO]) -> None: ...
    def write(self, file: Union[str, TextIO]) -> None: ...
    def __str__(self) -> str: ...
