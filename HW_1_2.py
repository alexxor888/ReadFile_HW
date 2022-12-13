from pprint import pprint

cook_book = {}
with open ('count.txt') as f:
    for  line in f:
        food = line.strip()
        count = int(f.readline())
        ingrs=[]

        for i in range (count):
            ingr = f.readline().strip()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingrs.append({"ingredient_name":ingredient_name,
                       "quantity":quantity,
                       "measure":measure
                       })
        f.readline()
        dishes,ingredients = [],[]
        ingredients.append(ingrs)
        dishes.append(food)
        cook_book = cook_book | dict(zip(dishes,ingredients))
        line.strip()
    print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] = int(new_shop_list_item['quantity']) * person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))