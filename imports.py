import discord 
from discord.ext import commands, tasks
from discord.ext.commands import *
from discord.utils import *

import google_auth_oauthlib.flow
import googleapiclient.discovery
from googleapiclient.discovery import build
import googleapiclient.errors

from itertools import cycle

import re
import random
import sys
import os
import time


from notatoken import *

"""
pip install google-api-python-client==1.12.8
pip3 install google-auth-oauthlib google-auth-httplib2

"""