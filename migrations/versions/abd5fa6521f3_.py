"""empty message

Revision ID: abd5fa6521f3
Revises: c5502219492d
Create Date: 2023-11-10 16:25:18.035060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abd5fa6521f3'
down_revision = 'c5502219492d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feature',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('url', sa.String(length=300), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('level', sa.String(length=2), nullable=True),
    sa.Column('classes', sa.String(length=100), nullable=True),
    sa.Column('desc', sa.String(), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feature')
    # ### end Alembic commands ###
