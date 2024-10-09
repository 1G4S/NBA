
from sqlalchemy import create_engine


connection_string = 'postgresql+psycopg2://user123:password123@localhost:5000/database_name'
engine = create_engine(connection_string)


df.to_sql(table_name, engine=engine, if_exists='append')

# general conn function -> create_connection_engine -> param: (postgres, mysql, mssql) -> conn_string -> engine
# load -> param: engine -> exec to_sql -> end

