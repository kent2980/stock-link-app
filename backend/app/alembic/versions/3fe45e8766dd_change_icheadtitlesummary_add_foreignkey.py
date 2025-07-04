"""Change IcHeadTitleSummary Add ForeignKey

Revision ID: 3fe45e8766dd
Revises: 0e8fc85dff6e
Create Date: 2025-06-13 23:09:15.517196

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '3fe45e8766dd'
down_revision = '0e8fc85dff6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'ix_head_title_summary', 'ix_head_title', ['head_item_key'], ['item_key'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ix_head_title_summary', type_='foreignkey')
    # ### end Alembic commands ###
