import requests
import json
from datetime import datetime

class TaskTimer:
	def __enter__(self):
		self.t_start = datetime.now()
		return self
	def __exit__(self, *args):
		self.t_end = datetime.now()
		self.t_diff = self.t_end - self.t_start
		return self.t_diff

def search_book_openlibrary_org(book):
	url_base = 'http://openlibrary.org/search.json?q='
	book_to_find = book.replace(' ', '+')
	print('Ищем:', book_to_find)
	full_url = url_base + book_to_find
	response = requests.get(full_url)
	content_txt = response.json()['docs']
	return content_txt

def printing(content_txt):
	for book in content_txt:
		print('------    book begin    -----')
		print('Title        : ', book['title'])
		if 'author_name' in book.keys():
			print('Author       : ', book['author_name'])
		else:
			print('Author       : ', 'none')
		if 'isdn' in book.keys():
			print('ISDN         :',book['isdn'])
		else:
			print('ISDN         :','none')
		print('Has fulltext : ', book['has_fulltext'])
		print('Seed         : ', book['seed'])
		print('Key          : ', book['key'])
		print('------    book end      -----')

def main_routine():
	repeat = True
	while repeat == True:
		inp = input('Введите действие: q - выход; s - поиск книги и печать, f - поиск книги без вывода:')
		if inp == 'q':
			repeat = False
		elif inp == 's':
			inp_book = input('    Введите книгу или автора на английском языке:')
			with TaskTimer() as t:
				text_to_print = search_book_openlibrary_org(inp_book)
				printing(text_to_print)
			print('=============конец поиска==========')
			print('Request time:', t.t_diff)
			print('=============конец ================')
		elif inp == 'f':
			inp_book = input('    Введите книгу или автора на английском языке:')
			with TaskTimer() as t:
				text_to_print = search_book_openlibrary_org(inp_book)
			print('=============конец поиска==========')
			print('Request time:', t.t_diff)
			print('=============конец ================')
		else:
			print('Неверный ввод, повторите.')

main_routine()


