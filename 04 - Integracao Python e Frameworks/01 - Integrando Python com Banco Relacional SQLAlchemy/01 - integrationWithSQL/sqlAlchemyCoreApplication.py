from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import text

#conexao com o banco de dados
DATABASE_USERNAME = 'root'
DATABASE_PASSWORD = '********'
DATABASE_HOST = '*********'
DATABASE_PORT = '3306'
DATABASE_NAME = 'teste'

DATABASE_URL = f'mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/'
engine = create_engine(DATABASE_URL)

with engine.connect() as connection:
    connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME}"))

DATABASE_URL = f'mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
engine = create_engine(DATABASE_URL)

metadata_obj = MetaData(schema=DATABASE_NAME)
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False)
)

user_prefs = Table(
    'user_prefes',
    metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False ),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(1000))
)

for table in metadata_obj.sorted_tables:
    print(table)

print(metadata_obj.tables)

metadata_obj.create_all(engine)

sql_insert = text("insert into user values(1, 'bento', 'bento@cao.com', 'bentaoPao')")

with engine.connect() as connection:
    # Começa uma transação
    with connection.begin():
        # Inserção de dados
        sql_insert = text("INSERT INTO user VALUES (1, 'bento', 'bento@cao.com', 'bentaoPao')")
        connection.execute(sql_insert)
        print('\nExecutando statement SQL de inserção')

    # Executa a seleção para verificar a inserção
    sql = text('SELECT * FROM user')
    result = connection.execute(sql)
    for row in result:
        print(row)