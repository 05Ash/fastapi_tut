"""add remaining to posts table

Revision ID: 7e09088551ea
Revises: b12106155be5
Create Date: 2025-09-02 23:48:45.938972

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7e09088551ea'
down_revision: Union[str, Sequence[str], None] = 'b12106155be5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
                    "posts",
                    sa.Column("content", sa.String(), nullable = False)
                    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "content")
    pass
