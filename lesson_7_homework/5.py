#import this

from functools import reduce

rooms = [{'name': 'Kitchen', 'length': 6, 'width': 4},
        {'name': 'Room 1', 'length': 5.5, 'width': 4.5},
        {'name': 'Room 2', 'length': 5, 'width': 4},
        {'name': 'Room 3', 'length': 7, 'width': 6.3}
]

areas = map(lambda room: room['length'] * room['width'], rooms)
total_area = reduce(lambda acc, area: acc + area, areas)

print(total_area)









