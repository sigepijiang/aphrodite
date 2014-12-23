#-*- coding: utf-8 -*-

from share.framework.bottle import MethodView, view


class UploadView(MethodView):
    @view('upload.html')
    def get(self):
        return {}
