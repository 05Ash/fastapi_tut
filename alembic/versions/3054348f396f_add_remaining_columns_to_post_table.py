"""add remaining columns to post table

Revision ID: 3054348f396f
Revises: ba1b958e7e18
Create Date: 2025-09-03 00:06:57.008545

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3054348f396f'
down_revision: Union[str, Sequence[str], None] = 'ba1b958e7e18'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("posts", sa.Column("published", sa.Boolean(),
                                     server_default="TRUE", nullable = False))
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone = True),
                                     server_default=sa.text("NOW()"), nullable = False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("posts", "created_at")
    op.drop_column("posts", "published")
    pass
