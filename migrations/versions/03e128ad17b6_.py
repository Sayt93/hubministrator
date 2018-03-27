"""empty message

Revision ID: 03e128ad17b6
Revises: 
Create Date: 2018-03-26 12:53:57.885318

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03e128ad17b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id_usr', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('is_providers', sa.Boolean(), nullable=True),
    sa.Column('is_resident', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id_usr')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('validations',
    sa.Column('id_chd', sa.Integer(), nullable=False),
    sa.Column('val_flag', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id_chd')
    )
    op.create_table('administrators_registry',
    sa.Column('id_admin', sa.Integer(), nullable=False),
    sa.Column('license_n', sa.String(length=20), nullable=False),
    sa.Column('p_iva', sa.String(length=13), nullable=False),
    sa.Column('condo_own_n', sa.Integer(), nullable=False),
    sa.Column('id_usr', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_usr'], ['users.id_usr'], ),
    sa.PrimaryKeyConstraint('id_admin')
    )
    op.create_table('providers_registry',
    sa.Column('id_provider', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=40), nullable=False),
    sa.Column('pi_cf', sa.String(length=16), nullable=False),
    sa.Column('city', sa.String(length=40), nullable=False),
    sa.Column('district', sa.String(length=40), nullable=False),
    sa.Column('manager', sa.String(length=30), nullable=True),
    sa.Column('phone_home', sa.String(length=20), nullable=False),
    sa.Column('phone_mobile', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('site', sa.String(length=40), nullable=True),
    sa.Column('category', sa.Integer(), nullable=False),
    sa.Column('id_usr', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_usr'], ['users.id_usr'], ),
    sa.PrimaryKeyConstraint('id_provider')
    )
    op.create_table('residents_registry',
    sa.Column('id_resident', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('surname', sa.String(length=40), nullable=False),
    sa.Column('cf', sa.String(length=16), nullable=False),
    sa.Column('sex', sa.Boolean(), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=False),
    sa.Column('birthplace', sa.String(length=20), nullable=False),
    sa.Column('identity_card', sa.String(length=8), nullable=False),
    sa.Column('address', sa.String(length=40), nullable=False),
    sa.Column('residence', sa.String(length=40), nullable=False),
    sa.Column('phone_home', sa.String(length=20), nullable=False),
    sa.Column('phone_mobile', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=40), nullable=False),
    sa.Column('flat', sa.String(length=2), nullable=False),
    sa.Column('thousandths', sa.Float(), nullable=False),
    sa.Column('id_usr', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_usr'], ['users.id_usr'], ),
    sa.PrimaryKeyConstraint('id_resident')
    )
    op.create_table('condos',
    sa.Column('id_condo', sa.Integer(), nullable=False),
    sa.Column('condo_name', sa.String(length=30), nullable=False),
    sa.Column('id_admin', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_admin'], ['administrators_registry.id_admin'], ),
    sa.PrimaryKeyConstraint('id_condo')
    )
    op.create_table('providers_category',
    sa.Column('boiler', sa.Integer(), nullable=False),
    sa.Column('lifter', sa.Integer(), nullable=False),
    sa.Column('extinguisher', sa.Integer(), nullable=False),
    sa.Column('gas', sa.Integer(), nullable=False),
    sa.Column('light', sa.Integer(), nullable=False),
    sa.Column('cleaning', sa.Integer(), nullable=False),
    sa.Column('electrician', sa.Integer(), nullable=False),
    sa.Column('plumber', sa.Integer(), nullable=False),
    sa.Column('lawyer', sa.Integer(), nullable=False),
    sa.Column('achitect', sa.Integer(), nullable=False),
    sa.Column('antenna', sa.Integer(), nullable=False),
    sa.Column('sewer', sa.Integer(), nullable=False),
    sa.Column('business_consultant', sa.Integer(), nullable=False),
    sa.Column('exterminator', sa.Integer(), nullable=False),
    sa.Column('bricklayer', sa.Integer(), nullable=False),
    sa.Column('gardeners', sa.Integer(), nullable=False),
    sa.Column('id_provider', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_provider'], ['providers_registry.id_provider'], ),
    sa.PrimaryKeyConstraint('id_provider')
    )
    op.create_table('condos_data',
    sa.Column('condo_name', sa.String(length=30), nullable=True),
    sa.Column('condo_age', sa.Date(), nullable=False),
    sa.Column('cf_c', sa.String(length=16), nullable=False),
    sa.Column('city', sa.String(length=20), nullable=False),
    sa.Column('district', sa.String(length=20), nullable=False),
    sa.Column('address', sa.String(length=30), nullable=False),
    sa.Column('house_n', sa.Integer(), nullable=True),
    sa.Column('condo_n', sa.Integer(), nullable=True),
    sa.Column('stair_n', sa.Integer(), nullable=True),
    sa.Column('flat_n', sa.Integer(), nullable=True),
    sa.Column('cap', sa.Integer(), nullable=True),
    sa.Column('id_condo', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_condo'], ['condos.id_condo'], ),
    sa.PrimaryKeyConstraint('id_condo')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('condos_data')
    op.drop_table('providers_category')
    op.drop_table('condos')
    op.drop_table('residents_registry')
    op.drop_table('providers_registry')
    op.drop_table('administrators_registry')
    op.drop_table('validations')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
