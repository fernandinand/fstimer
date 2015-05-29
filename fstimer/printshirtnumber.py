#!/usr/bin/env python
# coding: utf-8
__author__ = 'fernandinand'

# Copyright 2011 Álvaro Justen [alvarojusten at gmail dot com]
# License: GPL <http://www.gnu.org/copyleft/gpl.html>

from imagetext import ImageText
from imagemerge import ImageMerge


class PrintShirtNumber(object):
    def __init__(self, filename, options):
        self.background = options.background  # 'images/background.png'
        self.fontNumbers = 'fonts/dirt2 soulstalker.otf'
        self.fontLetters = 'fonts/28 Days Later.ttf'
        self.color = options.color  # (40, 40, 40)
        self.title = options.title
        self.logo = options.racelogo

    def printnumbers(self, registration):
        # color = (40, 40, 40)
        # text = 'I Trail TiMim'
        # fontNumbers = 'fonts/dirt2 soulstalker.otf'
        # fontLetters = 'fonts/28 Days Later.ttf'
        runner = 'Fernando Ribeiro'

        number_of_tickets = 5

        ns = [str(n) for n in range(number_of_tickets + 1)][1:]

        for item in ns:
            img = ImageText((750, 550), background=(255, 255, 255, 200))  # 200 = alpha
            number = str(int(3 - len(item)) * "0") + item
            img.write_text_box((180, 440), runner, box_width=400, font_filename=self.fontLetters,
                               font_size=24, color=self.color, place='center')
            img.write_text_box((180, 40), text, box_width=400, font_filename=self.fontLetters,
                               font_size=24, color=self.color, place='center')
            img.write_text((120, 40), number, font_filename=self.fontNumbers,
                           font_size='fill', max_height=200, color=self.color)
            # img.write_text_box((120, 40), number, box_width=450, font_filename=fontNumbers,
            #                font_size=269, color=color, place='center')

            img.save('export/temp_' + item + '.png')

            f = ImageMerge().merge('export/temp_' + item + '.png', self.logo)

            f.save('export/temp_' + item + '.png')

            f = img.merge(self.background, 'export/temp_' + item + '.png')

            f.save('export/dorsal_' + item + '.png')

            img = None
            f = None
