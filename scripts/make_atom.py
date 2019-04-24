import csv
from rfc3339 import rfc3339
from lxml import etree
from datetime import datetime

# Generates the XML
new_feed = etree.Element('feed', attrib={'xmlns':'http://www.w3.org/2005/Atom'})
etree.SubElement(new_feed, 'title').text = "A blog by Nicolas Kayser-Bril"
etree.SubElement(new_feed, 'link', attrib={'href':'https://blog.nkb.fr/atom.xml', 'rel':'self'})
etree.SubElement(new_feed, 'id').text = 'https://blog.nkb.fr/'
etree.SubElement(new_feed, 'updated').text = rfc3339(datetime.utcnow(), utc=True)

# Parses the CSV
num_art = 0
with open('public/assets/articles.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if row['is_external'] == '1':
            url = row['url']
        else:
            url = "https://blog.nkb.fr/" + row['url'] + "/"
        post = etree.SubElement(new_feed, 'entry')
        etree.SubElement(post, 'updated').text = rfc3339(datetime.strptime(row['date'], "%B %d, %Y"), utc=True)
        etree.SubElement(post, 'title').text = row['title']
        etree.SubElement(post, 'link', attrib={'href':url, 'rel':'alternate'})
        etree.SubElement(post, 'id').text = url
        content = etree.SubElement(post, 'content', attrib={'type':'xhtml'})
        etree.SubElement(content, 'div', attrib={'xmlns':"http://www.w3.org/1999/xhtml"}).text = """
            Sorry, I failed to account for RSS readers when I built my website - and I personnally feed my RSS subscriptions directly to Pocket.
            Read %s by following the link.
        """ % (row['title'])
        author = etree.SubElement(post, 'author')
        etree.SubElement(author, 'name').text = "Nicolas Kayser-Bril"
        num_art+=1
        if num_art >= 10:
        	break

# Saves the feed
with open('atom.xml', 'w') as file:
    file.write(str(etree.tostring(new_feed, encoding='unicode')))