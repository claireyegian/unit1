#Claire Yegian
#9/1/17
#stringAnalysis.py - reports words and characters in a sentence, finds occurences of entered words and characters

sentence = input('Enter your sentence: ')
spaces = int(sentence.count( ))
characters = int(len(sentence))
print('Your sentence has', spaces+1, 'words and', characters, 'characters and', characters-spaces, 'letters.')
