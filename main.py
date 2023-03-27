with open('recipes.txt', encoding='utf-8') as f:
    cook_book={}
    for line in f:
        dish_name = line.strip()
        ingredient_name = int(f.readline())
        dish_ingredients = []
        for i in range(ingredient_name):
            dish_ingr = f.readline().strip()
            ingredient_name, quantity, measure = dish_ingr.split(' | ')
            dish_ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        cook_book[dish_name] = dish_ingredients

    # print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    temporary_cook_book={}
    person_count = int(person_count)
    for dish in dishes:
        for meal, ingredients in cook_book.items():
            if meal == dish:
                for ingredient in ingredients:
                    dish_ingredients = {}
                    ingr_name = ingredient['ingredient_name']
                    dish_ingredients['measure'] = ingredient['measure']
                    dish_ingredients['quantity'] = int(ingredient['quantity']) * person_count
                    if ingr_name not in temporary_cook_book:
                        temporary_cook_book[ingr_name] = dish_ingredients
                    else:
                        for product, dict in temporary_cook_book.items():
                            if product == ingr_name:
                                dict['quantity'] += dish_ingredients['quantity']


    return temporary_cook_book



res = get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Запеченный картофель'], 8)
print(res)
