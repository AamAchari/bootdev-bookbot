from stats import get_num_words
from stats import get_num_characters

def get_book_text(file_path):
	with open(file_path) as file:
		file_contents = file.read()
		return file_contents

def main():
	file_path = "./books/frankenstein.txt"
	file_contents = get_book_text(file_path)
	num_words = get_num_words(file_contents.split())
	print(f'{num_words} words found in the document')
	char_dict = get_num_characters(file_contents)
	for key, value in char_dict.items():
		print(f'{key}:{value}')


if __name__ == '__main__':
	main()

