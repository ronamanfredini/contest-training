class Solution:
  def reverseVowels(self, s: str) -> str:
    found_vowels = []
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    new_str = ''
    for letter in s:
      if letter.lower() in vowels:
        found_vowels.append(letter)
    
    for letter in s:
      if not letter.lower() in vowels:
        new_str += letter
      else:
        new_str += found_vowels.pop()

    return new_str
  
