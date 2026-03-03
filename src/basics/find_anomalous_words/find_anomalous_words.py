def find_anomalous_words(text: str) -> list[str]:
    if  text == '':
        return []

    word_list = ''.join(c for c in text if c.isalpha() or c == ' ').split()
    avg_len = sum(len(s) for s in word_list) / len(word_list)
    res = []

    for w in word_list:
        print(len(w))
        if abs(len(w) - avg_len) >= 2:
            res.append(w)

    return res
