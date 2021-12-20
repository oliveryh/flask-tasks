"""added password to users

Revision ID: 6863fc4068d2
Revises: ee400f3e53d4
Create Date: 2020-02-24 21:00:33.010434

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6863fc4068d2'
down_revision = 'ee400f3e53d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###
