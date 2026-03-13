import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.asignacion_responsable_model import Asignacion_responsable
from fastapi.encoders import jsonable_encoder

class Asignacion_responsableController:
        
    def create_asignacion_responsable(self, asignacion_responsable: Asignacion_responsable):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO asignacion_responsable (id_pqr, id_usuario, fecha_asignacion) 
            VALUES (%s, %s, %s)""", (asignacion_responsable.id_pqr, asignacion_responsable.id_usuario, asignacion_responsable.fecha_asignacion))
            conn.commit()
            conn.close()
            return {"resultado": "Asignacion_responsable creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_asignacion_responsable(self, asignacion_responsable_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asignacion_responsable WHERE id_asignacion = %s", (asignacion_responsable_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id_asignacion':result[0],
                    'id_pqr':result[1],
                    'id_usuario':result[2],
                    'fecha_asignacion':result[3]


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
       
    def get_asignacion_responsables(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asignacion_responsable")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_asignacion':result[0],
                    'id_pqr':result[1],
                    'id_usuario':result[2],
                    'fecha_asignacion':result[3]
                   
                    
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

    def update_asignacion_responsable(self, asignacion_responsable_id: int, asignacion_responsable: Asignacion_responsable):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE asignacion_responsable
                SET id_pqr = %s, id_usuario = %s, fecha_asignacion = %s 
                WHERE id_asignacion = %s
            """, (asignacion_responsable.id_pqr, asignacion_responsable.id_usuario, asignacion_responsable.fecha_asignacion, asignacion_responsable_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Asignacion_responsable no encontrado")
            return {"resultado": "Asignacion_responsable actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_asignacion_responsable(self, asignacion_responsable_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM asignacion_responsable WHERE id_asignacion = %s", (asignacion_responsable_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Asignacion_responsable no encontrado")
            return {"resultado": "Asignacion_responsable eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    # Ver todas las PQRs asignadas a un responsable — su carga de trabajo
    def get_asignaciones_by_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asignacion_responsable WHERE id_usuario = %s ORDER BY fecha_asignacion DESC", (usuario_id,))
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id_asignacion': data[0], 'id_pqr': data[1],
                    'id_usuario': data[2], 'fecha_asignacion': data[3]
                }
                payload.append(content)
            if result:
                return {"resultado": jsonable_encoder(payload)}
            else:
                raise HTTPException(status_code=404, detail="No hay asignaciones para este usuario")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    # Ver quién está asignado a una PQR específica
    def get_asignacion_by_pqr(self, pqr_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM asignacion_responsable WHERE id_pqr = %s", (pqr_id,))
            result = cursor.fetchone()
            if result:
                content = {
                    'id_asignacion': result[0], 'id_pqr': result[1],
                    'id_usuario': result[2], 'fecha_asignacion': result[3]
                }
                return jsonable_encoder(content)
            else:
                raise HTTPException(status_code=404, detail="No hay asignacion para esta PQR")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    
    
    
       

##user_controller = UserController()