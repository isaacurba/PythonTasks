def count_vowel(words):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_found = []
    for word in words:
        if word in vowels and word not in vowels_found:
            vowels_found.append(word)
            count+=1
    return print(count)


count_vowel("pineapple")
