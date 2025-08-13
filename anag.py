def are_anagrams_dict(str1, str2):
    from collections import Counter
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    return Counter(str1) == Counter(str2)

print(are_anagrams_dict("liten", "silent"))