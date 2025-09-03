"""add users table

Revision ID: caabc66f60b3
Revises: 7e09088551ea
Create Date: 2025-09-02 23:53:19.552324

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'caabc66f60b3'
down_revision: Union[str, Sequence[str], None] = '7e09088551ea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable = False),
                    sa.Column("email", sa.String(), nullable = False),
                    sa.Column("password", sa.String(), nullable = False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('NOW()'), nullable = False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
    pass
