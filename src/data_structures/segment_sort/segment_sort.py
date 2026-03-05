def sort_segments(segments: list[tuple[int, int]]) -> list[tuple[int, int]]:
    len_dict = {}
    for i in segments:
        length = str(float(i[1] - i[0]))

        if length not in len_dict:
            len_dict[length] = []

        len_dict[length].append(i)
    print(len_dict)
    len_arr = sorted([ float(x) for x in len_dict.keys()])[::-1]
    res = []
    for i in len_arr:
        for j in len_dict[str(i)]:
            res.append(j)


    return res


# альтернативный простой вариант
def sort_segments_simple(segments: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return sorted(segments, key=lambda x: x[1] - x[0])[::-1]


print(sort_segments([(1, 5), (2, 3), (10, 20)]))

