import pandas as pd
import universalis
from worlds import World
from io import StringIO

_data_centers_df = pd.read_json(StringIO(universalis.get_data_centers()))
_data_centers_df.set_index("name", inplace=True)


class DataCenter:
    def __init__(self, name: str):
        self._name = name
        self._region = _data_centers_df["region"].get(self._name)

    @property
    def name(self) -> str:
        return self._name

    @property
    def region(self) -> str:
        return self._region

    @property
    def worlds(self) -> list[World]:
        worlds = []
        for world_id in _data_centers_df["worlds"].get(self._name):
            worlds.append(World(world_id))
        return worlds


_data_centers_list = []
for index, row in _data_centers_df.iterrows():
    _data_centers_list.append(DataCenter(str(index)))


def get_data_centers() -> list[DataCenter]:
    return _data_centers_list


def get_datacenter(name: str) -> DataCenter:
    for dc in _data_centers_list:
        if dc.name == name:
            return dc
    raise LookupError("No such data center by name " + name)
