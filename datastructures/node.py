class Node:
    left = None
    right = None
    previous = None
    next = None


    def __init__(self, data):
        self._data = data


    def __eq__(self, other):
        if self._data == other:
            return True
        else:
            return False


    def __gt__(self, other):
        if self._data > other:
            return True
        else:
            return False


    def __ge__(self, other):
        if self._data >= other:
            return True
        else:
            return False


    def __lt__(self, other):
        if self._data < other:
            return True
        else:
            return False


    def __le__(self, other):
        if self._data >= other:
            return True
        else:
            return False
