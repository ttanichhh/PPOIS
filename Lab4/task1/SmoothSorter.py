class SmoothSorter:
    def __init__(self):
        self.leo = []

    def _build_leonardo(self, limit: int):
        """Возвращает список чисел Леонардо, не превышающих limit."""
        a, b = 1, 1
        res = []
        while a <= limit:
            res.append(a)
            a, b = b, a + b + 1
        return res

    def _split_tree(self, root_idx, order, leo):
        """Для корня дерева Леонардо возвращает индексы корней двух поддеревьев."""
        right_root = root_idx - 1
        right_order = order - 2
        left_root = right_root - leo[right_order]
        left_order = order - 1
        return right_root, right_order, left_root, left_order

    def _heapify_up_down(self, seq, i, heap_orders, leo):
        """
        Восстанавливает свойства «леса» деревьев Леонардо:
        сначала двигаем корень вверх между деревьями, затем просеиваем вниз.
        """
        pos = len(heap_orders) - 1
        order = heap_orders[pos]

        # Подъём корня вверх по деревьям
        while pos > 0:
            j = i - leo[order]
            # Проверяем, нужно ли поднимать элемент на позицию j
            if (
                    seq[j] > seq[i]
                    and (order < 2 or (seq[j] > seq[i - 1] and seq[j] > seq[i - 2]))
            ):
                seq[i], seq[j] = seq[j], seq[i]
                i = j
                pos -= 1
                order = heap_orders[pos]
            else:
                break

        # Просеивание вниз внутри одного дерева
        while order >= 2:
            right_root, right_order, left_root, left_order = self._split_tree(i, order, leo)
            # выбираем большего ребёнка
            child = right_root if seq[right_root] > seq[left_root] else left_root
            child_order = right_order if child == right_root else left_order

            if seq[i] < seq[child]:
                seq[i], seq[child] = seq[child], seq[i]
                i, order = child, child_order
            else:
                break

    def sort(self, seq):
        """
        Основной метод сортировки Smoothsort.
        """
        n = len(seq)
        if n < 2:
            return seq

        leo = self._build_leonardo(n)
        heap_orders = []

        # Построение «леса» деревьев Леонардо
        for i in range(n):
            if len(heap_orders) >= 2 and heap_orders[-2] == heap_orders[-1] + 1:
                heap_orders.pop()
                heap_orders[-1] += 1
            else:
                if heap_orders and heap_orders[-1] == 1:
                    heap_orders.append(0)
                else:
                    heap_orders.append(1)
            self._heapify_up_down(seq, i, heap_orders, leo)

        # Разбор леса
        for i in range(n - 1, -1, -1):
            if heap_orders[-1] < 2:
                heap_orders.pop()
            else:
                order = heap_orders.pop()
                right_root, right_order, left_root, left_order = self._split_tree(i, order, leo)

                heap_orders.append(left_order)
                self._heapify_up_down(seq, left_root, heap_orders, leo)

                heap_orders.append(right_order)
                self._heapify_up_down(seq, right_root, heap_orders, leo)

        return seq