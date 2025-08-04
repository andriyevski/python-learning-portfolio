# Homework from file tasks/glossary.md
## Task ## : 6.5
# The river
from typing import Dict


def rivers() -> Dict[str, object]:
    """Dict with three or more rivers"""
    rivers = {
        'nile':'egypt',
        'usa':'colorado',
        'Ukraine':'dnipro',
        'belarus':'dunai'
    }
    return rivers

def rivers_msg(rivers: Dict[str, object]) -> None:
    """Print message with rivers"""
    count = 0
    for river in rivers.values():
        count+=1
        print(f"{count}. River - {river.title()}")

def country_rivers_msg(rivers: Dict[str, object]) -> None:
    """Message with only country where rivers"""
    count = 0
    for country in rivers:
        count+=1
        print(f"{count}. Country with river is - {country.title()}")


if __name__ == "__main__":
    rivers_msg(rivers())
    country_rivers_msg(rivers())
