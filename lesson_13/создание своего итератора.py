class SimpleIterator:
    def __iter__(self):
        return self

    def __init__(self, limit: int = 5) -> None:
        self.limit = limit
        self._counter = 0

    def __next__(self) -> int:
        if self._counter < self.limit:
            self._counter += 1
            return 1
        else:
            raise StopIteration

custom_iterator = SimpleIterator()
print(next(custom_iterator))
print(next(custom_iterator))
print(next(custom_iterator))
print(next(custom_iterator))
print(next(custom_iterator))

print()

new_custom_iterator = SimpleIterator()
print(next(new_custom_iterator))
print(next(new_custom_iterator))
print(next(new_custom_iterator))
print(next(new_custom_iterator))
print(next(new_custom_iterator))

for element in new_custom_iterator:
    print(element)