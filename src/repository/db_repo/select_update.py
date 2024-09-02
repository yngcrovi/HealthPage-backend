from sqlalchemy import select, func, cast, Integer, and_
from repository.config.engine import async_session_factory
from repository.tables.tables_orm import Test


def select_orm(new_id = 1):
    with async_session_factory() as session:
        new = session.get(Test, new_id)
        query = (
            select(Test.id)
            .where(Test.compenstation==20000)
        )
        result = session.execute(query)  
        print(result.scalar())

# select_orm()

def update_orm(new_id = 1, new_username: str = 'zxc'):
    with async_session_factory() as session:
        new = session.get(Test, new_id)
        new.username = new_username
        session.commit()

# update_orm()

def select_avg_orm():
    with async_session_factory() as session:
        query = (
            select(
                Test.id,
                cast(func.avg(Test.compenstation), Integer)
            )
            .select_from(Test)
            .filter(and_(
                Test.compenstation > 40000,
                Test.username == 'qwe'
            ))
            .group_by(Test.id)
        )
        print(query.compile(compile_kwargs={"literal_binds": True}))
        result = session.execute(query)
        res = result.all()
        print(res)
        print(res[0].id)

# select_avg_orm()

def insert_data_orm():
    with async_session_factory() as session:
        a = Test(username = 'avy2', compenstation = 100)
        session.add(a)
        #или add_all([...,...])
        session.commit()

# insert_data_orm()