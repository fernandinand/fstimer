#fsTimer - free, open source software for race timing.
#Copyright 2012-14 Ben Letham

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#The author/copyright holder can be contacted at bletham@gmail.com
'''Handling of the new project windows'''

import pygtk
pygtk.require('2.0')
import gtk
import fstimer.gui

class ProjectTypeWin(gtk.Window):
    '''Handles setting project settings'''

    def __init__(self, project_types, projecttype, numlaps, back_clicked_cb, next_clicked_cb, parent):
        '''Creates project type window'''
        super(ProjectTypeWin, self).__init__(gtk.WINDOW_TOPLEVEL)
        self.modify_bg(gtk.STATE_NORMAL, fstimer.gui.bgcolor)
        self.set_transient_for(parent)
        self.set_modal(True)
        self.set_title('fsTimer - Project type')
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(20)
        self.connect('delete_event', lambda b, jnk_unused: self.hide())
        # Now create the vbox.
        vbox = gtk.VBox(False, 50)
        self.add(vbox)
        ##First is the project type
        label_0 = gtk.Label('Select the race type.')
        rbs = {}
        rbs[0] = gtk.RadioButton(group=None, label='Standard.\t All runners begin at the same time.')
        rbs[1] = gtk.RadioButton(group=rbs[0], label='Handicap.\t Some runners are assigned a handicap and start the race later.')
        #Set the correct button active
        rbs[project_types.index(projecttype)].set_active(True)
        ##Second are other race settigns.
        label_1 = gtk.Label('Additional race options:')
        check_button = gtk.CheckButton(label='Lap timing - Check the box and specify the number of laps if more than one:')
        numlapsadj = gtk.Adjustment(value=2, lower=2, upper=10, step_incr=1)
        numlapsbtn = gtk.SpinButton(numlapsadj, digits=0, climb_rate=0)
        #Activate the button as needed
        if numlaps > 1:
            check_button.set_active(True)
            numlapsadj.set_value(numlaps)
        else:
            check_button.set_active(False)
            numlapsadj.set_value(2)
        #Pop these in an hbox
        hbox_0 = gtk.HBox(False, 0)
        hbox_0.pack_start(check_button, False, False, 8)
        hbox_0.pack_start(numlapsbtn, False, False, 8)
        # And an hbox with 2 buttons
        hbox_1 = gtk.HBox(False, 0)
        btnCANCEL = gtk.Button(stock=gtk.STOCK_CANCEL)
        btnCANCEL.connect('clicked', lambda btn: self.hide())
        alignCANCEL = gtk.Alignment(0, 0, 0, 0)
        alignCANCEL.add(btnCANCEL)
        btnBACK = gtk.Button(stock=gtk.STOCK_GO_BACK)
        btnBACK.connect('clicked', back_clicked_cb)
        btnNEXT = gtk.Button(stock=gtk.STOCK_GO_FORWARD)
        btnNEXT.connect('clicked', next_clicked_cb, rbs, check_button, numlapsbtn)
        alignNEXT = gtk.Alignment(1, 0, 1, 0)
        alignNEXT.add(btnNEXT)
        alignBACK = gtk.Alignment(1, 0, 1, 0)
        alignBACK.add(btnBACK)
        # And populate
        hbox_1.pack_start(alignCANCEL, True, True, 0)
        hbox_1.pack_start(alignBACK, False, False, 0)
        hbox_1.pack_start(alignNEXT, False, False, 0)
        vbox1 = gtk.VBox(False, 10)
        vbox2 = gtk.VBox(False, 10)
        vbox1.pack_start(label_0, False, False, 0)
        vbox1.pack_start(rbs[0], False, False, 0)
        vbox1.pack_start(rbs[1], False, False, 0)
        vbox2.pack_start(label_1, False, False, 0)
        vbox2.pack_start(hbox_0, False, False, 0)
        vbox2.pack_start(hbox_1, False, False, 0)
        vbox.pack_start(vbox1, False, False, 0)
        vbox.pack_start(vbox2, False, False, 0)
        self.show_all()
