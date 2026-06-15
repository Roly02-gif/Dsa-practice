def closeStrings(word1: str, word2: str) -> bool:
    w_occ1 = {}
    w_occ2 = {}
    for w in word1:
        w_occ1.setdefault(w, None)
        w_occ1[w] = 1 if w_occ1[w] is None else w_occ1[w]+1
    for w in word2:
        w_occ2.setdefault(w, None)
        w_occ2[w] = 1 if w_occ2[w] is None else w_occ2[w]+1

    occ1 = list(w_occ1.values())
    occ2 = list(w_occ2.values())
    occ1.sort()
    occ2.sort()
    return occ1 == occ2 and set(w_occ1.keys()) == set(w_occ2.keys())