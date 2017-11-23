import urllib
from urllib import request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        res = urllib.request.urlopen(url)
        if res.getcode() != 200:
            return None
        return res.read()
