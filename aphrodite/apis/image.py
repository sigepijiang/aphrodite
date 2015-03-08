# -*- coding: utf-8 -*-
import json
from hashlib import md5

from bottle import request
from qiniu import Auth, put_data

from share.framework.bottle.restful import RESTfulOpenAPI
from share.framework.bottle.engines import db
from share.framework.bottle.restful.validator import resful_validator

from aphrodite import app
from aphrodite.models import ImageModel

QINIU_ACCESS_KEY = app.config['qiniu_access_key']
QINIU_SECRET_KEY = app.config['qiniu_secret_key']
QINIU_BUCKET_NAME = app.config['qiniu_bucket_name']


class ImageAPI(RESTfulOpenAPI):
    path = '/image'
    methods = ['POST']

    def create(self):
        # TODO: 表单验证
        image = request.files['image']
        # TODO: 解包检查
        origin_name, suffix = image.raw_filename.split('.')

        data = image.file.read()
        data_hash = md5(data).hexdigest()
        key = data_hash + '.' + suffix

        model = ImageModel.query.get(data_hash)
        if model:
            return model.as_dict()

        auth = Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
        token = auth.upload_token(
            QINIU_BUCKET_NAME, None, 7200,
            {
                'returnBody': json.dumps({
                    'key': '$(key)',
                    'hash': '$(etag)',
                    'format': '$(imageInfo.format)',
                    'width': '$(imageInfo.width)',
                    'height': '$(imageInfo.height)',
                }),
                'save_key': '$(etag)',
            }
        )
        ret, info = put_data(token, key, data)
        model = ImageModel(
            hashkey=data_hash, suffix=suffix,
            width=ret['width'], height=ret['height'])
        db.session.add(model)
        db.session.commit()
        return model.as_dict()
