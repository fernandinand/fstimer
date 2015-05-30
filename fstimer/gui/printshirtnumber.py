# fsTimer - free, open source software for race timing.
# Copyright 2012-14 Ben Letham

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# The author/copyright holder can be contacted at bletham@gmail.com
'''Handling of the print shirt racing number window'''

import pygtk

pygtk.require('2.0')
import gtk
import os
import fstimer.gui


class PrintShirtNumberWin(gtk.Window):
    '''Handles the setup for printing new shirt racing numbers'''

    def __init__(self, path, flag, print_shirtnumb_cb):
        '''Creates print shirt racing numbers window'''
        super(PrintShirtNumberWin, self).__init__(gtk.WINDOW_TOPLEVEL)
        self.modify_bg(gtk.STATE_NORMAL, fstimer.gui.bgcolor)
        self.path = path
        self.print_shirtnumb_cb = print_shirtnumb_cb
        self.flag = flag
        # TODO: Ability to set all options from print window
        # Global options
        self.options = {}
        self.options['fontNumbers'] = 'fstimer/fonts/dirt2 soulstalker.otf'
        self.options['fontLetters'] = 'fstimer/fonts/28 Days Later.ttf'
        self.options['fontColor'] = (40, 40, 40)
        self.options['background'] = 'fstimer/data/background.png'
        self.options['logo'] = 'fstimer/data/fstimer_logo.png'
        self.options['export'] = 'fstimer/export/'
        self.set_modal(True)
        self.set_title('fsTimer - Print Shirt Racing Numbers')
        self.set_position(gtk.WIN_POS_CENTER)
        self.connect('delete_event', lambda b, jnk: self.hide())
        self.set_border_width(10)
        # Event Name.
        label_0 = gtk.Label('Enter the event/race name.')
        # And an error, if needed..
        self.label_00 = gtk.Label()
        self.label_00.set_line_wrap(True)
        # And the text entry
        self.eventname = gtk.Entry(max=80)
        # Background image.
        label_1 = gtk.Label('Choose the background file.')
        # And the text entry
        btnBKGFILE = gtk.Button('Choose file')
        btnBKGFILE.connect('clicked', self.choose_images, 'background')
        self.background = gtk.Entry(max=120)
        self.background.set_text(self.options['background'])
        # Background image.
        label_2 = gtk.Label('Choose the race logo file.')
        # And the text entry
        btnLGFILE = gtk.Button('Choose file')
        btnLGFILE.connect('clicked', self.choose_images, 'logo')
        self.logo = gtk.Entry(max=120)
        self.logo.set_text(self.options['logo'])
        # Background image.
        self.label_fontscolor = gtk.Label('')
        self.label_fontscolor.set_markup('<span color="grey">Test your font color.</span>')
        # And the text entry
        btnCOLOR = gtk.Button('Choose Color')
        btnCOLOR.connect('clicked', self.choose_color)
        # And the text entry
        btnEXPORT = gtk.Button('Choose export folder')
        btnEXPORT.connect('clicked', self.choose_folder)
        self.export = gtk.Entry(max=120)
        self.export.set_text(self.options['export'])
        # And an hbox with 2 buttons
        hbox_1 = gtk.HBox(False, 0)
        btnCANCEL = gtk.Button(stock=gtk.STOCK_CLOSE)
        btnCANCEL.connect('clicked', lambda btn: self.hide())
        alignCANCEL = gtk.Alignment(0, 0, 0, 0)
        alignCANCEL.add(btnCANCEL)
        btnPRINT = gtk.Button(stock=gtk.STOCK_PRINT)
        btnPRINT.connect('clicked', self.doPrint)
        alignPRINT = gtk.Alignment(1, 0, 1, 0)
        alignPRINT.add(btnPRINT)
        btnPRINT.set_sensitive(False)
        # And populate
        self.eventname.connect("changed", self.lock_btn_print, btnPRINT)
        hbox_1.pack_start(alignCANCEL, True, True, 0)
        hbox_1.pack_start(alignPRINT, False, False, 0)
        # Now create the vbox.
        vbox = gtk.VBox(False, 10)
        vbox.pack_start(label_0, False, False, 0)
        vbox.pack_start(self.eventname, False, False, 0)
        vbox.pack_start(self.label_00, False, False, 0)
        vbox.pack_start(label_1, False, False, 0)
        vbox.pack_start(btnBKGFILE, False, False, 0)
        vbox.pack_start(self.background, False, False, 0)
        vbox.pack_start(label_2, False, False, 0)
        vbox.pack_start(btnLGFILE, False, False, 0)
        vbox.pack_start(self.logo, False, False, 0)
        vbox.pack_start(self.label_fontscolor, False, False, 0)
        vbox.pack_start(btnCOLOR, False, False, 0)
        vbox.pack_start(btnEXPORT, False, False, 0)
        vbox.pack_start(self.export, False, False, 0)
        vbox.pack_start(hbox_1, False, False, 0)
        self.add(vbox)
        self.show_all()

    def lock_btn_print(self, jnk_unused, btnPRINT):
        '''does not unlock btnPRINT if the event name is not set'''
        txt = self.eventname.get_text()
        if (len(txt) > 0):
            btnPRINT.set_sensitive(True)
            self.options['eventname'] = txt
        else:
            btnPRINT.set_sensitive(False)

    def choose_images(self, jnk_unused, entry_point):
        chooser = gtk.FileChooserDialog(title='Choose ' + entry_point + ' file', action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                        buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OK, gtk.RESPONSE_OK))
        chooser.set_current_folder(os.path.join(os.getcwd(), self.path))
        ffilter = gtk.FileFilter()
        ffilter.set_name('Image files')
        ffilter.add_pattern('*.png')
        ffilter.add_pattern('*.jpeg')
        ffilter.add_pattern('*.jpg')
        chooser.add_filter(ffilter)
        response = chooser.run()
        if response == gtk.RESPONSE_OK:
            filename = chooser.get_filename()
            if entry_point == 'background':
                self.options
                self.options['background'] = filename
                self.background.set_text(filename)
            elif entry_point == 'logo':
                self.options['logo'] = filename
                self.logo.set_text(filename)
        chooser.destroy()

    def choose_color(self, jnk_unused):
        colorpicker = gtk.ColorSelectionDialog('Select fonts color')
        response = colorpicker.run()
        if response == gtk.RESPONSE_OK:
            self.options['fontColor'] = self.hex_to_rgb(str(colorpicker.colorsel.get_current_color()))
            self.label_fontscolor.set_markup('<span color="' + str(colorpicker.colorsel.get_current_color()) +
                                             '">Test your font color.</span>')
        colorpicker.destroy()

    def choose_folder(self, jnk_unused):
        chooser = gtk.FileChooserDialog(title='Select Export Folder',
                                        action=gtk.FILE_CHOOSER_ACTION_SELECT_FOLDER,
                                        buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_OK, gtk.RESPONSE_OK))
        response = chooser.run()
        if response == gtk.RESPONSE_OK:
            self.options['export'] = chooser.get_filename()
            self.export.set_text(chooser.get_filename())
        chooser.destroy()

    # Convert HEX to PIL RGB
    def hex_to_rgb(self, value):
        value = value.lstrip('#')
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def doPrint(self, jnk_unused):
        self.print_shirtnumb_cb(self.options, self.flag)
        self.destroy()
