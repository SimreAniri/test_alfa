"""date_update

Revision ID: 04bded3f3a95
Revises: 21b483c7f86d
Create Date: 2024-03-24 23:47:59.171719

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '04bded3f3a95'
down_revision: Union[str, None] = '21b483c7f86d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('table', 'date_update',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('table', 'date_update',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###