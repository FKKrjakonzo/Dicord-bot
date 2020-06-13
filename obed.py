#!/usr/bin/python
# -*- coding: utf-8 -*-

from requests import post
from json import loads
from boilerpy3 import extractors

headers = {'Accept': 'application/json', 'user_key': 'xxxxx'}


# https://developers.zomato.com/documentation?lang=sk#/
# Cool documentation

def zomato(id):
    obed_list = ''
    r = \
        post(url='https://developers.zomato.com/api/v2.1/dailymenu?res_id={}'.format(id),
             headers=headers)
    connection = loads(r.text)
    try:
        for i in connection['daily_menus'][0]['daily_menu']['dishes']:
            obed_list += '{} {} \n'.format(i['dish']['name'], i['dish'
                    ]['price'])
    except IndexError:
        obed_list = 'Nic'
    return obed_list


def velorex():
    extractor = extractors.KeepEverythingExtractor()
    content = \
        extractor.get_content_from_url('http://www.restauracevelorex.cz/poledni-menu/'
            )
    try:
        return content.split('(doba p\xc5\x99\xc3\xadpravy m\xc5\xaf\xc5\xbee b\xc3\xbdt v\xc2\xa0dob\xc4\x9b ob\xc4\x9bd\xc5\xaf 20 -30 minut, d\xc4\x9bkujeme za pochopen\xc3\xad)'
                             )[1].split('Podle z\xc3\xa1kona o evidenci tr\xc5\xbeeb je prod\xc3\xa1vaj\xc3\xadc\xc3\xad povinen vystavit kupuj\xc3\xadc\xc3\xadmu \xc3\xba\xc4\x8dtenku.'
                )[0]
    except IndexError:
        return 'Nic tu nie je'


def get_obed():
    return ['U Kotelny - \n {}'.format(zomato(16506016)),
            'Portoriko - \n {}'.format(zomato(16506862)),
            'Velorex - \n {}'.format(velorex())]
