class MyIterator:
    """
    Example
    >>> from my_iterator import MyIterator
    >>> list = [0, 1, 2, 3]
    >>> it = MyIterator(list)
    >>> next(it)
    0
    >>> next(it)
    1
    >>> next(it)
    2
    >>> next(it)
    3
    >>> next(it)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/workspaces/learn_python/python_tutorial/iterator_generator.py", line 11, in __next__
        raise StopIteration
    StopIteration
    """
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        ret = self.index
        self.index += 1
        return ret