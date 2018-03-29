import sqlite3

conn = sqlite3.connect('allitebooks.db')
conn.row_factory = sqlite3.Row
c = conn.cursor()
ebooks = c.execute('select * from allitebooks_ebookinfo').fetchall()

total_size = 0.0
file = open('links_download.txt', 'w')

for ebook in ebooks:
	link = ebook['ebook_linkdownload'].strip()
	if link != '': 
		file.write(link)
		file.write('\n')
	try:
		size = float((ebook['ebook_filesize'].replace(',','.').strip()))
	except:
		size = 0.0
	total_size += size
file.close()
print(total_size)