import os, re 
import ho.pisa as pisa
from django.conf import settings
import tempfile


def tmpfile(max_size=131072, dir=None, pre="tmp_", suf=".pdf"):
    if dir is None:
        dir = tempfile.gettempdir()
    try:
        file = tempfile.SpooledTemporaryFile(max_size=max_size, dir=dir, prefix=pre, suffix=suf)
    except:
        print "Error: can't created temporary file"

    return file


def fetch_resources(uri, rel):
    """
    Callback to allow pisa/reportlab to retrieve Images,Stylesheets, etc.
    `uri` is the href attribute from the html link element.
    `rel` gives a relative path, but it's not used here.

    """
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    print path
    return path

import sys

class DownloadToPDF():
    """
    download requested apge to DPF
    """
    def __init__(self):
        self.temp_file    = os.path.join(settings.REPORT_CONF['temp_path'], 'temp.pdf')
        self.temp_file2   = os.path.join(settings.REPORT_CONF['temp_path'], 'temp2.pdf')
       
    def process_response(self, request, response):
        print response.status_code
        if ("pdf" in request.GET 
            and "text" in response['Content-Type'] 
            and response.status_code == 200):
            fd  = open(self.temp_file, 'wb')
            pisa.showLogging()
            pdf = pisa.pisaDocument(
                response.content,   # src
                fd,                 # dest
#               debug=0,
#               path=None,
#               errout=sys.stdout
#               tempdir=None,
                format='pdf',
                link_callback=fetch_resources,
#               default_css=None,
                xhtml=True,
#               encoding='iso-8859-1',
#               xml_output=fd,
            )
            
            fd.close()
            if not pdf.err:
                response['Content-Type'] = u'%s; %s' % (settings.REPORT_CONF['content_type'], settings.REPORT_CONF['encoding'], )
                fd = open(self.temp_file, 'r')
                rs = fd.read()
                fd.close
                response.content = rs
            return response
        else:
            return response

