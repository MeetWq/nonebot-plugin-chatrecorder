"""msg_type

Revision ID: 9bca28bcb998
Revises: 7228a3a08576
Create Date: 2023-03-06 14:04:44.325356

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "9bca28bcb998"
down_revision = "7228a3a08576"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(
        "nonebot_plugin_chatrecorder_messagerecord", schema=None
    ) as batch_op:
        batch_op.alter_column(
            "message",
            existing_type=sa.String(255),
            type_=sa.JSON(),
            existing_nullable=False,
            postgresql_using="message::json",
        )
        batch_op.alter_column(
            "plain_text",
            existing_type=sa.String(255),
            type_=sa.TEXT(),
            existing_nullable=False,
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table(
        "nonebot_plugin_chatrecorder_messagerecord", schema=None
    ) as batch_op:
        batch_op.alter_column(
            "plain_text",
            existing_type=sa.TEXT(),
            type_=sa.String(255),
            existing_nullable=False,
        )
        batch_op.alter_column(
            "message",
            existing_type=sa.JSON(),
            type_=sa.String(255),
            existing_nullable=False,
        )

    # ### end Alembic commands ###
