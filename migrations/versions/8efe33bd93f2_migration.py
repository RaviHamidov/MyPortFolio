"""migration

Revision ID: 8efe33bd93f2
Revises: 1b4b1e0f5501
Create Date: 2021-12-20 15:15:54.870624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8efe33bd93f2'
down_revision = '1b4b1e0f5501'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('testimonials', 'test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('testimonials', sa.Column('test', sa.VARCHAR(length=100), nullable=True))
    # ### end Alembic commands ###
