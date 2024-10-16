"""revised data inside plant model

Revision ID: b64349277e77
Revises: ad28fa6e985f
Create Date: 2024-10-10 12:49:04.090602

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b64349277e77'
down_revision = 'ad28fa6e985f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('plants', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('plants', 'image',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('plants', 'price',
               existing_type=sa.FLOAT(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('plants', 'price',
               existing_type=sa.FLOAT(),
               nullable=False)
    op.alter_column('plants', 'image',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('plants', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
