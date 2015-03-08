#-*- coding: utf-8 -*-

import json
from hashlib import md5

from bottle import request
from qiniu import Auth, put_data

from share.framework.bottle import MethodView, view

from aphrodite import app

QINIU_ACCESS_KEY = app.config['qiniu_access_key']
QINIU_SECRET_KEY = app.config['qiniu_secret_key']
QINIU_BUCKET_NAME = app.config['qiniu_bucket_name']


class UploadView(MethodView):
    @view('upload.html')
    def get(self):
        return {}

    def post(self):
        for i in request.forms.keys():
            print i, request.forms[i], type(request.forms[i])

        for i in request.files.keys():
            print i, request.files[i], type(request.files[i])
            print request.files[i].__dict__

        image = request.files['image']
        name = image.raw_filename
        data = image.file.read()
        key = md5('data').hexdigest() + '.' + name.split('.')[-1]

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
