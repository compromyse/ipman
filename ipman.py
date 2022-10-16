#!/usr/bin/env python3
from pynput.keyboard import Controller
import gi
import sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib

pastekey = Controller()

try:
    option = sys.argv[1]
except IndexError:
    print(f"Usage: python3 {sys.argv[0]} [paste]/[setip]")


class EntryWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Enter The IP Address.")
        self.set_size_request(250, 47)

        self.timeout_id = None

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.entry = Gtk.Entry()
        vbox.pack_start(self.entry, True, True, 0)
        self.entry.connect("activate", self.onok)

        hbox = Gtk.Box(spacing=6)
        vbox.pack_start(hbox, True, True, 0)

    def onok(self, widget):
        global currentip
        with open("/tmp/tempaddr", "w") as h:
            h.write(widget.get_text())
        self.destroy()


def prompt():
    win = EntryWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()


def paste(text):
    pastekey.type(text)


def main():
    if option == "paste":
        try:
            with open("/tmp/tempaddr", "r") as h:
                paste(h.read().strip())
        except:
            pass
    elif option == "setip":
        prompt()


if __name__ == "__main__":
    try:
        main()
    except:
        pass
