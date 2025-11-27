from typing import Generic, TypeVar, Optional
from graph.GraphNode import GraphNode

T = TypeVar("T")
P = TypeVar("P")

class GraphVertex(Generic[T, P]):
    __slots__ = ("value", "properties", "matrix_index", "first_connection")

    def __init__(self, value: T, properties: P, matrix_index: int) -> None:
        self.value = value
        self.properties = properties
        self.matrix_index = matrix_index
        self.first_connection: Optional[GraphNode[T, P]] = None

    def __repr__(self) -> str:
        return f"Vertex('{self.value}', idx:{self.matrix_index})"