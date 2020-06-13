#!/usr/bin/python
# -*- coding: utf-8 -*-

import imaplib
import email
from email.header import decode_header, make_header


class Mailer:

    def __init__(self):
        self.mail = imaplib.IMAP4_SSL('server')
        self.mail.login('mail', 'password')
        self.mail.select('inbox')

    def search_for_unseen(self):
        mails = []
        (result, data) = self.mail.search(None, '(UNSEEN)')
        if result == 'OK':
            id_list = data[0].split()
            for i in id_list:
                mails.append(self.process(i))
        return mails

    def process(self, i):
        (result, data) = self.mail.fetch(i.decode('utf-8'), '(RFC822)')
        if result == 'OK':
            for response_part in data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])
                    return str(make_header(decode_header(msg['subject'
                               ])))
