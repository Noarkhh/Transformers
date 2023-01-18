from __future__ import annotations
from dataclasses import dataclass
from src.color import Color


@dataclass(frozen=True)
class Node:
    node_id: int
    color: Color

    def __repr__(self):
        return str(self.node_id)

    def __eq__(self, other) -> bool:
        if isinstance(other, int):
            return self.node_id == other
        if isinstance(other, Node):
            return self.node_id == other.node_id and self.color == other.color
        return False

    def color_eq(self, other: Node):
        return self.color == other.color


