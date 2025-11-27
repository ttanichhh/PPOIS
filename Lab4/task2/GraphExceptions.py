class GraphBaseException(Exception):
    """Базовое исключение для графа"""
    pass

class VertexException(GraphBaseException):
    """Исключение связанное с вершинами"""
    pass

class EdgeException(GraphBaseException):
    """Исключение связанное с ребрами"""
    pass

class ImmutableObjectException(GraphBaseException):
    """Попытка изменить неизменяемый объект"""
    pass

class VertexNotFoundError(VertexException):
    """Вершина не найдена"""
    pass

class EdgeNotFoundError(EdgeException):
    """Ребро не найдено"""
    pass

class DuplicateVertexError(VertexException):
    """Дублирующаяся вершина"""
    pass

class DuplicateEdgeError(EdgeException):
    """Дублирующееся ребро"""
    pass