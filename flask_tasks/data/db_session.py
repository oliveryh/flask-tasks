import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from flask_tasks.data.modelbase import SqlAlchemyBase

__factory = None


def global_init(db_file: str):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("You must specify a db file.")

    conn_str = "sqlite:///" + db_file.strip()
    engine = sa.create_engine(conn_str, echo=True)

    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import flask_tasks.data.__allmodels

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()
