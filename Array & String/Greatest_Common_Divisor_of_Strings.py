# First idea
def gcdOfStrings(str1: str, str2: str) -> str:
    x = ""
    temp_x = ""
    for i in range(min(len(str1), len(str2))):
        if str1[i] == str2[i]:
            x += str1[i]
            if str1 == x * (len(str1) // len(x)) and str2 == x * (len(str2) // len(x)):
                temp_x = x
        else:
            return ""
    if str1 == x * (len(str1) // len(x)) and str2 == x * (len(str2) // len(x)):
        return x
    else:
        return temp_x


# Second idea
from math import gcd


def gcdOfStrings(str1: str, str2: str) -> str:
    if str1 + str2 != str2 + str1:
        return ""
    else:
        return str1[: gcd(len(str1), len(str2))]
