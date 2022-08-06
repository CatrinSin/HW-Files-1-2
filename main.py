from pprint import pprint

with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        recipie_name = line.strip()
        next_line = file.readline().strip()
        quantity = int(next_line)
        ingr_list = []
        for i in range(quantity):
            ingredients = {}
            ingr_str = file.readline().strip()
            split_ingr = ingr_str.split(' | ')
            name_of_ingr, quant_of_ingr, meas_of_ingr = split_ingr
            ingredients['ingredient_name'] = name_of_ingr
            ingredients['quantity'] = quant_of_ingr
            ingredients['measure'] = meas_of_ingr
            ingr_list.append(ingredients)
        cook_book[recipie_name] = ingr_list
        file.readline()
    # pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    final_dict = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            name_of_ingr = ingredient.pop('ingredient_name')
            ingredient['quantity'] = int(ingredient['quantity']) * int(person_count)
            if name_of_ingr in final_dict:
                ingredient['quantity'] += final_dict[name_of_ingr]['quantity']
            final_dict.update({name_of_ingr : ingredient})
    # pprint(final_dict)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет', 'Фахитос'], 2)
