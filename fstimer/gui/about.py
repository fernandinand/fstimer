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
'''Handles the about window of the application'''

import pygtk
pygtk.require('2.0')
import gtk

class AboutWin(gtk.AboutDialog):
    '''Handles the about window of the application'''

    def __init__(self):
        '''Creates the about window'''
        super(AboutWin, self).__init__()
        self.set_logo(gtk.gdk.pixbuf_new_from_file("fstimer/data/icon.png"))
        self.set_program_name('fsTimer')
        self.set_version('0.5')
        self.set_copyright("""Copyright 2012-14 Ben Letham\
        \nThis program comes with ABSOLUTELY NO WARRANTY; for details see license.\
        \nThis is free software, and you are welcome to redistribute it under certain conditions; see license for details""")
        self.set_comments('free, open source software for race timing.')
        self.set_website('http://fstimer.org')
        self.set_wrap_license(False)
        with open('COPYING', 'r') as fin:
            gpl = fin.read()
        self.set_license(gpl)
        self.set_authors(['Ben Letham',
                          'Sebastien Ponce',
                          'Testing by Stewart Hamblin'])
        self.run()
        self.destroy()
