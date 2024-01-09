from pprint import pprint
def cook_book():
    cook_book = {}
    with open('recipes.txt') as f:   # для того чтобы узнать количество итераций в цикле по документу(рецептов)
        s = f.readlines()
        s = ''.join(s).split('\n\n')
    with open('recipes.txt', encoding='utf-8') as f:
        for line in range(len(s)):
            title = f.readline().strip()
            cook_book[title] = []
            count = f.readline().strip()
            for line in range(int(count)):
                ingridient = f.readline().strip().split(' | ')
                ingridients = {'ingredient_name': ingridient[0], 'quantity': ingridient[1], 'measure': ingridient[2]}
                cook_book[title].append(ingridients)
            f.readline().strip()
    return cook_book

#print(cook_book())

def get_shop_list_by_dishes(dishes, person_count):
    cook_book_ = cook_book()
    need_goods = {}
    for dish in dishes:
        for key, value in cook_book_.items():
           if key == dish:
               for i in value:
                   if i['ingredient_name'] not in need_goods:
                       need_goods[i['ingredient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
                   else:
                       need_goods[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count

    return need_goods

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
