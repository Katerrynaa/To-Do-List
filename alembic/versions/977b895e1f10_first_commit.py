"""first commit

Revision ID: 977b895e1f10
Revises: 
Create Date: 2024-04-26 14:04:25.091535

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '977b895e1f10'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "todo",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=100), nullable=True),
        sa.Column("description", sa.String(length=300), nullable=True),
        sa.Column("is_completed", sa.Boolean, default=False),
        sa.PrimaryKeyConstraint("id"),
)
    op.create_index(op.f("ix_todo"), "todo", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index(op.f("ix_todo_id"), table_name="todo")
    op.drop_table("todo")
