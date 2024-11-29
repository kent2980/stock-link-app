"""ix head add cloumn

Revision ID: 9a7ec44dd0d1
Revises: 86a6fe74191e
Create Date: 2024-11-29 19:39:21.212069

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes


# revision identifiers, used by Alembic.
revision = '9a7ec44dd0d1'
down_revision = '86a6fe74191e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ix_head_title', sa.Column('is_consolidated', sa.Boolean(), nullable=True))
    op.create_index('idx_ix_head_title_is_consolidated', 'ix_head_title', ['is_consolidated'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_ix_head_title_is_consolidated', table_name='ix_head_title')
    op.drop_column('ix_head_title', 'is_consolidated')
    # ### end Alembic commands ###
