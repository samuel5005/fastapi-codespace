import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.respuesta_model import Respuesta
from fastapi.encoders import jsonable_encoder

class RespuestaController:
        
    def create_respuesta(self, respuesta: Respuesta):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO respuesta (mensaje,fecha,id_pqr,id_usuario) \
            VALUES (%s, %s, %s, %s)", (respuesta.mensaje, respuesta.fecha, respuesta.id_pqr, respuesta.id_usuario))
            conn.commit()
            conn.close()
            return {"resultado": "Respuesta creado"}
        except psycopg2.Error as err:
            conn.rollback()
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_respuesta(self, respuesta_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM respuesta WHERE id_respuesta = %s", (respuesta_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id_respuesta':int(result[0]),
                    'mensaje':result[1],
                    'fecha':result[2],
                    'id_pqr':result[3],
                    'id_usuario':result[4]
                    
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                ##Esto interrumpe la ejecución y responde al cliente con un código 404
                ## comunica al cliente de la API qué pasó (error HTTP).
                ##código 404,comportamiento correcto según las reglas HTTP
                raise HTTPException(status_code=404, detail="User not found")  
                
        except psycopg2.Error as err:
            print(err)
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            ##Maneja el estado de la transacción en la base de datos.Si un INSERT, UPDATE o DELETE falla dentro de una transacción, rollback() revierte esos cambios.
            conn.rollback()
        finally:
            conn.close()
       
    def get_respuestas(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM respuesta")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_respuesta':data[0],
                    'mensaje':data[1],
                    'fecha':data[2],
                    'id_pqr':data[3],
                    'id_usuario':data[4]
                    
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

    def update_respuesta(self, respuesta_id: int, respuesta: Respuesta):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE respuesta
                SET mensaje = %s, fecha = %s, id_pqr = %s, id_usuario = %s
                WHERE id_respuesta = %s
            """, (respuesta.mensaje, respuesta.fecha, respuesta.id_pqr, respuesta.id_usuario, respuesta_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Respuesta no encontrada")
            return {"resultado": "Respuesta actualizada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_respuesta(self, respuesta_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM respuesta WHERE id_respuesta = %s", (respuesta_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Respuesta no encontrada")
            return {"resultado": "Respuesta eliminada"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
       

##user_controller = UserController()