#-*- coding: utf-8 -*-

from datetime import datetime

import sqlalchemy as sa

from share.framework.bottle.engines import db


__all__ = ['ImageModel']


class ImageModel(db.Model, db.TableOpt):
    __tablename__ = 'image'

    hashkey = sa.Column(sa.CHAR(32), primary_key=True)
    suffix = sa.Column(sa.String(8), nullable=False)
    width = sa.Column(sa.Integer(), nullable=False)
    height = sa.Column(sa.Integer(), nullable=False)
    date_created = sa.Column(
        sa.DateTime(), default=datetime.now,
        server_default=sa.func.NOW(),
    )
