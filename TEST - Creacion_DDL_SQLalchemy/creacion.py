import urllib
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base

# Definir la Clase (definición de la tabla) y variables
## para la conexión al servidor BBDD
Base = declarative_base()
SERVER = "localhost\SQLEXPRESS"
DATABASE = "AdventureWorks2022"

#a la clase, le pasamos como herencia la case declarative_base() [Base: creada arriba]
class TablaCustomPYTHON(Base):
    __tablename__ = 'Educative_Answers'

    custom_id = Column(Integer, primary_key=True)
    custom_name = Column(String)


# Construir la cadena de conexión utilizando la librería urllib para codificar la parte de la conexión ODBC
params = urllib.parse.quote_plus(f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes')

# Terminar de crear la cadena de conexión completa
conn_str = f'mssql+pyodbc:///?odbc_connect={params}'
engine = create_engine(conn_str)

# Create the tables in the database
Base.metadata.create_all(engine)

# Print the names of all tables in the database
def print_all_tables(engine):
    metadata = MetaData()
    metadata.reflect(bind=engine) #Metadata.reflect() recoge todas las definiciones de tabla en la BBDD indicada
    
    tables = metadata.tables.keys()
    
    print("List of tables:")
    for table in tables:
        print(table)

# Sacar por pantalla todas las tablas que haya en la base de datos indicada
print_all_tables(engine)