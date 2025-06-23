"""Add new fields for eggplant data

Revision ID: 75253c59959d
Revises: cd1ed2244844
Create Date: 2025-06-23 07:31:07.318408
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "75253c59959d"
down_revision: Union[str, Sequence[str], None] = "cd1ed2244844"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column("researchentry", sa.Column("title", sa.String(), nullable=True))
    op.add_column(
        "researchentry", sa.Column("project_summary", sa.String(), nullable=True)
    )
    op.add_column("researchentry", sa.Column("time_period", sa.String(), nullable=True))
    op.add_column(
        "researchentry", sa.Column("thesis_advisor_name", sa.String(), nullable=True)
    )
    op.add_column(
        "researchentry", sa.Column("thesis_advisor_email", sa.String(), nullable=True)
    )
    op.add_column(
        "researchentry", sa.Column("thesis_advisor_phone", sa.String(), nullable=True)
    )
    op.add_column(
        "researchentry", sa.Column("postal_address", sa.String(), nullable=True)
    )
    op.add_column(
        "researchentry", sa.Column("department_and_faculty", sa.String(), nullable=True)
    )
    op.add_column("researchentry", sa.Column("orcid", sa.String(), nullable=True))

    # Optionally set a default value if needed to enforce NOT NULL afterward
    op.execute(
        "UPDATE researchentry SET title = 'Untitled Project' WHERE title IS NULL"
    )
    op.execute(
        "UPDATE researchentry SET project_summary = '' WHERE project_summary IS NULL"
    )
    op.execute(
        "UPDATE researchentry SET time_period = 'Unknown' WHERE time_period IS NULL"
    )
    op.execute(
        "UPDATE researchentry SET thesis_advisor_name = 'Unknown' WHERE thesis_advisor_name IS NULL"
    )
    op.execute(
        "UPDATE researchentry SET thesis_advisor_email = 'unknown@example.com' WHERE thesis_advisor_email IS NULL"
    )
    op.execute(
        "UPDATE researchentry SET thesis_advisor_phone = '000-000-0000' WHERE thesis_advisor_phone IS NULL"
    )
    op.execute(
        "UPDATE researchentry SET postal_address = 'Not Provided' WHERE postal_address IS NULL"
    )
    op.execute(
        "UPDATE researchentry SET department_and_faculty = 'Unknown' WHERE department_and_faculty IS NULL"
    )
    op.execute(
        "UPDATE researchentry SET orcid = '0000-0000-0000-0000' WHERE orcid IS NULL"
    )

    # Now enforce NOT NULL constraint
    op.alter_column("researchentry", "title", nullable=False)
    op.alter_column("researchentry", "project_summary", nullable=False)
    op.alter_column("researchentry", "time_period", nullable=False)
    op.alter_column("researchentry", "thesis_advisor_name", nullable=False)
    op.alter_column("researchentry", "thesis_advisor_email", nullable=False)
    op.alter_column("researchentry", "thesis_advisor_phone", nullable=False)
    op.alter_column("researchentry", "postal_address", nullable=False)
    op.alter_column("researchentry", "department_and_faculty", nullable=False)
    op.alter_column("researchentry", "orcid", nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("researchentry", "orcid")
    op.drop_column("researchentry", "department_and_faculty")
    op.drop_column("researchentry", "postal_address")
    op.drop_column("researchentry", "thesis_advisor_phone")
    op.drop_column("researchentry", "thesis_advisor_email")
    op.drop_column("researchentry", "thesis_advisor_name")
    op.drop_column("researchentry", "time_period")
    op.drop_column("researchentry", "project_summary")
    op.drop_column("researchentry", "title")
