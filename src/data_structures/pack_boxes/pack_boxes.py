def pack_boxes(items: list[int], limit: int) -> list[list[int]]:
    items = [x for x in items if x <= limit]
    res = []
    counter = 0
    sub_items = []

    if len(items) == 0:
        return []

    for i in range(len(items)):

        if counter + items[i] <= limit:
            counter += items[i]
            sub_items.append(items[i])
        else:
            res.append(sub_items)
            sub_items = [items[i]]
            counter = items[i]
    res.append(sub_items)
    return res


