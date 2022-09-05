# Write a function in Python to check duplicate letters. 
# It must accept a string, i.e., a sentence.
# The function should return True if the sentence has any word with duplicate letters, else return False. 

def duplicate(sentence):
	word_list = sentence.split(' ')

	for word in word_list:
		print(word)
		for letter in word:
			count = word.count(letter)
			print(count)
			if count > 1:
				truth_value = True
				break
			else:
				truth_value = False


	return truth_value			

sentence = input("Enter a sentence: ")

print(duplicate(sentence))
