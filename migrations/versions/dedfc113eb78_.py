"""empty message

Revision ID: dedfc113eb78
Revises: d9ddebf75e32
Create Date: 2022-08-16 21:08:04.711491

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'dedfc113eb78'
down_revision = 'd9ddebf75e32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_post_timestamp', table_name='post')
    op.drop_table('post')
    op.drop_column('resource', 'creator')
    op.drop_constraint('resource_to_user_user_id_fkey', 'resource_to_user', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('resource_to_user_user_id_fkey', 'resource_to_user', 'user', ['user_id'], ['id'])
    op.add_column('resource', sa.Column('creator', sa.VARCHAR(length=140), autoincrement=False, nullable=True))
    op.create_table('post',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('body', sa.VARCHAR(length=140), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='post_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='post_pkey')
    )
    op.create_index('ix_post_timestamp', 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###
