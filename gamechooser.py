#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from subprocess import call
from gi.repository import Gtk


# Image Image Play Configure Label
# 0     1     2    3         4

class Game(object):

    def __init__(self, path, label):
        self.path = path
        self.label = label
        self.button = None


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Game Chooser")

    def launch(self, widget, *data):
        call(data[0])


# Il y aura bien évidemment plus de deux jeux sinon je ne m'embêterai pas.
amnesia = Game(path="/usr/games/Amnesia/Launcher.bin64", label="Amnesia - The Dark Descent")
aquaria = Game(path="/usr/games/Aquaria/aquaria", label="Aquaria")
minecraft = Game(path="minecraft", label="Minecraft")
GAMES = [amnesia, aquaria, minecraft]

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.set_title("Game Chooser")
win.set_border_width(5)
win.table = Gtk.Table(len(GAMES), 2, True)

# Le premier boutton est important car il ne nécessite pas de
# attach_next_to() pour être ajouté à la grille
first_game = True
x = 0
for game in GAMES:
    button = Gtk.Button(label="Play")
    button.connect("clicked", win.launch, game.path) # Rajout d'un argument dans l'appel

    if first_game:
        win.table.attach(button, 0, 1, 0, 1)
        first_game = False

    else:
        win.table.attach(button, 0, 1, x, x+1)
    x += 1

label = Gtk.Label("Amnesia is Fun")
win.table.attach(label, 1, 2, 0, 1)
win.table.set_row_spacings(5)
win.table.set_column_spacings(10)
win.add(win.table)
win.show_all()
Gtk.main()