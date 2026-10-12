from dataclasses import dataclass, field


@dataclass
class Bill:
    costs_by_dish: list = field(default_factory=list)

bill1 = Bill()
print(bill1.costs_by_dish)
bill1.costs_by_dish.append(1)

bill2 = Bill()
bill2.costs_by_dish.append(2)
print(bill1.costs_by_dish)
print(bill2.costs_by_dish)