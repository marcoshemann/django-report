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

class DownloadToPDF():
    """
    download requested apge to DPF
    """
    def __init__(self):
        self.temp_file    = os.path.join(settings.REPORT_CONF['temp_path'], 'temp.pdf')
       
    def process_response(self, request, response):
        print response.status_code
        if ("pdf" in request.GET 
            and "text" in response['Content-Type'] 
            and response.status_code == 200):
            fd  = open(self.temp_file, 'wb')
            pisa.showLogging()
            pdf = pisa.CreatePDF(response.content, fd, None, fetch_resources, 0, None, None)
            fd.close()
            if not pdf.err:
                response['Content-Type'] = settings.REPORT_CONF['content_type']
                fd = open(self.temp_file, 'r')
                rs = fd.read()
                fd.close
                response.content = rs
            return response
        else:
            return response

