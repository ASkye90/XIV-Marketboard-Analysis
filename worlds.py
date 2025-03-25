from typing import override

import pandas as pd
import universalis
from io import StringIO

_worlds_df = pd.read_json(StringIO(universalis.get_available_worlds()))
_worlds_df.set_index("id", inplace=True)


class World:
    def __init__(self, _id):
        self._id = _id
        self._name = _worlds_df["name"].get(self._id)

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name


_worlds_list = []
for index, row in _worlds_df.iterrows():
    _worlds_list.append(World(index))


def get_world(name_or_id: str | int) -> World:
    for world in _worlds_list:
        if world.id == name_or_id or world.name == name_or_id:
            return world
    raise LookupError("No such world by id or name " + str(name_or_id))


def get_worlds() -> list[World]:
    return _worlds_list
