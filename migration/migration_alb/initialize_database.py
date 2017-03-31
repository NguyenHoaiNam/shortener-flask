"""initialize database

Revision ID: b3c3f2e438c5
Revises:
Create Date: 2017-03-30 15:14:59.067419

"""
from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'urls',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('org_link', sa.String(length=255), nullable=True),
        sa.Column('short_link', sa.String(length=200), nullable=True)
    )
