#!python3
#encoding:utf-8
import xmltodict
from collections import OrderedDict
from requests_oauthlib import OAuth1Session
from bs4 import BeautifulSoup
import datetime

CREDENTIALS = {
    'client_key': 'aaaaaaa',
    'client_secret': 'bbbbbbbb',
    'resource_owner_key': 'ccccccccc',
    'resource_owner_secret': 'ddddddddd'
}

class HatenaClient(object):
    ENDPOINT = ('https://blog.hatena.ne.jp/'
                '{user}/{blog}/atom/entry')

    def __init__(self, **args):
        self.set_client(**args)

    def set_client(self, **args):
        self.client = OAuth1Session(**args)

    def get_service(self, user, blog):
        url = self.ENDPOINT.format(user=user, blog=blog)
        res = self.client.get(url)
        self.__check_response(res)
        self.__output_file("{0}.{1}.Services.xml".format(user, blog), res.text)

    def __check_response(self, response):
        if not response.ok:
            response.raise_for_status()
        print('status code: {}'.format(response.status_code))

    def __output_file(self, file_name, content, encoding='utf-8'):
        with open(file_name, mode='w', encoding=encoding) as f:
            f.write(content)


if __name__ == '__main__':
    client = HatenaClient(**CREDENTIALS)
    client.get_service('ytyaru', 'ytyaru.hatenablog.com')

