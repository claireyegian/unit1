#Claire Yegian
#9/1/17
#stringAnalysis.py - reports words and characters in a sentence, finds occurences of entered words and characters

sentence = input('Enter your sentence: ')
spaces = int(sentence.count(' '))
characters = int(len(sentence))
print('Your sentence has', spaces+1, 'words and', characters, 'characters and', characters-spaces, 'letters.')
t = input('Enter a character to search for: ')
x = int(sentence.count('t'))
print('Your sentence has', x, 'of the character', t)
the = input('Enter a word to search for: ')
y = int(sentence.count('the'))
print('Your sentence has', y, 'of the word', the)
