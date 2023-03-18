from pprint import pprint

def extract_file():
    with open('recipes.txt', 'rt', encoding='utf-8') as file:
        recipes = {}
        for line in file:
            name_of_the_dish = line.strip()
            num_of_serv = int(file.readline())
            layot = []
            for _ in range(num_of_serv):
                name, quantity, pieces = file.readline().strip().split(' | ')
                layot.append({
                    "name": name,
                    "quantity": quantity,
                    "pieces": pieces
                })
            file.readline()
            recipes[name_of_the_dish] = layot
        pprint(recipes, sort_dicts=False)
        return recipes


def get_shop_list_by_dishes(dishes, person_count):
    recipes = extract_file()
    result = {}
    for recipe, ingredients in recipes.items():
        if recipe in dishes:
            for ingredient in ingredients:
                name = ingredient["name"]
                quantity = int(ingredient["quantity"]) * person_count
                pieces = ingredient["pieces"]
                if name not in result.keys():
                    result[name] = {
                        "pieces": pieces,
                        "quantity": quantity
                    }
                else:
                    result[name]["quantity"] += quantity
    return result

pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))




