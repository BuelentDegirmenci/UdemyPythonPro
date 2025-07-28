from __future__ import annotations


from typing import Dict
from typing import Mapping
from typing import Union


def iterate_over_dict(my_dict: Mapping[str, Union[int, float]]) -> None:
    for key, val in my_dict.items():
        print(key, val)
    # eturn my_dict

if __name__ == "__main__":
    values = [1, 2, 3]
    expand_ration = 2

    my_dict = {"Jan": 26, "Peter": 32}
    iterate_over_dict(my_dict)
