"""newton_initial

Revision ID: a0d5cf6bc064
Revises: 
Create Date: 2017-03-31 15:21:21.694950

"""
from alembic import op
import sqlalchemy as sa
from migration.migration_alb import initialize_database


# revision identifiers, used by Alembic.
revision = 'newton'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    initialize_database.upgrade()
