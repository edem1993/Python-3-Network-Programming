import sys

testf = 'C:\\Users\\adenes\\Desktop\\test.txt'
db = 'C:\\Users\\adenes\\Desktop\\db.txt'

def open_file(file):
	file = open(testf, 'r')
	file.seek(0)
	f = file.readlines() # list of file entries
	
	return f
	#print(f)
	
o = open_file(testf)

def compare_db(items, dblist):
	""" returns the complementer of db and the file"""
	dbfile = open(db, 'r')
	dbfile.seek(0)
	db_list = dbfile.readlines() # list of db entries

	new_list = []
	for element in items:
		#print(element.rstrip('\n'))
		if element in db_list:
			new_list.append(element)
			
	result = [x.split('\t') for x in new_list]
	return result
	 
print(compare_db(o, db))
x = compare_db(o, db)

def replace_list_iterations(list_elements):
	
	if list_elements != False:
		for list_elem in list_elements:
			#print(list_elem)
			for entry in list_elem:
				entry = entry.split()
				
				entry = input('enter alias IN rtype addr : ')
				
				print('\n' + entry + '\n')
				return entry
			
			
replace_list_iterations(x)
