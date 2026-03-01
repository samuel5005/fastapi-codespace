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
            cursor.execute("""INSERT INTO historial_estado (fecha ,id_pqr,id_estado) 
            VALUES (%s, %s, %s)""", (historial_estado.fecha, historial_estado.id_pqrs, historial_estado.id_estado))
            conn.commit()
            return {"resultado": "Historial_estado creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
            return {"error": str(err)}
        finally:
            conn.close()
        

    def get_historial_estado(self, historial_estado_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial_estado WHERE id_historial = %s", (historial_estado_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id_historial':int(result[0]),
                    'fecha':result[1],
                    'id_pqr':result[2],
                    'id_estado':result[3]
                    
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
       
    def get_historial_estados(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM historial_estado")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_historial':data[0],
                    'fecha':data[1],
                    'id_pqr':data[2],
                    'id_estado':data[3]
                   
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

    def update_historial_estado(self, historial_estado_id: int, historial_estado: Historial_estado):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE historial_estado
                SET fecha = %s, id_pqrs = %s, id_estado = %s, estado = %s, pqrs = %s
                WHERE id = %s
            """, (historial_estado.fecha, historial_estado.id_pqrs, historial_estado.id_estado, historial_estado.estado, historial_estado.pqrs, historial_estado_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Historial no encontrado")
            return {"resultado": "Historial_estado actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
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
        finally:
            conn.close()
    
    
       

##user_controller = UserController()