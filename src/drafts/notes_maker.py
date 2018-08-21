#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from getopt import getopt
import requests, re, time, urllib, glob

# notes_maker -f filename -l -n
# n is for no link

options, args = getopt(argv[1:],"f:ln")
lg = "en"
nolink = False
for option, value in options:
	if option == "-f":
		filename = value
	elif option == "-l":
		lg = "fr"
	elif option == "-n":
		nolink = True

headers = {
"Host": "archive.is",
"Connection": "keep-alive",
"Content-Length": "150",
"Cache-Control": "max-age=0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Origin": "http://archive.is",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
"Content-Type": "application/x-www-form-urlencoded",
"Referer": "http://archive.is/",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.8"
}

if lg == "fr":
	nl = """



<h4>Pub</h4>
<img src="../images/bouffes_bluffantes.jpg" height="400" style="float: left;">
<p>Si vous avez aimé cet essai, vous allez adorer mon livre <a href='https://www.amazon.fr/Bouffes-Bluffantes-Kayser-Bril-Nicolas/dp/2955966053/' target='_blank'>Bouffes Bluffantes</a>, une histoire de l'humanité par l'alimentation.</p>
<p>« Un livre parfait pour l'été » Atabula</p>
<p>« On se régale » Le Vif</p>


<h4>Newsletter</h4>
<p>Si vous voulez recevoir mon prochain texte directement par e-mail, indiquez votre adresse ci-dessous.</p>
<form style="padding:3px;" action="https://tinyletter.com/nkb" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/nkb', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><p><label for="tlemail">Indiquez votre e-mail</label></p><p><input type="text" style="width:300px" name="email" id="tlemail" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Envoyer" /></form>
"""
else:
	nl = """


<h4>Newsletter</h4>
<p>In case you want to read my next essay in your e-mail inbox, type you email below and you'll be all set.</p>
<form style="padding:3px;" action="https://tinyletter.com/nkb" method="post" target="popupwindow" onsubmit="window.open('https://tinyletter.com/nkb', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true"><p><label for="tlemail">Enter your email address</label></p><p><input type="text" style="width:300px" name="email" id="tlemail" /></p><input type="hidden" value="1" name="embed"/><input type="submit" value="Subscribe" /></form>
"""

txt = open(filename)

txt_contents = txt.read()

notes = "\n\n <a name='notes' ></a>\n\n### Notes \n\n"
notes_counter = 0

pattern = '<note content="(.*?)">'

# Finds the notes

q = re.compile(pattern)
for match in q.finditer(txt_contents):
	notes_counter += 1
	note = match.group(1)

	# Saves the page if there is one
	pattern_url = '\[.*?\]\((.*?)\)'
	l = re.compile(pattern_url)
	for match_url in l.finditer(note):
		url = match_url.group(1)

		if nolink == False:
			submiturl = 'http://archive.is/submit/'
			submitid = 'dKcRmqFfNJ3YMmqus%2B8VHtMyZn8jImBpRzGaTfX6jknvpcyUWE1RyIqBMc8uJSO%2B'
			payload = 'submitid=' + submitid + ' &url=' + urllib.quote_plus(url)
			r = requests.post(submiturl, data=payload, headers=headers)
			print "Submitting URL " + url
			time.sleep(3)

		new_url = "https://archive.is/" + time.strftime("%Y%m%d") + "/" + url
		note = note.replace(url, new_url)

	#replaces markdown for links
	cleanr = re.compile('\]\(.*?\)')
	note_clean = re.sub(cleanr, '’', note).replace("[", "‘").replace("'", "’").replace("_", "").replace("</sup>", "").replace("<sup>", "")

	notes += "\n\n<a href='#note_" + str(notes_counter) + "' name='foot_" + str(notes_counter) + "' data-text='" + note_clean + "'>" + str(notes_counter) + ".</a> " + note + "\n"
	txt_contents = txt_contents.replace(match.group(0), "<sup><a name='note_" + str(notes_counter) + "' id='#note_" + str(notes_counter) + "' class='note_anchor' href='#foot_"+ str(notes_counter) +"'>" + str(notes_counter) + "</a></sup>")

# Adds the NL
txt_contents += nl

# Adds the notes
if notes_counter > 0:
	txt_contents += notes

# Searches for centuries en
pattern_cent = '(\d\d)th'
t = re.compile(pattern_cent)
for match in t.finditer(txt_contents):
	txt_contents = txt_contents.replace(match.group(0), match.group(0).replace("th", "") + "<sup>th</sup>")

# Searches for centuries fr
pattern_cent = '(\d\d)e'
t = re.compile(pattern_cent)
for match in t.finditer(txt_contents):
	txt_contents = txt_contents.replace(match.group(0), match.group(0).replace("e", "") + "<sup>e</sup> ")

# Creates the new file

new_filename = "../_posts/" + time.strftime("%Y-%m-%d") + "-" + filename.replace(".draft", "")
target = open(new_filename, 'w')
target.write(txt_contents)
target.close()
txt.close()
