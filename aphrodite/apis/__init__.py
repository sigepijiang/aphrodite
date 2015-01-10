# -*- coding: utf-8 -*-

from share.framework.bottle import APIBlueprint

from .image import ImageAPI


bp_apis = APIBlueprint('apis')
ImageAPI.attach_to(bp_apis)
