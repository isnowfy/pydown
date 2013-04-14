# -*- coding: utf-8 -*-

import os
import codecs
import shutil
import optparse

from markdown import markdown

markdown_options = ['extra', 'codehilite']

def copy(dst):
    try:
        shutil.copytree('templates/css', '%s/css' % dst)
        shutil.copytree('templates/js', '%s/js' % dst)
    except:
        pass

def slides_split(slides):
    data = ''
    css = ''
    for item in slides.split('\n'):
        if item.startswith('!SLIDE'):
            yield css, data
            css = ' '.join(item.split(' ')[1:])
            data = ''
        else:
            data += item+'\n'
    yield css, data

def handle(md, dst):
    copy(dst)
    slides = codecs.open(md, 'r', 'utf-8').read()
    data = ''
    for css, item in slides_split(slides):
        if not item:
            continue
        data += "<section class='slide %s'>" % css\
                + "<div class='content'>"\
                + markdown(item, markdown_options)\
                + "</div>"\
                + "</section>\n"
    html = codecs.open('templates/index.html', 'r', 'utf-8')
    html = html.read().replace('<slide>', data)
    f = codecs.open('%s/index.html' % dst, 'w', 'utf-8')
    f.write(html)
    f.close()

if __name__ == '__main__':
    parser = optparse.OptionParser()
    (options, args) = parser.parse_args()
    handle(*args)
