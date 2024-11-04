"""posts table

Revision ID: 4410ab7ab2a1
Revises: d032b4f6756b
Create Date: 2024-09-19 19:21:53.678601

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4410ab7ab2a1'
down_revision = 'd032b4f6756b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    # ### end Alembic commands ###
