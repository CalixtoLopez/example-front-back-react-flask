"""empty message

Revision ID: c0d1d088e73e
Revises: d4ef3547a228
Create Date: 2021-08-28 17:11:41.044795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0d1d088e73e'
down_revision = 'd4ef3547a228'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), nullable=False),
    sa.Column('money', sa.Numeric(), nullable=False),
    sa.Column('_password', sa.VARCHAR(), nullable=False),
    sa.Column('_is_active', sa.Boolean(), nullable=False, default = True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('account')
    # ### end Alembic commands ###
