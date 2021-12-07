"""add content column to post table

Revision ID: 824ea1c1bdcf
Revises: 9ff22ed6d7e4
Create Date: 2021-12-07 20:03:16.500060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '824ea1c1bdcf'
down_revision = '9ff22ed6d7e4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
