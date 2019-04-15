#!/usr/bin/python

'''
Write code which Encodes a string using RUN - LENGHT ENCODING AND
DECODES a string using  RUN - LENGHT DECODINGo

ex:
   "ABBCCC" will be encoded as "1A2B3C"
   "AABBBCCCC" will be encoded as "2A3B4C"
   "1D2E1F" will be decoded as "DEEF"
'''


def lengthEncode(word):
	encode_word = ""
	word_len = len(word)
	count_char = 1
	for index in range(0, word_len-1):
		if word[index] == word[index + 1]:
			count_char += 1
			continue
                else:
			encode_word += str(count_char) + word[index]
			count_char = 1
	if index == word_len and word[index-1] != word[index]:
		encode_word += "1" + word[index]
			
	return encode_word

def LenEncode(word):
	if word == None:
		return word
	index = 0
	end_word = ""
	while index < len(word):
		cur_index = index
		cur_char= word[index]
		count = 0
		while cur_index < len(word) and cur_char == word[index]:
			cur_index += 1
			index += 1
			count += 1
		end_word += str(count) + cur_char
	return end_word
	

def lengthDecode(word):
	decode_word = ""
	for index in range(0, len(word) -1):
		if word[index].isdigit():
			decode_word += word[index + 1] * int(word[index])
	return decode_word

def LenDecode(word):
	if word is None:
		return
	index = 0
	decode_word = ""
	while index < len(word):
		digit_ch = word[index]
		num = 0
		if digit_ch.isdigit():
			if num == 0:
				num += int(digit_ch)
			else:
				num *= 10
				num += int(digit_ch)
			index += 1
			digit_ch = word[index]
		else:
			decode_word += word[index] * int(num)		
	return decode_word


if __name__ == '__main__':
	user_word = raw_input("enter a word to lenght encode:")
	print("user enter word: " + user_word)
	en_word = lengthEncode(user_word)
	print("encodeded word: " + en_word)
	print("decoded word: " + lengthDecode(en_word))
			
	en_word = LenEncode(user_word)
	print("LenEncode: " + en_word)
	print("decoded word: " + lengthDecode(en_word))
		
