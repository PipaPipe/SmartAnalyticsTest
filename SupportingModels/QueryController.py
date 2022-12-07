import psycopg2


connection_parameters = [None, None, None, None, None]
current_table = None
is_connection = False

def get_connection():
    return psycopg2.connect(user=connection_parameters[0],
                            password=connection_parameters[1],
                            host=connection_parameters[2],
                            port=connection_parameters[3],
                            database=connection_parameters[4])


'''
Функция,которая устанавливает параметры для соединения
И проверяет соединение
'''
def set_connection():
    try:
        connection = get_connection()
    except Exception:
        connection = False
    finally:
        if connection:
            connection.close()
            return True
        return False


'''
Функция, которая получает названия всех
таблиц из БД
'''
def get_table_names():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("""SELECT table_name FROM information_schema.tables
                            WHERE table_schema = 'public'""")
        tables = []
        for table in cursor.fetchall():
            tables.append(str(table[0]))
        return True, tables
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True, tables
        return connection


'''
Функция, которая получает названия 
Всех колонок в таблице
'''
def get_columns_names():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM {current_table} LIMIT 0""")
        column_names = [row[0] for row in cursor.description]
        return True, column_names
    except Exception:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True, column_names
        return connection


'''
Функция для получения всех значений в таблице
'''
def get_table_records():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(f"""SELECT * FROM {current_table}""")
        table_records = cursor.fetchall()
        return True, table_records
    except Exception:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True, table_records
        return connection


'''
Добавление записи в таблицу
'''
def add_record(record):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        elements = ["'" + element + "'" for element in record]
        cursor.execute(f"""INSERT INTO {current_table} VALUES ({', '.join(list(map(str, elements)))})""")
        connection.commit()
        return True
    except Exception as e:

        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True
        return connection


'''
Изменение записи в таблице
'''
def update_record(element_field, element_value, updated_element, new_value):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(f"""UPDATE {current_table} SET {updated_element} = '{new_value} ' 
                        WHERE {element_field} = {element_value}""")
        connection.commit()
        return True
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True
        return connection


'''
Удаление записи из таблицы
'''
def remove_record(element_field, element_value):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {current_table} WHERE {element_field} = {element_value}")
        connection.commit()
        return True
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True
        return connection


'''
Создание таблицы
'''
def create_table(table_name, table_fields):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        all_fields = ''
        primary_key_fields = ''
        for field in table_fields:
            if 'K' in field:
                primary_key_fields += field[0] + ', '
            all_fields += field[0] + ' ' + field[1] + ', '
        primary_key_fields = primary_key_fields[0: len(primary_key_fields)-2]
        query = (f"""CREATE TABLE {table_name}(
                {all_fields} 
                PRIMARY KEY ({primary_key_fields}))""")
        cursor.execute(query)
        connection.commit()
        return True
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()

        return connection


'''
Удаление таблицы
'''
def remove_table(table_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(f"DROP TABLE {table_name}")
        connection.commit()
        return True
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True
        return connection


'''
Изменение названия таблицы
'''
def rename_table(old_table_name, new_table_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(f"""ALTER TABLE {old_table_name}
                            RENAME TO {new_table_name}""")
        connection.commit()
        return True
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True
        return connection


'''
Изменение названия столбца
'''
def rename_column(table_name, old_column_name, new_column_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(f"""ALTER TABLE {table_name}
                            RENAME COLUMN {old_column_name} TO {new_column_name}""")
        connection.commit()
        return True
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True
        return connection


def add_column(table_name, column_name, column_type):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(f"""ALTER TABLE {table_name}
                            ADD {column_name} {column_type} DEFAULT NULL""")
        connection.commit()
        return True
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True
        return connection


def drop_column(table_name, column_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query_drop(table_name, column_name))
        connection.commit()
        return True
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True
        return connection


def get_types():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(f"""SELECT column_name, data_type FROM information_schema.columns
                            WHERE table_schema = 'public' AND table_name = '{current_table}'""")
        column_types = cursor.fetchall()
        return True, column_types
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return True, column_types
        return connection


def change_type(table_name, column_name, new_type):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(f"""SELECT column_name, data_type FROM information_schema.columns
                            WHERE table_schema = 'public' AND table_name = '{table_name}'""")

        current_type = ""
        column_types = cursor.fetchall()

        for pair in column_types:
            if column_name == pair[0]:
                current_type = pair[1]
                break
        if current_type == new_type:
            return True
        # строку зануляем
        elif current_type == 'character varying':
            cursor.execute(query_drop(table_name, column_name))
            connection.commit()
            cursor.execute(query_change_to_null(table_name, column_name, new_type))
            connection.commit()
            return True

        elif current_type == 'integer':
            # integer можно перевести в строку и в decimal
            if new_type == 'numeric' or new_type == 'character varying':
                cursor.execute(query_change_type(table_name, column_name, new_type))
                connection.commit()
                return True

            else:
                cursor.execute(query_drop(table_name, column_name))
                connection.commit()
                cursor.execute(query_change_to_null(table_name, column_name, new_type))
                connection.commit()
                return True

        elif current_type == 'numeric':
            # decimal можно перевести в int и строку
            if new_type == 'integer' or new_type == 'character varying':
                cursor.execute(query_change_type(table_name, column_name, new_type))
                connection.commit()
                return True
            else:
                cursor.execute(query_drop(table_name, column_name))
                connection.commit()
                cursor.execute(query_change_to_null(table_name, column_name, new_type))
                connection.commit()
                return True
        elif current_type == 'date':
            # дату можно перевести в строку
            if new_type == 'character varying':
                cursor.execute(query_change_type(table_name, column_name, new_type))
                connection.commit()
                return True
            else:
                cursor.execute(query_drop(table_name, column_name))
                connection.commit()
                cursor.execute(query_change_to_null(table_name, column_name, new_type))
                connection.commit()
                return True
        else:
            connection = False
            return False
    except Exception as e:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
            return connection
        return connection


def query_drop(table_name, column_name):
    return f"""ALTER TABLE {table_name}
                DROP COLUMN {column_name}"""


def query_change_to_null(table_name, column_name, new_type):
    return f"""ALTER TABLE {table_name}
                ADD {column_name} {new_type} DEFAULT NULL"""


def query_change_type(table_name, column_name, new_type):
    return f"""ALTER TABLE {table_name}
                ALTER COLUMN {column_name} TYPE {new_type}"""
