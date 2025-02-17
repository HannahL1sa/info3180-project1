"""empty message

Revision ID: 6f5c1a2a3b49
Revises: 
Create Date: 2022-03-20 02:43:12.663053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f5c1a2a3b49'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_properties',
    sa.Column('property_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('num_bedrooms', sa.Integer(), nullable=True),
    sa.Column('num_bathrooms', sa.Integer(), nullable=True),
    sa.Column('location', sa.String(length=100), nullable=True),
    sa.Column('price', sa.String(length=80), nullable=True),
    sa.Column('property_type', sa.String(length=80), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('property_photo', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('property_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_properties')
    # ### end Alembic commands ###
