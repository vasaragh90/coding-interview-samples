#!/usr/bin/env python3

def commonCharacters(strings):
    # Write your code here.
      characterCounts = {}
      for string in strings:
          print(string)
          uniqueStringCharacters = set(string)
          print (uniqueStringCharacters)
          for character in uniqueStringCharacters:
           if character not in characterCounts:
               characterCounts[character] = 0
           characterCounts[character] += 1
      finalStringCharacters = []
      for character,count in characterCounts.items():
          if count == len(strings):
           finalStringCharacters.append(character)
      print (characterCounts.items())
      print (finalStringCharacters)
      return finalStringCharacters
      
def main():
  strings = ["abc","bcd","cbaccd"]
  print(strings)
  finalStringCharacters = commonCharacters(strings)
  print (finalStringCharacters)

if __name__ == "__main__":
    main()

