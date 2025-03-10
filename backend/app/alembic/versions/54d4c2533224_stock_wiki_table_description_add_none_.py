"""stock_wiki table description add None by kent

Revision ID: 54d4c2533224
Revises: 0a3884e17235
Create Date: 2025-02-14 20:48:35.692420

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '54d4c2533224'
down_revision = '0a3884e17235'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stock_wiki', 'description',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('stock_wiki', 'description',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###
