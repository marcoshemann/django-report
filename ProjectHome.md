# Introduction #

Django-report is a application that lays the foundation for generating simple printable PDF reports.

This is by now means a complete report generating suite, it just provide the strict necessary to create views that can be outputed either as HTML or PDF with minimum discrepancies as possible.

## How it works ##

It basically just output a HTML print friendly view which can be downloaded as PDF. Both the PDF file and the HTML view uses the same CSS file, which makes it easier to match the HTML output (preview) with the PDF (print document).

Matching the two outputs still isn't what we can call a walk to the park, but django-report makes it a lot easier.

## Dependencies ##

| **pisa** | http://pypi.python.org/pypi/pisa/ | pisa is a html2pdf converter using the ReportLab Toolkit, the HTML5lib and pyPdf. It supports HTML 5 and CSS 2.1 (and some of CSS 3). |
|:---------|:----------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| **ReportLab** | http://www.reportlab.org/oss/rl-toolkit/ | The ReportLab Toolkit is a library for programatically creating documents in PDF format.                                              |
| **html5lib** | http://code.google.com/p/html5lib/ | A ruby/python based HTML parser/tokenizer based on the WHATWG HTML5 specification for maximum compatibility with major desktop web browsers. |

## Screenshots ##

### HTML ###

![http://i.imgur.com/8cRtB.png](http://i.imgur.com/8cRtB.png)

### PDF ###

![http://i.imgur.com/qFNRO.png](http://i.imgur.com/qFNRO.png)