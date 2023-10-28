class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        n = len(s)//2
        a = s[:n]
        b = s[n:]
        vowel_count_a = 0
        vowel_count_b = 0
        for i in range(n):
            if a[i].lower() in vowels:
                vowel_count_a += 1
            if b[i].lower() in vowels:
                vowel_count_b += 1
        
        if vowel_count_a == vowel_count_b:
            return True
        else:
            return False