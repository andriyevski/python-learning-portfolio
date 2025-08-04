# Homework from file tasks/glossary.md
## Task ## : 6.5
# The rivers
from typing import Dict


def rivers() -> Dict[str, str]:
    """Dict with three or more rivers"""
    rivers = {
        'nile':'egypt',
        'usa':'colorado',
        'Ukraine':'dnipro',
        'belarus':'dunai'
    }
    return rivers

def rivers_msg(rivers: Dict[str, str]) -> None:
    """Print message with rivers"""
    count = 0
    for river in rivers.values():
        count+=1
        print(f"{count}. River - {river.title()}")

def countries_msg(rivers: Dict[str, str]) -> None:
    """Message with only country where rivers"""
    count = 0
    for countrie in rivers:
        count+=1
        print(f"{count}. Country with river is - {countrie.title()}")


if __name__ == "__main__":
    rivers_msg(rivers())
    countries_msg(rivers())
