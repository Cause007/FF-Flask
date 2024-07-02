"""empty message

Revision ID: b9a30538f583
Revises: 
Create Date: 2024-05-17 15:16:13.323988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9a30538f583'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('FirstName', sa.String(length=150), nullable=True),
    sa.Column('LastName', sa.String(length=150), nullable=True),
    sa.Column('Email', sa.String(length=150), nullable=False),
    sa.Column('Password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('employee',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('FirstName', sa.String(length=100), nullable=False),
    sa.Column('LastName', sa.String(length=100), nullable=False),
    sa.Column('Position', sa.String(length=150), nullable=True),
    sa.Column('Phone', sa.String(length=20), nullable=True),
    sa.Column('Email', sa.String(length=100), nullable=True),
    sa.Column('Address', sa.String(length=150), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('FirstName', sa.String(length=100), nullable=False),
    sa.Column('LastName', sa.String(length=100), nullable=False),
    sa.Column('Photo', sa.UUID(), nullable=True),
    sa.Column('Parent1', sa.String(length=100), nullable=False),
    sa.Column('Parent2', sa.String(length=100), nullable=True),
    sa.Column('Phone1', sa.String(length=100), nullable=True),
    sa.Column('Phone2', sa.String(length=100), nullable=True),
    sa.Column('Email1', sa.String(length=100), nullable=True),
    sa.Column('Email2', sa.String(length=100), nullable=True),
    sa.Column('Address1', sa.String(length=100), nullable=True),
    sa.Column('Address2', sa.String(length=100), nullable=True),
    sa.Column('City_ST_Zip1', sa.String(length=100), nullable=True),
    sa.Column('City_ST_Zip2', sa.String(length=100), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('employee')
    op.drop_table('user')
    # ### end Alembic commands ###
