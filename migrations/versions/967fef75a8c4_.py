"""empty message

Revision ID: 967fef75a8c4
Revises: 815a7ad21224
Create Date: 2020-05-11 13:14:54.472618

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '967fef75a8c4'
down_revision = '815a7ad21224'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('blog', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=False),
    sa.Column('date_posted', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('blogs')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blogs',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('date_posted', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('blog', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='blogs_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='blogs_pkey')
    )
    op.drop_table('comments')
    op.drop_table('blog')
    # ### end Alembic commands ###