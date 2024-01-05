IEC 61131-3 Syntax Highlighting with highlight.js
#################################################

:date: 2020-09-01 23:00
:modified: 2020-09-01 23:38
:tags: iec-61131, documentation
:category: iec-61131
:slug: iec-61131-syntax-highlighting
:authors: Joe Stanley
:summary: Adding context to 61131 code snippets with `highlight.js`.

.. _Marpit: https://github.com/marp-team/marpit
.. _GitHub highlightjs Project: https://github.com/highlightjs/highlightjs-structured-text
.. _issue: https://github.com/highlightjs/highlightjs-structured-text/issues/9#issuecomment-685266264
.. _pull request: https://github.com/highlightjs/highlightjs-structured-text/pull/10

I've been investigating some new resources for high-level documentation, including
automated presentation builders, and along the way, a question arose.

If I want to demonstrate code examples for IEC 61131-3, is there a way that I can provide
syntax highlighting so that readers will be able to understand the material more clearly?

So what is syntax highlighting anyway? Well, for code snippets, syntax highlighting uses
various colors and fonts to isolate the unique keywords, operators, and other items that
are standard in that particular programming language. I'll show an example here momentarily.
This is very useful because it allows readers to quickly interpret what the code is
intentionally doing.

I was fortunate enough that I was able to find a project that was already providing syntax
highlighting for IEC 61131-3 in the `highlight.js` project framework (though not natively)
and thus, I could leverage existing work! Trouble is, since it's not already a native
"language" it comes with its own set of challenges. The source of this highlighter comes
from the `GitHub highlightjs Project`_

My challenge was identifying an effective way of declaring the language so that I could
use it with `Marpit`_ which is part of the Marp project; a system built to convert
markdown files to HTML or PPTX presentations. (Be on the lookout for an upcoming article
on this topic.)

Solution
--------

After much trial and tribulation, I finally realized a solution. Since I was using
`highlight.js` as a required module in the marp framework, I could simply add the language
definition and register it accordingly. Here are the steps I took to modify my installation
to make it work as I wished.

#. Locate existing highlight.js installation location by finding dependent module (in my
   case marp). Then open directory (since I'm using Windows, I can use 
   `Explorer <path/to/marp/directory>`

   .. image:: {attach}/images/61131-highlighting/cmd-view.png
      :alt: Identify the install location.

#. Navigate to the directory containing the module of interest, then navigate to the
   `node_modules/highlight.js` folder underneath the desired module. In my case, since
   I'm using marp-cli, I navigated to
   `node_modules/@marp-team/marp-cli/node_modules/highlight.js/lib`

   .. image:: {attach}/images/61131-highlighting/explorer-view.png
      :alt: Locate the `index.js` file for modification.

#. Open the `index.js` file in a text editor and add a new line to register the `iecst`
   language.

   .. image:: {attach}/images/61131-highlighting/register-language.png
      :alt: Registering the new language.

#. Finally, navigate to the languages folder and add the `iecst.js` file. Here, for my
   application, I had to make some modifications (which I documented fully in an `issue`_
   and `pull request`_ on the source repository).

Summary
-------

To make this long story longer, I'll be writing more later to document how my Marp
integration comes along. For the meantime, here's the takeaway:

Syntax highlighting *does* exist for IEC 61131-3, and it'll become easier to implement
going forward!


Oh, and how about what that syntax-highlighted code? What does it look like anyway?

Have a look for yourself!

.. image:: {attach}/images/61131-highlighting/61131example.png
   :alt: An example of (nonsense) syntax-highlighted 61131 code.
