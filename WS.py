
#coding: utf-8
#Author: Mirela Hilmkvist

from bottle import route, run, template, request, static_file, error, response from os import listdir import os

from text_p import * from loggs import *

@error(404) def error404(error): """ Shows an error message whenever the user tries to acces a page that does not exist. """

return template("template.tpl", base="</br><h2>sidan under uppbygnad</h2>")
@route('/') def start(): """ Shows the home page. """

sid = request.get_cookie("account", secret='some-secret-key')
email = get_email(str(sid))
if email:
    return template("start.tpl", email=email)
else:
    return template("start.tpl", email='')
@route('/material') def mat(): sid = request.get_cookie("account", secret='some-secret-key') email = get_email(str(sid)) if email: return template("tip_us.tpl", email = email) else: return template("tip_us.tpl", email='')

@route('/program') def programs(): sid = request.get_cookie("account", secret='some-secret-key') email = get_email(str(sid)) if email: return template('program.tpl', email = email) else: return template('program.tpl', email='')

@route('/program/arhitect') def arhitect(): sid = request.get_cookie("account", secret='some-secret-key') email = get_email(str(sid)) if email: return template('architect.tpl', email=email) else: return template('architect.tpl', email='')

@route('/contact') def contact(): sid = request.get_cookie("account", secret='some-secret-key') email = get_email(str(sid)) if email: return template('contact.tpl', email=email) else: return template('contact.tpl', email='')

"""The main job of the session table is used to translate between the session key and the user identity. The session table stores the username as part of the session data so that when a valid cookie is received, the application can identify the logged in user."""

@route('/conversations') def discussions(): #verify sid = request.get_cookie("account", secret='some-secret-key') email = get_email(str(sid))

path = os.path.abspath('date/conversations')
path = path.replace("\\", "/")
files = listdir(path)
mode='r'

text = []
for fis in files:
    n_path = path + '/' + fis +'/det.txt'
    fob = open(n_path, mode)
    all_text = fob.read()
    text.append(all_text)
    fob.close()

if email:
    return template("discussions", email = email, list_sf = files, detalii = text)
else:
    return template("login.tpl", matching="", email = '')
@route('/discussions')
route('/conversations/') def sub_forums(name): sid = request.get_cookie("account", secret='some-secret-key') email = get_email(str(sid))

# get all text files add possibility to add a discusion
directory = 'date/conversations/' + name
path = os.path.abspath(directory)
path = path.replace("\\", "/")
files = listdir(path)


if email:
    return template("discussions", email = email, list_sf = '', detalii = '')
else:
    return template("login.tpl", matching="", email = '')


return "<p>Bla bla bla</p>"
for css
@route('filename:path') @route ('/program/filename:path')

def send_static(filename): return static_file(filename, root='views')

run(host='localhost', port=8080, debug=True, reloader=True)
