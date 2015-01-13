import zipfile
import os
import shutil
import xml.dom.minidom
from glob import glob

#Gather all the ePubs
dropIn = 'drop-in/'
toAnalyze = glob( os.path.join( dropIn, "*.epub") )

for bookDir in toAnalyze:
	unzipDir = bookDir.split('.epub')[0]
	
	os.mkdir(unzipDir)
	with zipfile.ZipFile(bookDir, 'r') as z:
		z.extractall(unzipDir)

	#Now we have everything we need in place - time to get some stuff done
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

	#print '-- cssFiles --'
	#print cssFiles
	print '-- opfFiles --'
	print opfFiles
	#print '-- xmlFiles --'
	#print xmlFiles
	#print '-- htmlFiles --'
	#print htmlFiles
	#print '-- ncxFiles --'
	#print ncxFiles
	#print '-- xhtmlFiles --'
	#print xhtmlFiles

	#We going to parse the stuff we need
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
	#For the basic Metadata the opf file should be interesting
	metadata = opf.getElementsByTagName('metadata')
	for meta in metadata:
		author = meta.getElementsByTagName('dc:creator')[0].firstChild.data
		print 'Author: ' + author
		title = meta.getElementsByTagName('dc:title')[0].firstChild.data
		print 'Title: ' + title
		language = meta.getElementsByTagName('dc:language')[0].firstChild.data
		print 'Language: ' + language
		subject = meta.getElementsByTagName('dc:subject')[0].firstChild.data
		print 'Subject: ' + subject
	shutil.rmtree(unzipDir)
