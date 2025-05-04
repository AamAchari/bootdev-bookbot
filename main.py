from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted_dict

def get_book_text(file_path):
	with open(file_path) as file:
		file_contents = file.read()
		return file_contents

def main():
	file_path = "./books/frankenstein.txt"
	file_contents = get_book_text(file_path)
	num_words = get_num_words(file_contents.split())
	char_dict = get_num_characters(file_contents)
	for key, value in char_dict.items():
		print(f"'{key}': {value}")
	sorted_list = get_sorted_dict(char_dict)
	print("============ BOOKBOT ============")
	print("Analyzing book found at books/frankenstein.txt...")
	print("----------- Word Count ----------")
	print(f'Found {num_words} total words ')
	for l in sorted_list:
		key, value = l.items()
		if not key[1].isalpha():
			continue
		print(f'{key[1]}: {value[1]}')

if __name__ == '__main__':
	main()

