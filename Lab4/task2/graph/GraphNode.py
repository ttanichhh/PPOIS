"""Узел списка смежности (как описан один «выход» из вершины).
GraphNode — это «узел ребра» в списке смежности,
то есть один элемент двусвязного списка соседей вершины в твоём графе."""


from typing import Generic, TypeVar, Optional

T = TypeVar("T")
P = TypeVar("P")

# connected_vertex: 'GraphVertex[T, P]'
# это вершина, к которой ведёт это ребро. Если этот узел хранится в списке у вершины A,
# то connected_vertex — это, например, вершина B (конец ребра A–B)
class GraphNode(Generic[T, P]):
    __slots__ = ("connected_vertex", "row_index", "column_index", "prev_node", "next_node")

    def __init__(self, connected_vertex: 'GraphVertex[T, P]', row_index: int, column_index: int):
        self.connected_vertex = connected_vertex
        # Позиция соответствующего ребра в матрице смежности (строка и столбец).
        self.row_index = row_index
        self.column_index = column_index
        # Ссылки на предыдущий и следующий узел в двусвязном списке смежности.
        self.prev_node: Optional["GraphNode[T, P]"] = None
        self.next_node: Optional["GraphNode[T, P]"] = None
        # Для каждой вершины есть цепочка таких узлов:
        # first_connection → Node(to:...) → Node(to:...) → ...

    def __repr__(self) -> str:
        return f"Node(to:{self.connected_vertex.value})"