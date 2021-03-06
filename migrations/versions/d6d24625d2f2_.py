"""empty message

Revision ID: d6d24625d2f2
Revises: e9a7b25e3c62
Create Date: 2019-04-09 14:36:16.766327

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6d24625d2f2'
down_revision = 'e9a7b25e3c62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('eth_contact', sa.Column('last_updated', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True))
    op.add_column('token_transaction', sa.Column('last_updated', sa.DateTime(), server_default=sa.text(u'now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('token_transaction', 'last_updated')
    op.drop_column('eth_contact', 'last_updated')
    # ### end Alembic commands ###
