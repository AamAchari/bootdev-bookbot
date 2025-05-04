def get_num_words(content):
	return len(content)

def get_num_characters(content):
	dict_chars = {}
	
	for c in contents:
		key = c.lower()
		if key in dict_chars.keys():
			dict_chars[key]+=1
			continue
		dict_chars[key]=0
	return dict_chars


