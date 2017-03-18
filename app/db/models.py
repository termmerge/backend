from sqlalchemy import \
  create_engine, \
  Column, ForeignKey, \
  MetaData
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ


db_engine = create_engine(
  'postgres://{}:{}@{}/{}'.format(
    environ.get("POSTGRES_USER"),
    environ.get("POSTGRES_PASS"),
    environ.get("POSTGRES_HOST"),
    environ.get("POSTGRES_DB")
  )
)

metadata = MetaData(bind=db_engine)
SessionClass = sessionmaker(bind=db_engine)
Base = declarative_base(bind=db_engine, metadata=metadata)


class User(Base):
  __tablename__ = "user"

  id = Column(postgresql.INTEGER,
              nullable=False,
              primary_key=True,
              autoincrement=True)
  name = Column(postgresql.TEXT,
                nullable=False)
  username = Column(postgresql.TEXT,
                    nullable=False)
  password = Column(postgresql.TEXT,
                    nullable=False)
  created_at = Column(postgresql.TIMESTAMP,
                      nullable=False)


class Report(Base):
  __tablename__ = "report"

  id = Column(postgresql.INTEGER,
              nullable=False,
              primary_key=True,
              autoincrement=True)
  user_id = Column(postgresql.TEXT,
                   ForeignKey("user.id"),
                   nullable=False)
  created_at = Column(postgresql.TIMESTAMP,
                      nullable=False)
  converge = Column(postgresql.TEXT,
                    nullable=False)


class WordTimeline(Base):
  __tablename__ = "word_timeline"

  report_id = Column(postgresql.TEXT,
                     ForeignKey("report.id"),
                     nullable=False,
                     primary_key=True)
  word = Column(postgresql.TEXT,
                nullable=False,
                primary_key=True)
  branch = Column(postgresql.INT,
                  nullable=False)
  epoch = Column(postgresql.INT,
                 nullable=False)
