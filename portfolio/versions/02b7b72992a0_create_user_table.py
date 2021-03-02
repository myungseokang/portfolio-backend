"""create user table

Revision ID: 02b7b72992a0
Revises: 
Create Date: 2021-03-01 06:13:34.712691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '02b7b72992a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('email', sa.String(127), unique=True, index=True),
        sa.Column('password', sa.String(255)),
    )


def downgrade():
    op.drop_table('users')
