"""added title column to posts

Revision ID: 9b0ef55bd932
Revises: 09f4e478ad20
Create Date: 2019-01-25 14:56:23.017027

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9b0ef55bd932'
down_revision = '09f4e478ad20'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('title', sa.String(length=100), nullable=True))
    op.alter_column('post', 'body',
               existing_type=mysql.VARCHAR(length=400),
               type_=sa.String(length=1000),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'body',
               existing_type=sa.String(length=1000),
               type_=mysql.VARCHAR(length=400),
               existing_nullable=True)
    op.drop_column('post', 'title')
    # ### end Alembic commands ###
