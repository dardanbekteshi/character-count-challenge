from typing import List, Tuple
from dataclasses import dataclass, astuple, field


@dataclass
class Character:
    char: str
    count: int

    def increase(self):
        self.count += 1


@dataclass
class Characters:
    items: List[Character] = field(default_factory=list)

    def add(self, item: Character) -> None:
        self.items.append(item)

    def is_current(self, char: str) -> bool:
        return self.items[-1].char == char

    def increase_current(self) -> None:
        return self.items[-1].increase()

    def __iter__(self):
        return iter(self.items)


def count_chars_in_order(input_string: str) -> List[Tuple[str, int]]:
    characters = Characters()
    first, *rest = input_string
    characters.add(Character(first, 1))

    for char in rest:
        print(f"processing :{char}")
        if characters.is_current(char):
            characters.increase_current()
        else:
            characters.add(Character(char, 1))

    return [astuple(item) for item in characters]
