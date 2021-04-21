from typing import List, Tuple
from dataclasses import dataclass, astuple, field


@dataclass
class Character:
    value: str
    count: int = 1

    def increase_count(self):
        self.count += 1


@dataclass
class Characters:
    items: List[Character] = field(default_factory=list)

    def add(self, char: Character) -> None:
        self.items.append(char)
        print(f"Added character {char.value}")

    def current(self) -> Character:
        return self.items[-1]

    def was_previous(self, char: str) -> bool:
        return self.current().value == char

    def __iter__(self):
        return iter(self.items)


def count_characters(input_string: str) -> List[Tuple[str, int]]:
    if len(input_string) == 0:
        return []
    characters = Characters()
    first_char, *rest_of_chars = input_string
    characters.add(
        Character(value=first_char)
    )

    for char in rest_of_chars:
        if characters.was_previous(char):
            characters.current().increase_count()
        else:
            characters.add(
                Character(value=char)
            )

    return [astuple(item) for item in characters]
