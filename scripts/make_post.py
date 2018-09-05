from sys import argv
from getopt import getopt
import requests, re, time, urllib, glob, json
from urllib.parse import quote

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
	newsletter_block = "\n\n<article class='message is-link' id='newsletter'>  <div class='message-header'>    <p>Newsletter</p>  </div>  <div class='message-body'>    <p>Si vous voulez recevoir mon prochain texte directement par e-mail, indiquez votre adresse ci-dessous.</p>\n<form style='padding:3px;' action='https://tinyletter.com/nkb' method='post' target='popupwindow' onsubmit='window.open('https://tinyletter.com/nkb', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true'><p><input type='text' style='width:300px' placeholder='Votre adresse e-mail ici' name='email' id='tlemail' class='input'/></p><input type='hidden' value='1' name='embed'/><input type='submit' value='Envoyer' class='button is-link' /></form>  </div></article>"
else:
	newsletter_block = "\n\n<article class='message is-link' id='newsletter'>  <div class='message-header'>    <p>Newsletter</p>  </div>  <div class='message-body'>    <p>Write down your e-mail in the box below and you'll receive my next text directly in your inbox.</p>\n<form style='padding:3px;' action='https://tinyletter.com/nkb' method='post' target='popupwindow' onsubmit='window.open('https://tinyletter.com/nkb', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true'><p><input type='text' style='width:300px' placeholder='Your e-mail address here' name='email' id='tlemail' class='input'/></p><input type='hidden' value='1' name='embed'/><input type='submit' value='Submit' class='button is-link' /></form>  </div></article>"

title = filename.replace(".draft.md", "").replace("../public/drafts/wip/", "")

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
	pattern_url = r'\[.*?\]\((.*?)\)'
	l = re.compile(pattern_url)
	for match_url in l.finditer(note):
		url = match_url.group(1)

		if nolink == False:
			submiturl = 'http://archive.is/submit/'
			submitid = 'dKcRmqFfNJ3YMmqus%2B8VHtMyZn8jImBpRzGaTfX6jknvpcyUWE1RyIqBMc8uJSO%2B'
			payload = 'submitid=' + submitid + ' &url=' + quote(url)
			r = requests.post(submiturl, data=payload, headers=headers)
			print ("Submitting URL " + url)
			time.sleep(3)

		new_url = "https://archive.is/" + time.strftime("%Y%m%d") + "/" + url
		note = note.replace(url, new_url)

	#replaces markdown for links
	cleanr = re.compile(r'\]\(.*?\)')
	note_clean = re.sub(cleanr, '’', note).replace("[", "‘").replace("'", "’").replace("_", "").replace("</sup>", "").replace("<sup>", "")

	notes += "\n\n<a href='#note_" + str(notes_counter) + "' name='foot_" + str(notes_counter) + "' data-text='" + note_clean + "'>" + str(notes_counter) + ".</a> " + note + "\n"
	txt_contents = txt_contents.replace(match.group(0), "<sup><a name='note_" + str(notes_counter) + "' id='#note_" + str(notes_counter) + "' class='note_anchor' href='#foot_"+ str(notes_counter) +"'>" + str(notes_counter) + "</a></sup>")

# Adds the NL
txt_contents += newsletter_block

# Adds the notes
if notes_counter > 0:
	txt_contents += notes

# Searches for centuries en and fr
txt_contents = re.sub(r'(\d\d)th', r'\1<sup>th</sup>', txt_contents)
txt_contents = re.sub(r'(\d\d)e', r'\1<sup>e</sup>', txt_contents)

json_dict = {
    "title": re.search( r'title: \"(.+)\"', txt_contents, re.M).group(1),
    "date": re.search( r'date: \"(.+)\"', txt_contents, re.M).group(1),
    "image": re.search( r'image: \"(.+)\"', txt_contents, re.M).group(1),
    "intro":re.search( r'intro: \"(.+)\"', txt_contents, re.M).group(1),
    "share": re.search( r'share: \"(.+)\"', txt_contents, re.M).group(1),
    "text": txt_contents[txt_contents.find("---", 10):],
    "description": re.search( r'description: \"(.+)\"', txt_contents, re.M).group(1)
}

# Creates the new file
new_filename = "../public/articles/" + title + ".json"
with open(new_filename, 'w+') as fp:
	json.dump(json_dict, fp)
