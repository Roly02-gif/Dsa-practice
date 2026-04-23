# Solution 1
def reverseWords(s: str) -> str:
    wordList = s.split()
    result = ""
    for i in range(len(wordList) - 1, 0, -1):
        cur_word = wordList[i]
        result += cur_word + " "
    result += wordList[0]
    return result


# Solution 2
def reverseWords(s: str) -> str:
    reversedWordList = s.split()[::-1]
    result = " ".join(reversedWordList)
    return result
