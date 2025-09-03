"""Create Table Posts

Revision ID: b12106155be5
Revises: 282f92816682
Create Date: 2025-09-02 23:46:50.110320

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b12106155be5'
down_revision: Union[str, Sequence[str], None] = '282f92816682'
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
