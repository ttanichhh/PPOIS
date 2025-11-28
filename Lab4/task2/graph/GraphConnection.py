"""объект ребра, как связаны две вершины и их узлы."""

from typing import Generic, TypeVar

T = TypeVar("T")
P = TypeVar("P")

class GraphConnection(Generic[T, P]):
    __slots__ = ("source_vertex", "target_vertex", "source_node", "target_node", "attributes")

    def __init__(self, source_vertex, target_vertex, source_node, target_node, attributes=None) -> None:
        self.source_vertex = source_vertex # одна вершина (например, A).
        self.target_vertex = target_vertex # другая вершина (например, B).
        self.source_node = source_node # тот GraphNode, который лежит в списке смежности у source_vertex и указывает на target_vertex
        self.target_node = target_node # симметричный GraphNode у другой вершины.
        self.attributes = attributes or {} # словарь с доп. инфой о ребре (None)

    def __repr__(self) -> str:
        return f"Connection({self.source_vertex.value}↔{self.target_vertex.value})"