from typing import List


def compress(chars: List[str]) -> int:
    i = 0
    j = 0
    count = 0
    while i < len(chars):
        while (j < len(chars)) and (chars[i] == chars[j]):
            count += 1
            j += 1
        if count > 1:
            chars[i + 1 : i + count] = list(str(count))
            i += len(str(count)) + 1
        else:
            i += 1

        count = 0
        j = i
