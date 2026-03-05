def find_most_expensive_weapons(inventory: dict[str, int], blueprints: dict[str, dict]) -> list[str]:
    res = []
    max_price = 0
    for blueprint in blueprints.items():

        blueprint_name = blueprint[0]
        blueprint_materials = blueprint[1]["materials"]
        blueprint_price = blueprint[1]["price"]
        stop = False

        for material in blueprint_materials:
            if material not in inventory or inventory[material] < blueprint_materials[material]:
                stop = True
        if stop:
            continue

        if max_price == blueprint_price:
            res.append(blueprint_name)
        if max_price < blueprint_price:
            res = [blueprint_name]
            max_price = blueprint_price


    return res



