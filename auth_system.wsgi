#!/usr/bin/python

"""
author : Vinay Kumar Kuresi
created Date : 03/12/2023

"""

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/auth_system/")

from settings import config
from auth_system import app as application
application.secret_key = config.SECRET_KEY
