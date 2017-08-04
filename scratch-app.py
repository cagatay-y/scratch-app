#!/usr/bin/python3

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk,WebKit2
from subprocess import Popen

def quit(app):
    Gtk.main_quit()
    server.terminate()

server = Popen(["npm", "start"], cwd="/app/lib/node_modules/scratch-gui")

webview = WebKit2.WebView()
webview.open("localhost:8601")

window = Gtk.Window()
window.connect("destroy", quit)
window.set_default_size(800, 600)

window.add(webview)
window.show_all()
Gtk.main()
