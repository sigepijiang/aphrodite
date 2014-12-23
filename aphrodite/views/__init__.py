#-*- coding: utf-8 -*-

from share.framework.bottle.app import Blueprint

from .upload import UploadView

bp_aphrodite = Blueprint('aphrodite', subdomain='aphrodite')

bp_aphrodite.add_url_rule(
    '/', view_func=UploadView.as_view(), methods=['GET', 'POST'],
    endpoint='upload'
)
