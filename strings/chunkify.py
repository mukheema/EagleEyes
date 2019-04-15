#!/usr/bin/python


def GetChunkList(document, chunkDelimiter=";", chunkSize=5):
	if document is None:
		return []
	
	doc_list = list()
	word = ""
	for ch in document:
		word += ch
		if len(word) > chunkSize:
			doc_list.append(word)
		if ch == ":":
			word = ""

		
#	doc_list = document.split(chunkDelimiter)
#	for element in doc_list:
	return doc_list


if __name__ == '__main__':
	user_doc = raw_input("enter document : ")
	doc_list = GetChunkList(user_doc)	
	print("doc_list" + str(doc_list))
