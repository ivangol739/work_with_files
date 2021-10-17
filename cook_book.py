from pprint import pprint

with open('recipes.txt', 'r', encoding='utf-8') as f:
    cook_book = {}
    for dish in f:
        dish_name = dish.strip()
        count = int(f.readline().strip())
        list_ingredients = []
        for count_ingredients in range(count):
            ingredient_name, quantity, measure = f.readline().split('|')
            products = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure}
            list_ingredients.append(products)
        cook_book[dish_name] = list_ingredients
        f.readline()

def get_shop_list_by_dishes(dishes, person_count):
    menu = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in menu:
                    menu[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity'] * person_count)
                else:
                    menu[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity'] * person_count)}
    return pprint(menu)

get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)


