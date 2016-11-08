# -*- coding:utf-8 -*-

from datetime import datetime, timedelta

from pymongo import DESCENDING, ASCENDING

from models.dc import model as dc_model

from helpers import settings


MODEL_SLOTS = ['Dc']


class Dc(dc_model.Dc):
    pass
