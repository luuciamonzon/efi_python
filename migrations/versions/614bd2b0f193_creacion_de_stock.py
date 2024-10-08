"""Creacion de stock

Revision ID: 614bd2b0f193
Revises: 3bcfb1ae3dfc
Create Date: 2024-08-11 18:59:44.525730

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '614bd2b0f193'
down_revision = '3bcfb1ae3dfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('equipo_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['equipo_id'], ['equipo.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    # ### end Alembic commands ###
