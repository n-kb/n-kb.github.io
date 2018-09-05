import csv
from lxml import etree
from datetime import datetime

# Generates the XML
new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed')
etree.SubElement(new_feed, 'title').text = "A blog by Nicolas Kayser-Bril"
etree.SubElement(new_feed, 'link', attrib={'href':'https://blog.nkb.fr/atom.xml', 'rel':'self'})
etree.SubElement(new_feed, 'link', attrib={'href':'https://blog.nkb.fr'})
etree.SubElement(new_feed, 'updated').text = datetime.utcnow().strftime("%Y-%m-%d")

# Parses the CSV
num_art = 0
with open('../_public/assets/articles.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        if row['is_external'] == '1':
            url = row['url']
        else:
            url = "https://blog.nkb.fr/" + row['url'] + "/"
        post = etree.SubElement(new_feed, 'entry')
        etree.SubElement(post, 'updated').text = datetime.strptime(row['date'], "%B %d, %Y").strftime("%Y-%m-%d")
        etree.SubElement(post, 'title').text = row['title']
        etree.SubElement(post, 'link', attrib={'href':url})
        num_art+=1
        if num_art >= 10:
        	break

# Saves the feed
with open('../atom.xml', 'w') as file:
    file.write(str(etree.tostring(new_feed, encoding='unicode')))