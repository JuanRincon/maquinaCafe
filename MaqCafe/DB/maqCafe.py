from ast import Try
import sqlite3
from sqlite3 import Error
from turtle import title
from .connection import create_connection

def insert_maqCafe(data):
    conn = create_connection() 
    sql = """ INSERT INTO books (Bebida, Precio) 
                VALUES(?, ?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevo libro agregado")
        return True
    except Error as e:
        print("Error Inserting new book" + str(e))
    finally:
        if conn:
            cur.close() 
            conn.close()
        
def update_book(_id, data):
    conn = create_connection()
    
    sql = f""" UPDATE books SET 
                            Bebida = ?
                            Precio = ?
            WHERE Id_bebida = {_id}
    """

try:
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    print("bebida Actualizada")
    return True
except Error as e:
    print("Error updating bebida: " + str(e))
finally:
    if conn:
        cur.close()
        conn.close()

def delete_bebidas():
    conn = create_connection()
    sql = f"DELETE FROM bebidas WHERE Id_bebida = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("bebida Eliminada")
        return True
    except Error as e:
        pass
    finally:
        pass