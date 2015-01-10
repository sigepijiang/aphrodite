"""init

Revision ID: 4d688824c7ff
Revises: None
Create Date: 2015-01-10 15:46:09.678382

"""

# revision identifiers, used by Alembic.
revision = '4d688824c7ff'
down_revision = None

from datetime import datetime

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'image',
        sa.Column('hashkey', sa.CHAR(32), primary_key=True),
        sa.Column('height', sa.Integer(), nullable=False),
        sa.Column('width', sa.Integer(), nullable=False),
        sa.Column('suffix', sa.String(8), nullable=False),
        sa.Column(
            'date_created', sa.DateTime(), default=datetime.now,
            server_default=sa.func.now(),
        ),
    )


def downgrade():
    op.drop_table('image')
