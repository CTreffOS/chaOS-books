import zipfile
import os
import shutil
import xml.dom.minidom

#Gather all the ePubs
toAnalyze = []
dropIn = 'drop-in/'
for file in os.listdir(dropIn):
	if file.upper().endswith('.EPUB'): #making shure, we get all ePubs
		toAnalyze.append(os.path.join(dropIn,file))

#just open the first file to see whats going on
bookDir = toAnalyze[0]
unzipDir = bookDir.split('.epub')[0]
os.mkdir(unzipDir)
with zipfile.ZipFile(bookDir, 'r') as z:
	z.extractall(unzipDir)

#Now wie have everything we need in place - time to get some stuff done
epubStruct = []
for root, dirs, files in os.walk(unzipDir, topdown=False):
	for name in files:
		epubStruct.append(os.path.join(root, name))
		for name in dirs:
			epubStruct.append(os.path.join(root, name))
cssFiles = []
opfFiles = []
xmlFiles = []
htmlFiles = []
ncxFiles = []
xhtmlFiles = []
bookVersion = '2.0'
for file in epubStruct:
	if file.endswith('.css'):
		cssFiles.append(file)
	elif file.endswith('.opf'):
		opfFiles.append(file)
	elif file.endswith('.xml'):
		xmlFiles.append(file)
	elif file.endswith('.html'):
		htmlFiles.append(file)
	elif file.endswith('.ncx'):
		ncxFiles.append(file)
	elif file.endswith('.xhtml'):
		#an xhtml file only existis in v3
		xhtmlFiles.append(file)
		bookVersion = '3.0'

'''
print '-- cssFiles --'
print cssFiles
print '-- opfFiles --'
print opfFiles
print '-- xmlFiles --'
print xmlFiles
print '-- htmlFiles --'
print htmlFiles
print '-- ncxFiles --'
print ncxFiles
print '-- xhtmlFiles --'
print xhtmlFiles
'''

#First we need some Infos about the book
if bookVersion == '2.0':
	if len(opfFiles) == 1:
		opf = xml.dom.minidom.parse(opfFiles[0])
	elif len(opfFiles) < 1:
		#ToDo
		print 'error'
	elif len(opfFiles) > 1:
		#ToDo
		print 'error'

	if len(xmlFiles) == 1:
		xml = xml.dom.minidom.parse(xmlFiles[0])
	elif len(xmlFiles) < 1:
		#ToDo
		print 'error'
	elif len(xmlFiles) > 1:
		#ToDo
		print 'error'
elif bookVersion == '3.0':
	if len(xhtmlFiles) == 1:
		xhtml = xml.dom.minidom.parse(xhtmlFiles[0])
	elif len(xhtmlFiles) < 1:
		#ToDo
		print 'error'
	elif len(xhtmlFiles) > 1:
		#ToDo
		print 'error'
shutil.rmtree(unzipDir)
