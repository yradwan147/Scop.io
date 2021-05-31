"""empty message

Revision ID: 4a7815ebdc10
Revises: 
Create Date: 2021-05-24 01:18:21.402171

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a7815ebdc10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authors', sa.Column('coauthor7', sa.String(), nullable=True))
    op.add_column('authors', sa.Column('coauthor8', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authors', 'coauthor8')
    op.drop_column('authors', 'coauthor7')
    # ### end Alembic commands ###