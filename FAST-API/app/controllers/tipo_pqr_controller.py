import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tipo_pqr_model import Tipo_pqr
from fastapi.encoders import jsonable_encoder

class Tipo_pqrController:
        
    def create_tipo_pqr(self, tipo_pqr: Tipo_pqr):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tipo_pqr (nombre) VALUES (%s)", (tipo_pqr.nombre,))
            conn.commit()
            conn.close()
            return {"resultado": "Tipo_pqr creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_tipo_pqr(self, tipo_pqr_id: int):
    try:

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tipo_pqr WHERE id_tipo = %s", (tipo_pqr_id,))
        result = cursor.fetchone()

        if not result:
            raise HTTPException(status_code=404, detail="Tipo_pqr no encontrado")

        content = {
            'id_tipo': int(result[0]),
            'nombre': result[1]
        }

        return jsonable_encoder(content)

    except psycopg2.Error as err:
        print(err)
        conn.rollback()
        raise HTTPException(status_code=500, detail="Error en base de datos")

    finally:
        conn.close()
       
    def get_tipo_pqrs(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM tipo_pqr")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_tipo':data[0],
                    'nombre':data[1]
                   
                    
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="User not found")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def update_tipo_pqr(self, tipo_pqr_id: int, tipo_pqr: Tipo_pqr):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE tipo_pqr
                SET nombre = %s
                WHERE id = %s
            """, (tipo_pqr.nombre, tipo_pqr_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo_pqr no encontrado")
            return {"resultado": "Tipo_pqr actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_tipo_pqr(self, tipo_pqr_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tipo_pqr WHERE id = %s", (tipo_pqr_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo_pqr no encontrado")
            return {"resultado": "Tipo_pqr eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
       

##user_controller = UserController()