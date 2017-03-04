# -*- coding: utf-8 -*-
from __future__ import absolute_import, division
import string
import config
from time import gmtime, strftime
from random import SystemRandom as SR


def rand():
    """
    Generate random string to be url path
    """
    return ''.join(SR().choice(string.ascii_letters + string.digits)
                   for _ in range(config.RAND_DIR_LENGTH))


def time():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())
