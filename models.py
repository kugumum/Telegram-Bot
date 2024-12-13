from sqlalchemy import BigInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(url='sqlite+aiosqlite:///db.sqlite3')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
  pass


class User(Base):
  __tablename__ = 'users'

  id: Mapped[int] = mapped_column(primary_key=True)
  tg_id = mapped_column(BigInteger)


class Category(Base):
  __tablename__ = 'categories'
   
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column()


class Item(Base):
  __tablename__ = 'items'

  id: Mapped[int] = mapped_column(primary_key=True)

