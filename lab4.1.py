sentence = str(input(""))
palindromes = [word for word in sentence.split() if word.lower() == word.lower()[::-1]]
print(f"\nNumber of palindrome words: {len(palindromes)}")