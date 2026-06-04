def maxVowels(s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        n = len(s)
        max_vowels = 0
        for i in range(k):
            max_vowels += 1 if s[i] in vowels else 0
            temp_max_vowels = max_vowels
        for i in range(n-k):
            temp_max_vowels = temp_max_vowels+1 if s[i+k] in vowels else temp_max_vowels
            temp_max_vowels = temp_max_vowels-1 if s[i] in vowels else temp_max_vowels
            max_vowels = max(temp_max_vowels, max_vowels)
        return max_vowels