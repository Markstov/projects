from xml.dom import minidom
import sqlite3

doc = minidom.Document()

db = sqlite3.connect("comp.db")
cur = db.cursor()

#Загрузка в XML
catalog = doc.createElement('catalog')

for row in cur.execute("select * from pc"):
    newex = doc.createElement('Computer')
    newex.setAttribute('id', str(row[0]))  # Вместо прямого задания, можно достать из базы

    name = doc.createElement('name')
    text = doc.createTextNode(row[1])  
    name.appendChild(text)
    newex.appendChild(name)

    model = doc.createElement('model')
    text = doc.createTextNode(str(row[2]))
    model.appendChild(text)
    newex.appendChild(model)

    price = doc.createElement('price')
    text = doc.createTextNode(str(row[3]))
    price.appendChild(text)
    newex.appendChild(price)

    catalog.appendChild(newex)

doc.appendChild(catalog)

xml_str = doc.toprettyxml()
with open("myxml.xml", "w", encoding ='utf-8') as f:
    f.write(xml_str)

#Выгрузка из XML

node = doc.documentElement
computers = doc.getElementsByTagName("Computer")
titles = []
for perf in computers:
    titleObj = perf.getElementsByTagName("name")[0]
    titles.append(titleObj)
for title in titles:
    nodes = title.childNodes
    for node in nodes:
        if node.nodeType ==node.TEXT_NODE:
            print(node.data)
