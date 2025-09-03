"""empty message

Revision ID: 282f92816682
Revises:
Create Date: 2025-09-02 23:29:24.018099

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '282f92816682'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
                    "posts",
                    sa.Column("id", sa.Integer(), nullable = False, primary_key = True),
                    sa.Column("title", sa.String(), nullable = False)
                    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("posts")
    pass
