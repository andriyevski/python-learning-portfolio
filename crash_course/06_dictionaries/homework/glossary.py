# Homework from file tasks/glossary.md
## Task ## : 6.4
# Golossary 2
from typing import Dict

def popular_lang() -> Dict[str, object]:
    """
    Five or more language in dict
    """
    lang_explain = {
    'Python':'Simple but powerful language',
    'c':'Hard, fast, clear language, you can control memory!',
    'C#':'Simple if compare with C but have much more tools and good OOP',
    'php':'Powerful for sites and 90% all sites in web write on PHP',
    'js':'Simple dinamic language, uses for front most of all cases, but you can write for backand',
    'go':'So cool for microservices!',
    'java':'Old but good for banking and almoust all in real life what we use!',
    'c++':'Used in every hard task if you need speed and memory control!'}
    return lang_explain


def lang_message(languages: Dict[str, object]) -> None:
    """
    Print all words in list with message in good format!
    """
    for key, val in languages.items():
        print(f"The language: {key.title()} - {val}")

if __name__ == "__main__":
    lang_message(popular_lang())
