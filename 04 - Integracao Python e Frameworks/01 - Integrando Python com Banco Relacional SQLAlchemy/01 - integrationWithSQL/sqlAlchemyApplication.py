import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import select
from sqlalchemy import func

Base = declarative_base()

class User(Base):
    __tablename__ = "user_account"
    #atributos
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(50))

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"
    

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)


    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address (id={self.id}, email_address={self.email_address})"
    

print(User.__tablename__)
print(Address.__tablename__)

#conexao com o banco de dados
DATABASE_USERNAME = 'root'
DATABASE_PASSWORD = '********'
DATABASE_HOST = '********'
DATABASE_PORT = '3306'
DATABASE_NAME = 'pythondio'

DATABASE_URL = f'mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'
engine = create_engine(DATABASE_URL)

# criando as classes como tabelas no banco de dados
Base.metadata.create_all(engine);

inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"));
print(inspetor_engine.get_table_names());
print(inspetor_engine.default_schema_name);

with Session(engine) as session:
    bento = User(
        name = 'Bento',
        fullname = "Bento do Pao",
        address = [Address(email_address = 'bento@cao.com')]
    )

    joao = User(
        name = 'Joao',
        fullname = "Joao II",
        address = [Address(email_address = 'joao@ii.com'),
                   Address(email_address = 'joao@oo.com')]
    )

    bob = User(
        name = 'Bob',
        fullname = "Bob III",
    )

    # enviando para o Banco de Dados (persistência de dados)
    # session.add_all([bento, joao, bob])

    # session.commit()

stmt = select(User).where(User.name.in_(['Bento', 'Bob']))
print(stmt)

for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))

for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc());
print("\nRecuperando info de maneida ordenada")
for result in session.scalars(stmt_order):
    print(result)
print("\nJoin")
stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
for result_join in session.scalars(stmt_join):
    print(result_join)

#print(select(User.fullname, Address.email_address).join_from(Address, User))

print("\nExecutando statement a partir da connection")
connection = engine.connect();
results = connection.execute(stmt_join).fetchall();
for result in results:
    print(result)

print("\nTotal de instâncias em User")
stmt_count = select(func.count('*')).select_from(User)
for result in session.scalars(stmt_count):
    print(result)