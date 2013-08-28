#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from subprocess import call
from gi.repository import Gtk


# Image Image Play Configure Label
# 0     1     2    3         4

class Game(object):

    def __init__(self, path, confpath, conf, label):
        self.path = path
        self.label = label
        self.confpath = confpath
        self.conf = conf


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Game Chooser")

    def launch(self, widget, *data):
        call(data[0])


# Il y aura bien évidemment plus de deux jeux sinon je ne m'embêterai pas.
amnesia = Game(path="/usr/games/Amnesia/Amnesia.bin64", confpath="/usr/games/Amnesia/Launcher.bin64", conf=True, label="Amnesia")
aquaria = Game(path="/usr/games/Aquaria/aquaria", confpath=None, conf=False, label="Aquaria")
minecraft = Game(path="minecraft", confpath=None, conf=False, label="Minecraft")
botanicula = Game(path="/usr/games/Botanicula/botanicula", confpath=None, conf=False, label="Botanicula")
frogatto = Game(path="/usr/bin/frogatto", confpath=None, conf=False, label="Frogatto")
GAMES = [amnesia, aquaria, minecraft, botanicula, frogatto]

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.set_title("Game Chooser")
win.set_border_width(10)
win.set_icon_from_file("/usr/share/icons/Faenza/devices/scalable/joystick.svg")
win.set_resizable(False)

win.table = Gtk.Table(len(GAMES), 3, True)
win.table.set_row_spacings(5)
win.table.set_col_spacings(25)

x = 0
for game in GAMES:
    image = Gtk.Image()
    image.set_from_stock(Gtk.STOCK_MEDIA_PLAY, Gtk.IconSize.BUTTON)
    play_button = Gtk.Button()
    play_button.set_image(image)
    play_button.connect("clicked", win.launch, game.path) # Rajout d'un argument dans l'appel
    win.table.attach(play_button, 1, 2, x, x+1)
    if game.conf:
        image = Gtk.Image()
        image.set_from_stock(Gtk.STOCK_EXECUTE, Gtk.IconSize.BUTTON)
        conf_button = Gtk.Button()
        conf_button.set_image(image)
        conf_button.connect("clicked", win.launch, game.confpath)
        win.table.attach(conf_button, 2, 3, x, x+1)

    label = Gtk.Label(game.label)
    label.set_justify(Gtk.Justification.LEFT)
    win.table.attach(label, 0, 1, x, x+1)
    x += 1

win.add(win.table)
win.show_all()
Gtk.main()