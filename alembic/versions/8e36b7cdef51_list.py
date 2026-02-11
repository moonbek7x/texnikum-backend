"""list

Revision ID: 8e36b7cdef51
Revises: 582f1dee81fb
Create Date: 2026-02-11 19:24:09.502065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8e36b7cdef51'
down_revision: Union[str, Sequence[str], None] = '582f1dee81fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        ALTER TABLE deficiencies
        ALTER COLUMN photo TYPE JSON
        USING CASE
            WHEN photo IS NULL THEN NULL
            ELSE json_build_array(photo)
        END;
    """)

    op.execute("""
        ALTER TABLE news
        ALTER COLUMN photo TYPE JSON
        USING CASE
            WHEN photo IS NULL THEN NULL
            ELSE json_build_array(photo)
        END;
    """)

    op.execute("""
        ALTER TABLE teachers
        ALTER COLUMN photo TYPE JSON
        USING CASE
            WHEN photo IS NULL THEN NULL
            ELSE json_build_array(photo)
        END;
    """)


def downgrade() -> None:
    op.execute("""
        ALTER TABLE teachers
        ALTER COLUMN photo TYPE VARCHAR(255)
        USING photo->>0;
    """)

    op.execute("""
        ALTER TABLE news
        ALTER COLUMN photo TYPE VARCHAR(255)
        USING photo->>0;
    """)

    op.execute("""
        ALTER TABLE deficiencies
        ALTER COLUMN photo TYPE VARCHAR(255)
        USING photo->>0;
    """)

