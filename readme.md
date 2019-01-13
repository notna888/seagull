# Seagull Page Generation Script

[![license][]](https://opensource.org/licenses/MIT)
[![semver][]](http://semver.org)

[license]: https://img.shields.io/github/license/notna888/seagull.svg?style=plastic
[semver]: http://img.shields.io/:semver-0.1.1-green.svg?style=plastic


I don't honestly expect anyone to use this, it's mostly just for me.

Basically I found myself liking features of having django's templating engine while not using all those neat things that you get with a full fat python framework.

At the same time I found myself copying and pasting bits and pieces that set up my pages how I like them with jquery and a bootstrap navbar etc on them, and when I could be bothered, adding quite basic ajax navigation. Then it hit me, I should just write a python script that does this stuff for me.


Needs at minimum Python 3.5, (I think - I use some features that were apparently only added in that version) Tested & Built with 3.7.1

Some features though in case I forget.
*   Compiles scss.
*   Minifies JS and CSS.
*   Uses jinja2 for html templating.
*   Uses Jquery, Bootstrap, Popper.js.
*   Has ajax navigation that I've written.


There's lots of improvements I've got to make to it, but for now it's okay to share I think, I hope it's at least somewhat useful for someone else besides me.

Webpack was one of the last things I actually included in it - hence why I use libsass and jinja seperately.

Named Seagull as a homage to Pelican, which is what inspired me to make this.

## Features to develop
*   ~~Automatically picking up on all the html files and compiling them.~~
*   ~~Better support for sub folders and junk?~~
*   Make the ajax navigation do stuff with history
*   Improve the ajax navigation in general
*   I'll move the templates folder into the pages subdirectory at some point, I've just got to make a few changes so that'll work.
*   Change up how I've set out my base template so that it is in a couple of pieces like a head, nav and footer maybe?
*   <Maybe> Autogenerate the navbar? (Might be an flag for the cli options)
*   Add command line options
*   auto-run the python web server
*   watch for changes and re-run the code when changes occur
