"""empty message

Revision ID: 0c3cd09e2891
Revises: d1dd089291f3
Create Date: 2023-11-10 10:22:38.169101

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c3cd09e2891'
down_revision = 'd1dd089291f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(length=5000), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('spell', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
