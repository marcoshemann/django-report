# Installing dependencies #

These instructions are for Ubuntu, it might differ on other platforms.

## pisa ##

| Home page | http://pypi.python.org/pypi/pisa/ |
|:----------|:----------------------------------|

```
$: cd /tmp
$: wget http://pypi.python.org/packages/source/p/pisa/pisa-3.0.32.tar.gz#md5=d68f2f76e04b10f73c07ef4df937b243
$: tar -zxf pisa-3.0.32.tar.gz && cd pisa-*
$: sudo python setup.py install
```

## ReportLab & HTML5 lib ##

```
$: sudo apt-get install python-reportlab python-html5lib
```

# Installing django-report #

```
svn co http://django-report.googlecode.com/svn/trunk/ report
```

Edit your `settings.py` file and add the following lines:

```

REPORT_CONF = {
    'content_type':         u'application/pdf',
    'temp_path':            u'/tmp',
    'base_title':           u'Report: ',
    'toolbar_back_txt':     u'&laquo; Back',
    'toolbar_download_txt': u'Download to PDF',
    'title':                u"Untitled report",
}

```

Add `report` to `INSTALLED_APPS` and `report.middleware.DownloadToPDF` to `MIDDLEWARE_CLASSES`.

Finally add report to your URLs:

```
urlpatterns = patterns('',
    (r'^report/',    include('report.urls')),
    (r'^admin/(.*)', admin_site.root),
)
```