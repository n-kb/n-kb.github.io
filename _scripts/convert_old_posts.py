from os import listdir
from os.path import isfile, join
from datetime import datetime
import re,json

mypath = "src/old_posts"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for filename in onlyfiles:
	date = filename[0:10]
	datetime_object = datetime.strptime(date, '%Y-%m-%d')
	date_format = datetime_object.strftime('%B %d, %Y')
	intro = "An essay by"
	share = "Share"
	file = open(mypath + "/" + filename, "r")
	file_string = file.read()
	matchObj = re.search( r'title: \"(.+)\"', file_string, re.M)
	if matchObj:
		title = matchObj.group(1)
	else:
		title = ""

	matchObj = re.search( r'image: \"images\/(.+)\"', file_string, re.M)
	if matchObj:
		image = matchObj.group(1)
	else:
		image = ""

	matchObj = re.search( r'description: \"(.+)\"', file_string, re.M)
	if matchObj:
		description = matchObj.group(1)
	else:
		description = ""
	print (filename, title, image, date_format)

	# Removes the metadata from the markdown file
	text = file_string[file_string.find("---", 10):]

	# Replaces images path
	text = re.sub(r'\"\.\.\/images\/(.+)\"', r'"./public/images/\1"', text)

	# Removes and replaces the newsletter block
	newsletter_block_en = "<article class='message is-link' id='newsletter'>  <div class='message-header'>    <p>Newsletter</p>  </div>  <div class='message-body'>    <p>Write down your e-mail in the box below and you'll receive my next text directly in your inbox.</p>\n<form style='padding:3px;' action='https://tinyletter.com/nkb' method='post' target='popupwindow' onsubmit='window.open('https://tinyletter.com/nkb', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true'><p><input type='text' style='width:300px' placeholder='Your e-mail address here' name='email' id='tlemail' class='input'/></p><input type='hidden' value='1' name='embed'/><input type='submit' value='Submit' class='button is-link' /></form>  </div></article>"

	text = re.sub(r'<h4>Newsletter<\/h4>.+In case.+<\/form>', newsletter_block_en, text, flags=re.S)

	newsletter_block_fr = "<article class='message is-link' id='newsletter'>  <div class='message-header'>    <p>Newsletter</p>  </div>  <div class='message-body'>    <p>Si vous voulez recevoir mon prochain texte directement par e-mail, indiquez votre adresse ci-dessous.</p>\n<form style='padding:3px;' action='https://tinyletter.com/nkb' method='post' target='popupwindow' onsubmit='window.open('https://tinyletter.com/nkb', 'popupwindow', 'scrollbars=yes,width=800,height=600');return true'><p><input type='text' style='width:300px' placeholder='Votre adresse e-mail ici' name='email' id='tlemail' class='input'/></p><input type='hidden' value='1' name='embed'/><input type='submit' value='Envoyer' class='button is-link' /></form>  </div></article>"

	text = re.sub(r'<h4>Newsletter<\/h4>.+Si.+<\/form>', newsletter_block_fr, text, flags=re.S)

	# Saves everything to a new json
	with open('src/articles/' + filename[11:-3] + ".json", 'w+') as fp:
		json.dump({
				"title": title,
				"date": date_format,
				"image": image,
				"intro": intro,
				"share": share,
				"text": text,
				"description": description
			}, fp)