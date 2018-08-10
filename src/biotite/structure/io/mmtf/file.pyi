from numpy import ndarray
from typing import (
    Dict,
    List,
    Optional,
    Union,
)


class MMTFFile:
    def __delitem__(self, key: str) -> None: ...
    def __getitem__(
        self,
        key: str
    ) -> Union[ndarray, List[int], List[Dict[str, Union[str, List[str], List[int]]]], int, str]: ...
    def __init__(self) -> None: ...
    def __setitem__(
        self,
        key: str,
        item: Union[List[int], List[Dict[str, Union[str, List[str], List[int]]]], int]
    ) -> None: ...
    def get_codec(self, key: str) -> Optional[int]: ...
    def get_param(self, key: str) -> int: ...
    def read(self, file: str) -> None: ...
    def set_array(self, key: str, array: ndarray, codec: int, param: int = 0) -> None: ...
    def write(self, file: str) -> None: ...
