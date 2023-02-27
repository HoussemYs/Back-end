import psycopg2

hostname = 'localhost'
database = 'configsystem'
username = 'postgres'
pwd = 'houssem'
port_id = 5050
conn = None
cursor = None

try:
    conn = psycopg2.connect(
        host = hostname,
        port = port_id,
        database = database,
        user = username,
        password = pwd
    )
    cursor = conn.cursor()
    
    # sql_query = '''ALTER TABLE profiles ADD CONSTRAINT profiles_user_id_unique UNIQUE(user_id);'''
    # cursor.execute(sql_query)
    # conn.commit()
    # print("Success !")
    
    # sql_query = '''ALTER TABLE users ADD CONSTRAINT user_id_unique UNIQUE(id);'''
    # cursor.execute(sql_query)
    # conn.commit()
    # print("Success !")

    # #Creation de la table types ********
    # sql_query1 = ''' CREATE TABLE types(
    #     id BIGSERIAL PRIMARY KEY,
    #     name VARCHAR(255) NOT NULL,
    #     description VARCHAR(255) NOT NULL) '''
    # cursor.execute(sql_query1)
    # conn.commit()
    # print("Table types created with successfully!")
    
    # #Creation de la table users 
    # sql_query1 = ''' CREATE TABLE users(
    #     id BIGSERIAL PRIMARY KEY,
    #     username VARCHAR(255) NOT NULL,
    #     password VARCHAR(255) NOT NULL,
    #     type_id INTEGER NOT NULL REFERENCES types(id)) '''
    # cursor.execute(sql_query1)
    # conn.commit()
    # print("Table users created with successfully!")
    
    # sql_query = '''ALTER TABLE users ADD CONSTRAINT unique_user_id UNIQUE (id);'''
    # cursor.execute(sql_query)
    # print("AlTER users success")
    
    
    # #Creation de la table profiles
    # sql_query2 = ''' CREATE TABLE profiles(
    #     id BIGSERIAL PRIMARY KEY,
    #     name VARCHAR(255) NOT NULL,
    #     email VARCHAR(255) NOT NULL,
    #     telephone VARCHAR(255) NOT NULL,
    #     adresse VARCHAR(255) NOT NULL,
    #     image VARCHAR(255) NOT NULL,
    #     description VARCHAR(255) NOT NULL,
    #     user_id INTEGER NOT NULL REFERENCES users(id))'''
    # cursor.execute(sql_query2)
    # conn.commit()
    # print("Table profiles created with successfully!")
    
    
    # Creation de la table configurations
    # sql_query2 = ''' CREATE TABLE configurations(
    #     id BIGSERIAL PRIMARY KEY,
    #     name VARCHAR(255) NOT NULL,
    #     value VARCHAR(255) NOT NULL,
    #     defaultValue VARCHAR(255) NOT NULL,
    #     createdAt TIMESTAMP NOT NULL,
    #     createdBy VARCHAR(255) NOT NULL,
    #     updatedBy VARCHAR(255),
    #     description VARCHAR(255) NOT NULL,
    #     version INTEGER NOT NULL DEFAULT 1
    #     )'''
    # cursor.execute(sql_query2)
    # conn.commit()
    # print("Configurations created with successfully!")
    
    # sql_query='''CREATE TABLE user_configurations (
    #     user_id BIGINT REFERENCES users(id),
    #     configuration_id BIGINT REFERENCES configurations(id),
    #     PRIMARY KEY (user_id, configuration_id)
    #     )'''
    # cursor.execute(sql_query)
    # conn.commit()
    # if conn.commit():
    #     print("Created")
    
    # sql_query='''CREATE TABLE roles(
    #     id BIGSERIAL PRIMARY KEY,
    #     name VARCHAR(255) NOT NULL,
    #     descrition VARCHAR(255) NOT NULL
    #     )'''
    # cursor.execute(sql_query)
    # conn.commit()
    # print("AAA")
    
    # sql_query='''CREATE TABLE permissions(
    #     id BIGSERIAL PRIMARY KEY,
    #     name VARCHAR(255) NOT NULL,
    #     descrition VARCHAR(255) NOT NULL
    #     )'''
    # cursor.execute(sql_query)
    # conn.commit()
    # print("AAA")
    
    # sql_query='''CREATE TABLE roles_permissions(
    #     role_id BIGINT REFERENCES roles(id),
    #     permission_id BIGINT REFERENCES permissions(id),
    #     PRIMARY KEY (role_id, permission_id)
    #     )'''
    # cursor.execute(sql_query)
    # conn.commit()
    # print("AAA")
    
    # sql_query='''CREATE TABLE users_roles(
    #     user_id BIGINT REFERENCES users(id),
    #     role_id BIGINT REFERENCES roles(id),
    #     PRIMARY KEY (user_id, role_id)
    #     )'''
    # cursor.execute(sql_query)
    # conn.commit()
    # print("AAA")
    
    
except Exception as e:
    print(e)
finally:
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()