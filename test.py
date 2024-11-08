from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from contextlib import contextmanager


# 数据库连接信息
DATABASE_URL = 'postgresql+psycopg2://postgres:sams111@192.168.2.230:5432/sams'

# 创建数据库引擎
engine = create_engine(DATABASE_URL, echo=False, pool_size=20, max_overflow=100, pool_recycle=60)

# 创建基本类
Base = declarative_base()

# 定义模型
class User(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

# 创建数据表
# Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)


@contextmanager
def getSession():
    s = Session()
    try:
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()

# 添加用户
def add_user(name, email):
    new_user = User(name=name, email=email)
    with getSession() as session:
        session.add(new_user)
    print(f"Added user: {new_user}")

# 查询用户
def get_user(user_id):
    with getSession() as session:
        user = session.query(User).filter_by(id=user_id).first()
    return user

# 更新用户
def update_user(user_id, new_name):
    with getSession() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            user.name = new_name
            print(f"Updated user: {user}")

# 删除用户
def delete_user(user_id):
    with getSession() as session:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            session.delete(user)
            print(f"Deleted user: {user}")

# 示例操作
if __name__ == "__main__":
    # 添加用户
    # add_user("Alice", "alice@example.com")
    # add_user("Bob", "bob@example.com")

    # 查询用户
    user = get_user(1)
    print(f"Queried user: {user}")

    # # 更新用户
    # update_user(1, "Alice Smith")

    # # 删除用户
    # delete_user(2)
