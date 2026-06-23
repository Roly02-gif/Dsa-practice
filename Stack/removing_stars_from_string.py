def removeStars(s: str) -> str:
    res = []
    for elt in s:
        if elt == '*':
            res.pop()
        else:
            res.append(elt)
    return "".join(res)
            