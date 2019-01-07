from jinja2 import FileSystemLoader
from jinja2 import Environment as Jinja2Environment
from webassets import Environment as AssetsEnvironment
from webassets.ext.jinja2 import AssetsExtension
from webassets import Bundle
import sass

import shutil
import os
import sys
import http
import re

# Need to remove the already compiled assets here...

compiledSass = ''
sass_files_to_compile = ['main.scss']
for sassFile in sass_files_to_compile:
    # with open('resources/css/scss/'+sassFile, 'r') as thisfile:
    #     SassData=thisfile.read()
    compiledSass += sass.compile(filename='resources/css/scss/'+sassFile, include_paths='resources/css/scss/vendor/')
with open('resources/css/sass.css', 'w') as outputFile:
    outputFile.write(compiledSass)

all_js = Bundle('**/*.js', filters='jsmin', output='packed.js')
all_css = Bundle('**/*.css', filters='cssmin', output="main.css")

jinja_env = Jinja2Environment(extensions=[AssetsExtension])
jinja_env.loader = FileSystemLoader('.')
assets_env = AssetsEnvironment(url='/assets', directory='resources')

assets_env.register('all_js', all_js)
assets_env.register('all_css', all_css)

jinja_env.assets_environment = assets_env

pages = ['index.html', 'second_page.html']
for page in pages:
    thisTemplate = jinja_env.get_template('pages/'+page)
    thisTempRendered = thisTemplate.render()
    with open('output/'+page, 'w') as tempFile:
        tempFile.write(thisTempRendered)

    # This bit is used for my ajax shenanigans
    # anything you want on a page needs to go on body though...
    result = re.search('<body>(.*)<\/body>', '"' + thisTempRendered.replace('"', '\"').replace('\n',' ') + '"')
    # print(result)
    onlyTheBodyPart = result.group(1)
    with open('output/content/'+page, 'w') as tempFile:
        tempFile.write(onlyTheBodyPart)

src = 'resources'
dst = 'output/assets'
filelist = []
files = ['main.css', 'packed.js']
for filename in files:
  filelist.append(filename)
  fullpath = src + '/' + filename
  shutil.move(os.path.join(src, filename), os.path.join(dst, filename))


# python -m http.server -d 'output'
