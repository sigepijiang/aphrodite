# -*- coding: utf-8 -*-

from share.framework.bottle.restful import RESTfulOpenAPI
from share.framework.bottle.restful.validator import resful_validator

from aphrodite.models import ImageModel
from . import forms


class ImageAPI(RESTfulOpenAPI):
    path = '/image'
    methods = ['GET', 'POST']

    @resful_validator(forms.hashkey)
    def get(self, hashkey):
        image = ImageModel.query.get(hashkey)
        return image.as_dict() if image else {}
