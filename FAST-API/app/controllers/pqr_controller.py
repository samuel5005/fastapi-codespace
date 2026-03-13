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

    # Obtener todas las PQRs de un usuario — para que cada usuario vea solo las suyas
    def get_pqrs_by_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pqr WHERE id_usuario = %s", (usuario_id,))
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id_pqr': data[0], 'descripcion': data[1],
                    'fecha': data[2], 'id_usuario': data[3],
                    'id_tipo': data[4], 'id_estado': data[5],
                    'id_departamento': data[6], 'id_prioridad': data[7]
                }
                payload.append(content)
            if result:
                return {"resultado": jsonable_encoder(payload)}
            else:
                raise HTTPException(status_code=404, detail="No se encontraron PQRs para este usuario")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    # Filtrar PQRs por estado — ver Pendientes, En proceso, Resueltas, etc.
    def get_pqrs_by_estado(self, estado_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pqr WHERE id_estado = %s", (estado_id,))
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id_pqr': data[0], 'descripcion': data[1],
                    'fecha': data[2], 'id_usuario': data[3],
                    'id_tipo': data[4], 'id_estado': data[5],
                    'id_departamento': data[6], 'id_prioridad': data[7]
                }
                payload.append(content)
            if result:
                return {"resultado": jsonable_encoder(payload)}
            else:
                raise HTTPException(status_code=404, detail="No hay PQRs con ese estado")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    # Cambiar solo el estado de una PQR — sin modificar todo el registro
    def update_estado_pqr(self, pqr_id: int, nuevo_estado_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE pqr SET id_estado = %s WHERE id_pqr = %s", (nuevo_estado_id, pqr_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="PQR no encontrada")
            return {"resultado": "Estado de PQR actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    # Filtrar PQRs por departamento — ver las solicitudes asignadas a cada área
    def get_pqrs_by_departamento(self, departamento_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pqr WHERE id_departamento = %s", (departamento_id,))
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id_pqr': data[0], 'descripcion': data[1],
                    'fecha': data[2], 'id_usuario': data[3],
                    'id_tipo': data[4], 'id_estado': data[5],
                    'id_departamento': data[6], 'id_prioridad': data[7]
                }
                payload.append(content)
            if result:
                return {"resultado": jsonable_encoder(payload)}
            else:
                raise HTTPException(status_code=404, detail="No hay PQRs para ese departamento")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    # Filtrar PQRs por prioridad — ver las urgentes primero
    def get_pqrs_by_prioridad(self, prioridad_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pqr WHERE id_prioridad = %s", (prioridad_id,))
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id_pqr': data[0], 'descripcion': data[1],
                    'fecha': data[2], 'id_usuario': data[3],
                    'id_tipo': data[4], 'id_estado': data[5],
                    'id_departamento': data[6], 'id_prioridad': data[7]
                }
                payload.append(content)
            if result:
                return {"resultado": jsonable_encoder(payload)}
            else:
                raise HTTPException(status_code=404, detail="No hay PQRs con esa prioridad")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    
    
##pqr_controller = pqrController()






