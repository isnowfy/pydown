#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import codecs
import shutil
import optparse

from markdown import markdown


HERE = os.path.abspath(os.path.dirname(__file__))
markdown_options = ['extra', 'codehilite']


def copy(dst):
    try:
        shutil.copytree(os.path.join(HERE, 'templates', 'css'),
                        os.path.join(dst, "css"))
        shutil.copytree(os.path.join(HERE, 'templates', 'js'),
                        os.path.join(dst, 'js'))
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
        data += '<section class="slide %s">' % css\
                + '<div class="content">'\
                + markdown(item, markdown_options)\
                + '</div>'\
                + '</section>\n'
    index_template = os.path.join(HERE, 'templates', 'index.html')
    html = codecs.open(index_template, 'r', 'utf-8')
    html = html.read().replace('<slide>', data)
    f = codecs.open(os.path.join(dst, 'index.html'), 'w', 'utf-8')
    f.write(html)
    f.close()

def main():
    '''Main entry point for the pydown CLI.'''
    parser = optparse.OptionParser()
    (options, args) = parser.parse_args()
    if len(args) != 2:
        print 'usage: pydown mdfile directory'
    else:
        handle(*args)

if __name__ == '__main__':
    main()
