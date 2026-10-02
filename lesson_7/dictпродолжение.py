brands = (('Audi', 5), ('BMW', 5), ('Porshe', 3))

my_brand_dict = {brand.lower(): rate for brand, rate in brands if rate >= 5}

print(my_brand_dict)



my_list = [1,2,3,4,5,3,2,1,3,1]

my_set = {i for i in my_list}
print(my_set)