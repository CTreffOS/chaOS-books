import zipfile
import os
import shutil

#Gather all the ePubs
toAnalyze = []
dropIn = 'drop-in/'
for file in os.listdir(dropIn):
	if file.upper().endswith('.EPUB'): #making shure, we get all ePubs
		toAnalyze.append(os.path.join(dropIn,file))

#just open the first file to see whats going on
bookDir = toAnalyze[0]
print bookDir
unzipDir = bookDir.split('.epub')[0]
os.mkdir(unzipDir)
with zipfile.ZipFile(bookDir, 'r') as z:
	z.extractall(unzipDir)
#Now wie have everything we need in place - time to get some stuff done


#shutil.rmtree(unzipDir)

'''
#Stuff that works with the ebooklib

from ebooklib import epub

#Better Pipe the output to a file to gather a better overview
# ID = 2  is CSS
# ID = 9  is content
# ID = 4  is NCX
# ID = 1  is Binary Content
for bookDir in toAnalyze:
	print ' '
	book = epub.read_epub(bookDir)
	print '-- the item ids in the book ' + bookDir + ' --'
	for item in book.get_items():
		print '----------------'
		print 'ID: ' + item.get_id()
		print 'Type Number: ' + str(item.get_type())
		if item.get_type() == 2:
			print 'Type: CSS'
		elif item.get_type() == 4:
			print 'Tpye: NCX'
		elif item.get_type() == 9:
			print 'Type: Content'
		elif item.get_type() == 1:
			print 'Type: Binary Content'
#Just examine the first book in the list, otherwise the output is too long
book = epub.read_epub(toAnalyze[0])
for item in book.get_items():
	if item.get_id() != 'ncx':
		print ' '
		print '-- the ' + item.get_id() + ' item --'
		print '-- the type --'
		print item.get_type()
		print '-- the content --'
		print item.get_content()
	if item.get_id() == 'ncx':
		print '-- the ncx item --'
		htmlItem = epub.EpubHtml(item)
		print '-- the Nav item --'
		navItem = epub.EpubNav(htmlItem)
		print navItem
		print '-- the language --'
		print htmlItem.get_language()
		print '-- the content via Item --'
		print item.get_content()
		print '-- the type via nav Item --'
		print navItem.get_type()
'''
