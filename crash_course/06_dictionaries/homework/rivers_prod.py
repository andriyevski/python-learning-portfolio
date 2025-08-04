# Production level
from typing import Dict,Literal


Rivers_Dict = Dict[str,str]

def get_rivers() -> Rivers_Dict:
    """
    Print rivers, countries, or both depending on mode.

    Args:
        data (Dict[str, str]): Dictionary with rivers and their corresponding countries.
        mode (str): "all", "countries", or "rivers" to control output.

    Example:
        >>> print_info(get_rivers(), mode="rivers")
        1. Nile
        2. Amazon
        3. Dnepr
    """

    return {
    'nile':'egypt',
    'amazon':'brazil',
    'dnepr':'Ukraine'
    }

def print_info(data: Rivers_Dict, mode: Literal["all","countries","rivers"] = "all") -> None:
    """Print rivers with using mode: all, countries, rivers"""
    if mode in ("all","rivers"):
        print("\nRivers:")
        for i, river in enumerate(data,1):
            print(f"{i}.{river.title()}")
    if mode in ("all","countries"):
        print("\nCountries:")
        for i, countrie in enumerate(data.values(),1):
            print(f"{i}.{countrie.title()}")

if __name__ =="__main__":
    print_info(get_rivers())
