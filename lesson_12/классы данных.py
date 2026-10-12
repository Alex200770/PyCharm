class ITEmployee:
    dept = 'IT'

    def __init__(self, name, id: int):
        self.name = name
        self.id = id
    def __eq__(self, other: ITEmployee):
        if self.name == other.name:
            return True
        return False

    def __lt__(self, other: ITEmployee):
        return True if self.id < other.id else False

it1 = ITEmployee('Jake2', 19)
it2 = ITEmployee('Jake2', 12)

print(it1 < it2)
print(it1 == it2) #по равенству а is по айдишнику



from dataclasses import dataclass


@dataclass    #(order=True) для < > =
class ITEmployee:
    name: str
    id: int
    dept: str = 'IT'

it1 = ITEmployee('Jake', 138)
it2 = ITEmployee('Jake', 138)

print(it1 == it2)