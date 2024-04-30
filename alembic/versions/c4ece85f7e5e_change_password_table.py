"""change password table

Revision ID: c4ece85f7e5e
Revises: 9319c6296cba
Create Date: 2024-04-30 12:40:54.549779

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'c4ece85f7e5e'
down_revision: Union[str, None] = '9319c6296cba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.String(length=255),
               type_=mysql.INTEGER(),
               existing_nullable=True)
    # ### end Alembic commands ###