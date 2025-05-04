def get_num_words(content):
	return len(content)

def get_num_characters(content):
	dict_chars = {}	
	for c in content:
		key = c.lower()
		if key in dict_chars.keys():
			dict_chars[key]+=1
			continue
		dict_chars[key]=1
	return dict_chars
def get_sorted_dict(character_dictionary):
	sorted_keys = sorted(list(character_dictionary.keys()), key=lambda key:character_dictionary[key],reverse=True)
	res = list(map(lambda key: {"char": key, "num": character_dictionary[key]}, sorted_keys))
	return res