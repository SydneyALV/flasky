"""adds Crystal model

Revision ID: 784ea8e81c6e
Revises: 
Create Date: 2023-04-28 10:03:16.085279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '784ea8e81c6e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('crystal',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('color', sa.String(), nullable=True),
    sa.Column('powers', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('crystal')
    # ### end Alembic commands ###
