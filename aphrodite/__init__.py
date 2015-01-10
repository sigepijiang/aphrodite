#-*- coding: utf-8 -*-

from share.framework.bottle import Avalon

# push the app into the stack FIRST!
app = Avalon(__name__)

from .views import bp_aphrodite
app.register_blueprint(bp_aphrodite)

from .apis import bp_apis
app.register_blueprint(bp_apis)
