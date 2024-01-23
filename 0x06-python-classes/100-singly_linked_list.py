#!/usr/bin/python3
"""
This module contains the definition of the classes Node and
SinglyLinkedList.
"""


class Node:
    """This class defines a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """initializes a Node instance object with the
        data and the next_node attribute values.

        Args:
            data (int): the value stored at the node.
            next_node (Node object): the next node a node points to in
            a singly linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This is the getter method for the data private attribute."""
        return self.__data

    @property
    def next_node(self):
        """This is the getter method for the next_node private attribute."""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Setter method for data attribute after checks it's an integer
        Args:
            value (int): the value that the data attribute will be set to.
        """
        if value:
            if (type(value) is int):
                self.__data = value
            else:
                raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        """Setter method for next_node attribute after checks it's of type Node
        Args:
            value (Node object): the Node that the next_node attribute will be
            set to.
        """
        if value:
            if (type(value) is Node):
                self.__next_node = value
            else:
                raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = None


class SinglyLinkedList:
    """This class defines a singly linked list"""
    def __init__(self):
        """Initializes the SinglyLinkedList object"""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a node into the correct sorted position in the list
        Args:
            value (int): the value to be in the newly added node
        """
        currentnode = self.head
        newnode = Node(value, None)
        if currentnode is None:
            self.head = newnode
        else:
            while (currentnode.next_node):
                currentnode = currentnode.next_node
            currentnode.next_node = newnode

    def __str__(self):
        """prints the entire list in stdout one node number by line"""
        currentnode = self.head
        result = []
        while (currentnode):
            result.append(str(currentnode.data))
            currentnode = currentnode.next_node
        result = sorted(result, key=lambda x: int(x))
        sep = "\n"
        result = sep.join(result)
        return result
