from UndirectedGraph import UndirectedGraph

def DemonstrateGraph():
    print("=== Демонстрация неориентированного графа с модифицированной структурой Вирта ===\n")

    # Создаем граф для хранения городов и расстояний
    transportation_network = UndirectedGraph[str, dict]()

    # Добавляем города (вершины)
    print("Добавляем города:")
    cities = ["Москва", "СПб", "Казань", "Новосибирск"]
    for city in cities:
        transportation_network.insert_vertex(city, {"population": 1000000})
        print(f"  Добавлен город: {city}")

    print(f"\nКоличество городов: {transportation_network.get_vertex_count()}")

    # Добавляем дороги (связи)
    print("\nСтроим дороги:")
    roads = [
        ("Москва", "СПб", {"distance": 700}),
        ("Москва", "Казань", {"distance": 800}),
        ("СПб", "Казань", {"distance": 1200}),
        ("Москва", "Новосибирск", {"distance": 2800})
    ]

    for city1, city2, attrs in roads:
        transportation_network.create_connection(city1, city2, attrs)
        print(f"  Построена дорога: {city1} ↔ {city2}")

    print(f"\nКоличество дорог: {transportation_network.get_connection_count()}")

    # Демонстрация структуры
    print("\n" + "=" * 50)
    print("СТРУКТУРА ГРАФА:")
    print("=" * 50)

    print(f"\nОбщая информация:")
    print(f"  Граф: {transportation_network}")
    print(f"  Пуст ли граф: {transportation_network.is_graph_empty()}")

    print(f"\nСтепени вершин:")
    for vertex in transportation_network.vertex_iterator():
        degree = transportation_network.calculate_vertex_degree(vertex.value)
        print(f"  Город {vertex.value}: соединен с {degree} городами")

    print(f"\nСмежные города для Москвы:")
    for neighbor in transportation_network.adjacent_vertex_iterator("Москва"):
        print(f"  - {neighbor.value}")

    print(f"\nВсе дороги (итератор):")
    for road in transportation_network.connection_iterator():
        print(f"  {road.source_vertex.value} ↔ {road.target_vertex.value}")

    # Демонстрация удаления
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ УДАЛЕНИЯ:")
    print("=" * 50)

    print("\nУдаляем дорогу Москва-СПб:")
    transportation_network.remove_connection("Москва", "СПб")
    print(f"Количество дорог после удаления: {transportation_network.get_connection_count()}")

    print(f"\nПроверяем существование дороги Москва-СПб: {transportation_network.connection_exists('Москва', 'СПб')}")

    # Демонстрация неизменяемых итераторов
    print("\n" + "=" * 50)
    print("НЕИЗМЕНЯЕМЫЕ ИТЕРАТОРЫ:")
    print("=" * 50)

    print("\nГорода (неизменяемый итератор):")
    for city in transportation_network.immutable_vertex_iterator():
        print(f"  {city.value} (неизменяемый)")

    # Демонстрация удаления по итератору
    print("\n" + "=" * 50)
    print("УДАЛЕНИЕ ПО ИТЕРАТОРУ:")
    print("=" * 50)

    # Удаление ребра по итератору
    print("Удаляем ребро по итератору:")
    edge_iter = transportation_network.connection_iterator()
    first_edge = next(edge_iter)
    print(f"Удаляем: {first_edge.source_vertex.value} ↔ {first_edge.target_vertex.value}")
    transportation_network.delete_connection_via_iterator(edge_iter)
    print(f"Осталось рёбер: {transportation_network.get_connection_count()}")

    # Удаление вершины по итератору
    print("\nУдаляем вершину по итератору:")
    vertex_iter = transportation_network.vertex_iterator()
    first_vertex = next(vertex_iter)
    print(f"Удаляем: {first_vertex.value}")
    transportation_network.delete_vertex_via_iterator(vertex_iter)
    print(f"Осталось вершин: {transportation_network.get_vertex_count()}")


if __name__ == "__main__":
    DemonstrateGraph()