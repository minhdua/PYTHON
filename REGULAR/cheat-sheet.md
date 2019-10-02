# metacharacters

- \ :
- [] : Represent a character class
- ^ : Matches the beginning
- $ : Mathches the end
- . : Mathches any character except newline
- ? : Matches zero or one occurence
- | : Means OR (Matches with any of the characters separated by it.
- * : Any number of occurrences (including 0 occurrences)
- + : One ore more occurrences
- {} : Indicate number of occurrences of a preceding RE to match.
- () : Enclose a group of REs

# Function compile()
- module re
- return object Regular Expression
- findall searches for the Regular Expression and return a list upon finding 
# Metacharacter blackslash
- \d:  Matches any decimal digit, this is equivalent to the set class [0-9].
- \D   Matches any non-digit character.
- \s   Matches any whitespace character.
- \S   Matches any non-whitespace character
- \w   Matches any alphanumeric character, this is equivalent to the class [a-zA-Z0-9_].
- \W   Matches any non-alphanumeric character.
# Function split()
- re.split(pattern, string, maxsplit=0, flags=0)
- flags = re.IGNORECASE
# Function sub()
- re.sub(pattern, repl, string, count=0, flags=0)
- r\s..\s
# Function subn()
- re.subn(pattern, repl, string, count=0, flags=0)
# Searching a occurrence of pattnern
- re.search()
- re.match()
- re.findall()
# check anagram
- use function sorted
# sample Regulars
- URL : "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
# Longest Common Substring
- difflib.SequenceMatcher
- find_longest_match(begin1,end1,begin2,end2)
newChars = map(lambda x: x if (x!=c1 and x!=c2) else c1 if (x==c2) else c2,input)


