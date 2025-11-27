from typing import Generic, TypeVar, Optional

T = TypeVar("T")
P = TypeVar("P")

class GraphNode(Generic[T, P]):
    __slots__ = ("connected_vertex", "row_index", "column_index", "prev_node", "next_node")

    def __init__(self, connected_vertex: 'GraphVertex[T, P]', row_index: int, column_index: int):
        self.connected_vertex = connected_vertex
        self.row_index = row_index
        self.column_index = column_index
        self.prev_node: Optional["GraphNode[T, P]"] = None
        self.next_node: Optional["GraphNode[T, P]"] = None

    def __repr__(self) -> str:
        return f"Node(to:{self.connected_vertex.value})"