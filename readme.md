# Seagull Page Generation Script

[![license][]](https://opensource.org/licenses/MIT)
[![semver][]](http://semver.org)

[license]: https://img.shields.io/github/license/notna888/seagull.svg?style=plastic
[semver]: http://img.shields.io/:semver-0.1.1-green.svg?style=plastic

## A Static Site Generator that doesn't generate anything for you

I don't honestly expect anyone to use this, it's mostly just for me.

Basically I found myself liking features of having django's templating engine while not using all those neat things that you get with a full fat python framework. Hell, I wasn't even using server side scripting. (That being said I think this should work with php as long as your host supports it)

At the same time I found myself copying and pasting bits and pieces that set up my pages how I like them with jquery and a bootstrap navbar etc on them, and when I could be bothered, adding quite basic ajax navigation. Then it hit me, I should just write a python script that does this stuff for me.

Named Seagull as a homage to Pelican, which is what inspired me to make this.

Needs at minimum Python 3.5, (I think - I use some features that were apparently only added in that version) Tested & Built with 3.7.1

## Features:
*   Compiles scss.
*   Minifies JS and CSS.
*   Uses jinja2 for html templating.
*   Copies eveything to a handy "output" folder that you can just upload to your webhost
*   Uses Jquery, Bootstrap, Popper.js.
*   Has ajax navigation that I've written.

## Installing / Usage

### Installation:
git clone this repo

### Usage
python compilePages.py

### Updating
For the foreseeable future - Just replace the compilePages.py file and the files in resources.

There's lots of improvements I've got to make to it, but for now it's okay to share I think, I hope it's at least somewhat useful for someone else besides me.

Webpack was one of the last things I actually included in it - hence why I use libsass and jinja seperately.


## Features to develop
*   ~~Automatically picking up on all the html files and compiling them.~~
*   ~~Better support for sub folders and junk?~~
*   Development mode that doesn't minify the js/css but does everything else
*   Make the ajax navigation do stuff with history
*   Improve the ajax navigation in general
*   I'll move the templates folder into the pages subdirectory at some point, I've just got to make a few changes so that'll work.
*   Change up how I've set out my base template so that it is in a couple of pieces like a head, nav and footer maybe?
*   Add command line options
*   Auto-run the python web server
*   Watch for changes and re-run the code when changes occur
*   Support CSS and JS on individual pages (Currently the only way to have stuff specific to individual pages is to have it in the html itself.)
*   Maybe - Autogenerate the navbar from folder/file names? (Might be an flag for the cli options)
