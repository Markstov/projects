import html, cgi, sqlite3

db = sqlite3.connect('comp.db')
cur = db.cursor()

form = cgi.FieldStorage()

text = form.getfirst("Author", "")
integer = int(form.getfirst("Book", ""))

cur.execute("Insert into pc_sales (id_pc, name_customer) values (?, ?)", (integer, text))
db.commit()
redirectURL = 'http://localhost:8000/'

print ('Content-Type: text/html')
print ('Location: %s' % redirectURL)
print ()# HTTP says you have to have a blank line between headers and content
print ('<html>')
print (' <head>')
print (' <meta http-equiv="refresh" content="0;url=%s" />' % redirectURL)
print (' <title>You are going to be redirected</title>')
print (' </head>' )
print (' <body>')
print (' Redirecting... <a href="%s">Click here if you are not redirected</a>' % redirectURL)
print (' </body>')
print ('</html>')