import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.pqr_model import Pqr
from fastapi.encoders import jsonable_encoder

class PqrController:
        
    def create_pqr(self, pqr: Pqr):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO pqr (descripcion,fecha,id_usuario,id_tipo,id_estado,id_departamento,id_prioridad)\
             VALUES (%s, %s, %s, %s, %s ,%s, %s)", (pqr.descripcion, pqr.fecha, pqr.id_usuario, pqr.id_tipo, pqr.id_estado, pqr.id_departamento, pqr.id_prioridad))
            conn.commit()
            conn.close()
            return {"resultado": "pqr creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_pqr(self, pqr_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pqr WHERE id_pqr = %s", (pqr_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id_pqr':result[0],
                    'descripcion':result[1],
                    'fecha':result[2],
                    'id_usuario':result[3],
                    'id_tipo':result[4],
                    'id_estado':result[5],
                    'id_departamento':result[6],
                    'id_prioridad':result[7]
                           
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
       
    def get_pqrs(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pqr")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_pqr':data[0],
                    'descripcion':data[1],
                    'fecha':data[2],
                    'id_usuario':data[3],
                    'id_tipo':data[4],
                    'id_estado':data[5],
                    'id_departamento':data[6],
                    'id_prioridad':data[7]
                    
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

    def update_pqr(self, pqr_id: int, pqr: Pqr):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE pqr
                SET descripcion = %s, fecha = %s, id_usuario = %s, id_tipo = %s, id_estado = %s,
                    id_departamento = %s, id_prioridad = %s
                WHERE id_pqr = %s
            """, (pqr.descripcion, pqr.fecha, pqr.id_usuario, pqr.id_tipo, pqr.id_estado, pqr.id_departamento,
                  pqr.id_prioridad, pqr_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Pqr no encontrado")
            return {"resultado": "Pqr actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_pqr(self, pqr_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM pqr WHERE id_pqr = %s", (pqr_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Pqr no encontrado")
            return {"resultado": "Pqr eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
##pqr_controller = pqrController()






