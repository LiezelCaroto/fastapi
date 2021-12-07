"""add FK to posts table

Revision ID: 6793236e46f2
Revises: 35ba9d55204b
Create Date: 2021-12-07 20:16:22.963375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6793236e46f2'
down_revision = '35ba9d55204b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'],
                          remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
