import ebook
from glob import glob
import os
import psycopg2

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

        # The Following Lines are just experiments with PostgreSQL
        conn = psycopg2.connect("dbname=ebook user=postgres")
        cur = conn.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public' AND table_type='BASE TABLE' AND table_name = 'book';")
        if cur.fetchone()[0] != 'book':
            cur.execute("CREATE TABLE book (id serial PRIMARY KEY, author varchar, language varchar, subject varchar, title varchar, image bytea);")
        if u"{0}".format(book.author) != 'None':
            SQL = "SELECT COUNT(*) FROM book WHERE author = %s AND language = %s AND subject = %s AND title = %s AND image = %s"
            data = (u"{0}".format(book.author), u"{0}".format(book.language), u"{0}".format(book.subject), u"{0}".format(book.title), u"{0}".format(book.cover),)
            cur.execute(SQL, data)
            if int(cur.fetchone()[0]) == 0:
                SQL = "INSERT INTO book (author, language, subject, title, image) VALUES (%s, %s, %s, %s, %s)"
                data = (u"{0}".format(book.author), u"{0}".format(book.language), u"{0}".format(book.subject), u"{0}".format(book.title), u"{0}".format(book.cover),)
                cur.execute(SQL,data)
                conn.commit()
        cur.close()
        conn.close()

        del book

if __name__ == '__main__':
    main()