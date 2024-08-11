"""Creacion de equipos

Revision ID: 3bcfb1ae3dfc
Revises: 
Create Date: 2024-08-11 17:53:13.610187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bcfb1ae3dfc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marca',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('proveedor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('nro_telefono', sa.String(length=20), nullable=False),
    sa.Column('direccion', sa.String(length=50), nullable=True),
    sa.Column('cuit', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reclamos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('nro_telefono', sa.String(length=20), nullable=False),
    sa.Column('direccion', sa.String(length=50), nullable=False),
    sa.Column('reclamo', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('equipo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('modelo', sa.String(length=50), nullable=False),
    sa.Column('precio', sa.Integer(), nullable=True),
    sa.Column('anio_de_fabricacion', sa.Integer(), nullable=True),
    sa.Column('caracteristicas', sa.String(length=4000), nullable=True),
    sa.Column('marca_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['marca_id'], ['marca.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('equipo')
    op.drop_table('reclamo')
    op.drop_table('proveedor')
    op.drop_table('marca')
    # ### end Alembic commands ###
