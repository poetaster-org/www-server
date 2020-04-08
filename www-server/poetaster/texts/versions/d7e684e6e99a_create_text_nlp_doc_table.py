"""create text nlp doc table

Revision ID: d7e684e6e99a
Revises: ac13307b2ddd
Create Date: 2020-02-20 13:14:34.528421

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'd7e684e6e99a'
down_revision = 'ac13307b2ddd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('texts_TextNLPDoc',
    sa.Column('version', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('value', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('text_slug', sa.String(), nullable=True),
    sa.Column('text_version', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['text_slug', 'text_version'], ['texts_Text.slug', 'texts_Text.version'], ),
    sa.PrimaryKeyConstraint('id', 'version')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('texts_TextNLPDoc')
    # ### end Alembic commands ###