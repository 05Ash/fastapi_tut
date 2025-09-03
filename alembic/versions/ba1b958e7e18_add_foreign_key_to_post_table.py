"""add foreign key to post table

Revision ID: ba1b958e7e18
Revises: caabc66f60b3
Create Date: 2025-09-03 00:01:07.053261

"""
from tkinter import CASCADE
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ba1b958e7e18'
down_revision: Union[str, Sequence[str], None] = 'caabc66f60b3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts",
                  sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk",
                          source_table="posts",
                          referent_table="users",
                          local_cols=["owner_id"],
                          remote_cols=["id"],
                          ondelete="CASCADE"
                          )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("posts_users_fk", "posts")
    op.drop_column("posts", "owner_id")
    pass
