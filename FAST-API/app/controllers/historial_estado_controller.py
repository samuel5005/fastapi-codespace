import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.historial_estado_model import Historial_estado
from fastapi.encoders import jsonable_encoder

class Historial_estadoController:
        
 def create_historial_estado(self, historial_estado: Historial_estado):   
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO historial_estado (fecha, id_pqrs, id_estado) 
        VALUES (%s, %s, %s)""", (historial_estado.fecha, historial_estado.id_pqrs, historial_estado.id_estado))
        conn.commit()
        return {"resultado": "Historial_estado creado"}
    except psycopg2.Error as err:
        print(err)
        conn.rollback()
        return {"error": str(err)}
    finally:
        conn.close()

def get_historial_estado(self, historial_estado_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM historial_estado WHERE id = %s", (historial_estado_id,))
        result = cursor.fetchone()
        if result:
            content = {
                'id_historial': int(result[0]),
                'fecha': result[1],
                'id_pqrs': result[2],
                'id_estado': result[3]
            }
            return jsonable_encoder(content)
        else:
            raise HTTPException(status_code=404, detail="Historial no encontrado")
    except psycopg2.Error as err:
        print(err)
        conn.rollback()
        return {"error": str(err)}
    finally:
        conn.close()

def get_historial_estados(self):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM historial_estado")
        result = cursor.fetchall()
        if result:
            payload = []
            for data in result:
                content = {
                    'id_historial': data[0],
                    'fecha': data[1],
                    'id_pqrs': data[2],
                    'id_estado': data[3]
                }
                payload.append(content)
            return {"resultado": jsonable_encoder(payload)}
        else:
            raise HTTPException(status_code=404, detail="No hay registros")
    except psycopg2.Error as err:
        print(err)
        conn.rollback()
        return {"error": str(err)}
    finally:
        conn.close()

def update_historial_estado(self, historial_estado_id: int, historial_estado: Historial_estado):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE historial_estado
            SET fecha = %s, id_pqrs = %s, id_estado = %s
            WHERE id = %s
        """, (historial_estado.fecha, historial_estado.id_pqrs, historial_estado.id_estado, historial_estado_id))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Historial no encontrado")
        return {"resultado": "Historial_estado actualizado"}
    except psycopg2.Error as err:
        print(err)
        conn.rollback()
        return {"error": str(err)}
    finally:
        conn.close()

def delete_historial_estado(self, historial_estado_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM historial_estado WHERE id = %s", (historial_estado_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Historial no encontrado")
        return {"resultado": "Historial_estado eliminado"}
    except psycopg2.Error as err:
        print(err)
        conn.rollback()
        return {"error": str(err)}
    finally:
        conn.close()