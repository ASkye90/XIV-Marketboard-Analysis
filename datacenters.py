import pandas as pd
import universalis
from worlds import World
from io import StringIO

_data_centers_df = pd.read_json(StringIO(universalis.get_data_centers()))
_data_centers_df.set_index("name", inplace=True)


class DataCenter:
    def __init__(self, name):
        self._name = name
        self._region = _data_centers_df["region"].get(self._name)

    @property
    def name(self):
        return self._name

    @property
    def region(self):
        return self._region

    def worlds(self):
        worlds = []
        for world_id in _data_centers_df["worlds"].get(self._name):
            worlds.append(World(world_id))
        return worlds

    def __eq__(self, other):
        return self._name == other.name

_data_centers_list = []
for index, row in _data_centers_df.iterrows():
    _data_centers_list.append(DataCenter(index))


def get_datacenter(name):
    for dc in _data_centers_list:
        if dc.name == name:
            return dc
    raise LookupError("No such data center by name " + name)
