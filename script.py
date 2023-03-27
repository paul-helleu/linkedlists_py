class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class LinkedList:
    def __init__(self, value=None):
        self.head_node = Node(value)

    def get_head_node(self):
        return self.head_node

    def insert_beginning(self, new_value):
        new_node = Node(new_value, self.head_node)
        self.head_node = new_node

    def stringify_list(self):
        string_list = ""
        current_node = self.head_node

        while current_node is not None:
            string_list += str(current_node.get_value()) + "\n"

            next_node = current_node.get_next_node()
            current_node = next_node

        return string_list

    def remove_node(self, value_to_remove):
        current_node = self.head_node

        if current_node.get_value() == value_to_remove:
            self.head_node = current_node.get_next_node()
        else:
            while current_node is not None:
                next_node = current_node.get_next_node()

                if next_node is None:
                    break

                if next_node.get_value() == value_to_remove:
                    current_node.set_next_node(next_node.get_next_node())
                    break

                next_node = current_node.get_next_node()
                current_node = next_node

    def remove_nodes(self, value_to_remove):
        current_node = self.head_node

        while current_node is not None:
            if current_node == self.head_node and current_node.get_value() == value_to_remove:
                self.head_node = self.head_node.get_next_node()
                continue

            next_node = current_node.get_next_node()
            if next_node == None:
                break

            if next_node.get_value() == value_to_remove:
                current_node.set_next_node(next_node.get_next_node())

            current_node = current_node.get_next_node()

    def swap_nodes_values(self, value1, value2):
        # No change if value not found
        if value1 == value2:
            return

        node1 = None
        node2 = None

        current_node = self.head_node

        if current_node.get_value() == value1:
            node1 = current_node
        else:
            while True:
                next_node = current_node.get_next_node()
                if next_node is None:
                    break

                if next_node.get_value() == value1:
                    node1 = next_node
                    break

                current_node = next_node

        current_node = self.head_node

        if current_node.get_value() == value2:
            node2 = current_node
        else:
            while True:
                next_node = current_node.get_next_node()
                if next_node is None:
                    break

                if next_node.get_value() == value2:
                    node2 = next_node
                    break

                current_node = next_node

        if node1 is not None and node2 is not None:
            node1_value = node1.get_value()

            node1.value = node2.get_value()
            node2.value = node1_value
