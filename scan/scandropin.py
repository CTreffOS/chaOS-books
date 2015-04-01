import ebook
from glob import glob
import os

def main():
    # Scans the drop-in Folder for files and calls the according functions
    dropinfolder = "drop-in"
    # gather all files from the folder
    toanalyze = glob( os.path.join( dropinfolder, "*") )
    for bookfile in toanalyze:
        book = ebook.ebook(bookfile)
        print ''
        print '##################'
        print ''
        print 'File:     ' + u"{0}".format(book.file)
        print 'Author:   ' + u"{0}".format(book.author)
        print 'Language: ' + u"{0}".format(book.language)
        print 'Subject:  ' + u"{0}".format(book.subject)
        print 'Title:    ' + u"{0}".format(book.title)
        del book
if __name__ == '__main__':
    main()