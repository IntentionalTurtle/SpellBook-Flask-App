"""empty message

Revision ID: 0c2c9ed5f759
Revises: aa4c5cb81c94
Create Date: 2023-11-10 20:35:36.200310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c2c9ed5f759'
down_revision = 'aa4c5cb81c94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feature', schema=None) as batch_op:
        batch_op.alter_column('level',
               existing_type=sa.VARCHAR(length=2),
               type_=sa.String(length=10),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feature', schema=None) as batch_op:
        batch_op.alter_column('level',
               existing_type=sa.String(length=10),
               type_=sa.VARCHAR(length=2),
               existing_nullable=True)

    # ### end Alembic commands ###