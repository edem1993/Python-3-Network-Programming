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

	"""for d in db_list:
		for i in items:
			if d == i:
				print(d)
			else:
				pass
 
	print("****************\n")"""
	
	"""compares the unique values..
	matches = set(items).intersection(db_list)
	print(matches)
	return list(matches)"""
	
	new_list = []
	for element in db_list:
		if element in items:
			new_list.append(element)
	
	return new_list
	
compare_db(o, db)

print(compare_db(o, db))
