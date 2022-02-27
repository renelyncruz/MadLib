#dictionary to remind user of specific definitions
dictionary = [
  {
    "Nouns": "Nouns are words that represent people, places, or things.",
    "Adjectives": "Adjectives are words that describe people, places, or things.",
    "Verbs": "Verbs are words that show an action(sing), occurence (develop), or state of being (exist).",
    "Adverbs": "Adverbs are words that desribe verbs, usually ending in '-ly'. The also tell when, where, how often, and how much a verb is done."
  }]

print("Hello! Welcome to my MadLib program. Before we start, let's remember the definitions for nouns, adjectives, verbs, and adverbs.\n") 
#print statements calling each key
print(dictionary["Nouns"])
print(dictionary["Adjectives"])
print(dictionary["Verbs"])
print(dictionary["Adverbs"])
print("\nAll righty then! Now that we understand those words, let's make a story together! You'll need to provide me with some information below.\n")
#list to inquire for words from user
story_parts = [
  "1st adjective ",
  "1st noun ",
  "adverb, ending in -ly ",
  "2nd adjective ",
  "3rd adjective ",
  "your favorite food ",
  "4th adjective ",
  "2nd noun ",
  "1st verb, ending in -ed ",
  "3rd noun ",
  "2nd verb, ending in -ed ",
  "5th adjective "
]
#dictionary to hold the users words
bucket_for_story_parts = {}
#loop that fills story parts list
for part in story_parts:
  #asks the user for different word types
  word = input(f"Please enter {part}:")
  #places each chosen word inside the dictionary. It turns each word type into a key, while the user's word choice is that key's value.
  bucket_for_story_parts[part] = word

print(bucket_for_story_parts)