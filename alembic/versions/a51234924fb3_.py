"""empty message

Revision ID: a51234924fb3
Revises: 3fc3638bd0ed
Create Date: 2022-08-30 16:47:43.491187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a51234924fb3'
down_revision = '3fc3638bd0ed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('moderators',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vk_id', sa.BigInteger(), nullable=True),
    sa.Column('steamid', sa.BigInteger(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_moderators_id'), 'moderators', ['id'], unique=False)
    op.create_index(op.f('ix_moderators_steamid'), 'moderators', ['steamid'], unique=False)
    op.create_index(op.f('ix_moderators_vk_id'), 'moderators', ['vk_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_moderators_vk_id'), table_name='moderators')
    op.drop_index(op.f('ix_moderators_steamid'), table_name='moderators')
    op.drop_index(op.f('ix_moderators_id'), table_name='moderators')
    op.drop_table('moderators')
    # ### end Alembic commands ###