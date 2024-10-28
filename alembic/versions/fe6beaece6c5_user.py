"""user

Revision ID: fe6beaece6c5
Revises: 
Create Date: 2024-10-28 15:58:31.780702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from faker import Faker


# revision identifiers, used by Alembic.
revision: str = 'fe6beaece6c5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    fake= Faker(['id_ID', 'de_DE'])
    users = op.create_table(
        'users',
        sa.Column('id', sa.BigInteger, primary_key=True, index=True),
        sa.Column('name', sa.String(500), index=True, nullable=True),
        sa.Column('gender', sa.String(500), nullable=True, index=True),
    )

    # insert data by seed
    for x in range(100):
        op.bulk_insert(users, [
            {
                'name': fake.name_male(),
                'gender': fake.passport_gender()
            }
        ])

def downgrade() -> None:
    op.drop_table('users')
