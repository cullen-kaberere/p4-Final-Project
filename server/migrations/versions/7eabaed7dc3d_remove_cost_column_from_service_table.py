"""Remove cost column from Service table

Revision ID: 7eabaed7dc3d
Revises: 339900a9f0bc
Create Date: 2025-01-30 07:56:01.407133

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7eabaed7dc3d'
down_revision = '339900a9f0bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.drop_column('cost')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('services', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cost', sa.FLOAT(), nullable=False))

    # ### end Alembic commands ###
