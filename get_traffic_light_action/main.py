first_color = "green"
second_color = "yellow"
third_color = "red"

color_of_traffic_light = input('Цвет светофора: ')

if color_of_traffic_light.lower() == first_color.lower():
    print('Go')
elif color_of_traffic_light.lower() == second_color.lower():
    print('Slow down')
elif color_of_traffic_light.lower() == third_color.lower():
    print('Stop')
else:
    print('unknown')
