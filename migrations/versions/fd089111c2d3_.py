"""empty message

Revision ID: fd089111c2d3
Revises: 
Create Date: 2022-01-31 13:59:17.533993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd089111c2d3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pet',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('bio', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('zipcode', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pet')
    # ### end Alembic commands ###
