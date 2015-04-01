import zipfile
import shutil
import sys
import os
import xml.dom.minidom

class ebook:
    def __init__(self, ebookfile):
        self.file = ebookfile
        self.booktype = ebookfile[ebookfile.find('.'):].upper()
        self.extractdir = self.file.split('.')[0]

        if self.booktype == '.EPUB':
            os.mkdir(self.extractdir)
            try:
                with zipfile.ZipFile(self.file, 'r') as z:
                    z.extractall(self.extractdir)
            except Exception as ex:
                self.throwexception("Unexpexted Error during extraction of " + self.file, ex, "true")

        self.title = self.gettitle()
        self.author = self.getauthor()
        self.subject = self.getsubject()
        self.language = self.getlanguage()

    def gettitle(self):
        if self.booktype == '.EPUB':
            #Get the OPF File - there is everything we need for the Metadata
            opfFile = self.getfilewithextionsion(self.extractdir, ".opf")
            opf = xml.dom.minidom.parse(opfFile)
            metadata = opf.getElementsByTagName('metadata')
            for meta in metadata:
                title = meta.getElementsByTagName('dc:title')[0].firstChild.data
            return title


    def getauthor(self):
        if self.booktype == '.EPUB':
            #Get the OPF File - there is everything we need for the Metadata
            opfFile = self.getfilewithextionsion(self.extractdir, ".opf")
            opf = xml.dom.minidom.parse(opfFile)
            metadata = opf.getElementsByTagName('metadata')
            for meta in metadata:
                author = meta.getElementsByTagName('dc:creator')[0].firstChild.data
            return author

    def getsubject(self):
        if self.booktype == '.EPUB':
            #Get the OPF File - there is everything we need for the Metadata
            opfFile = self.getfilewithextionsion(self.extractdir, ".opf")
            opf = xml.dom.minidom.parse(opfFile)
            metadata = opf.getElementsByTagName('metadata')
            subjectinfo = ""
            for meta in metadata:
                for subject in meta.getElementsByTagName('dc:subject'):
                    subjectinfo = subjectinfo + subject.firstChild.data
            return subjectinfo

    def getlanguage(self):
        if self.booktype == '.EPUB':
            #Get the OPF File - there is everything we need for the Metadata
            opfFile = self.getfilewithextionsion(self.extractdir, ".opf")
            opf = xml.dom.minidom.parse(opfFile)
            metadata = opf.getElementsByTagName('metadata')
            for meta in metadata:
                language = meta.getElementsByTagName('dc:language')[0].firstChild.data
            return language

    def deletefolder(self, folder):
        if os.path.isdir(folder):
            try:
                shutil.rmtree(folder)
            except Exception as ex:
                self.throwexception("Unexpexted Error during deletion of the folder " + folder, ex, "false")

    def getfilewithextionsion(self, dir, fileextension):
        for root, dirs, files in os.walk(dir):
                for file in files:
                    if file.endswith(fileextension):
                        return os.path.join(root, file)

    def throwexception(self, raised, ex, kill):
        print
        print raised
        print type(ex)
        print ex.args
        print ex
        if kill == "true":
            sys.exit(-1)

    def __del__(self):
        self.deletefolder(self.extractdir)
