from typing import Generic, TypeVar

T = TypeVar("T")
P = TypeVar("P")

class GraphConnection(Generic[T, P]):
    __slots__ = ("source_vertex", "target_vertex", "source_node", "target_node", "attributes")

    def __init__(self, source_vertex, target_vertex, source_node, target_node, attributes=None) -> None:
        self.source_vertex = source_vertex
        self.target_vertex = target_vertex
        self.source_node = source_node
        self.target_node = target_node
        self.attributes = attributes or {}

    def __repr__(self) -> str:
        return f"Connection({self.source_vertex.value}↔{self.target_vertex.value})"