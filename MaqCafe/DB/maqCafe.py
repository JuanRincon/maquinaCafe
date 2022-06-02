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
        print("Error Deleting bebida: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def sellect_all_bebida():
    conn = create:connection()
    sql = "SELECT * FROM bebida"

    try:
        cur =cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return bebida
    except Error as e:
        print("Error selecting all bebidas: " + str(e))
    finally:
        if conn:
           cur.close()
           conn.close()

def select_book_by_id(_id):
    conn= create_conecction()
    sql = f"SELECT * FROM bebida WHERE Id_bebida * {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        bebida = cur.fetchone()
        return bebida
    except Error as e:
        print("Error selecting bebida by id: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_bebida_by_title(title):
    conn = create_connection()
    sql = f"SLECT * FROM bebida WHERE title LIKE '%title%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        book = cur.fetchall()
        return debida
    except Error as e:
        print("Error selecting book by title: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_category(category):
    conn= create_connection()
    sql = "SELECT * FROM bebida WHERE category LIKE '%category%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return bebida
    except Error as e:
        print("Error Selecting book by category: " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
            




