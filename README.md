#pydown
pydown is another "Presentation System in a single HTML page" written by python inspired by [keydown](https://github.com/infews/keydown).

Like keydown it uses the [deck.js](http://imakewebthings.github.com/deck.js) and its extentions for the presentation.

##Demo
[http://isnowfy.github.io/pydown/](http://isnowfy.github.io/pydown/)

##Usage

###Write your slides in markdown
Edit slides.md
~~~~
!SLIDE

# Hello

!SLIDE

# Another slide

!SLIDE left

# left
~~~~

###Generate the html

~~~~
python main.py slides.md slides
~~~~

This will make:
~~~~
| - slides/
  | - css/
  | - js/
  | - index.html
~~~~

###Slide classes

Any text follows !SLIDE will be added to the slide as css classes
~~~~
!SLIDE left
~~~~

###Syntax Highlighting

For python
<pre>
~~~~{python}
   def test():
       print 'hello'
~~~~
</pre>

###Markdown syntax

[English version](http://daringfireball.net/projects/markdown/syntax)

[Chinese version](https://gitcafe.com/riku/Markdown-Syntax-CN/)
