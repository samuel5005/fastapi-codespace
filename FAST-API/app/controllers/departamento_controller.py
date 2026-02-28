import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.departamento_model import Departamento
from fastapi.encoders import jsonable_encoder

class DepartamentoController:
        
    def create_departamento(self, departamento: Departamento):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO departamento (nombre,pqrs) 
            VALUES (%s, %s)""", (departamento.nombre, departamento.pqrs))
            conn.commit()
            conn.close()
            return {"resultado": "Departamento creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_departamento(self, departamento_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM departamento WHERE id = %s", (departamento_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id_departamento':result[0],
                    'nombre':result[1],
                    'pqrs':result[2]
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
       
    def get_departamentos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM departamento")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_departamento':data[0],
                    'nombre':data[1],
                   
                    
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

    def update_departamento(self, departamento_id: int, departamento: Departamento):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE departamento
                SET nombre = %s, pqrs = %s
                WHERE id = %s
            """, (departamento.nombre, departamento.pqrs, departamento_id))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Departamento no encontrado")
            return {"resultado": "Departamento actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_departamento(self, departamento_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM departamento WHERE id = %s", (departamento_id,))
            conn.commit()
            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Departamento no encontrado")
            return {"resultado": "Departamento eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    
    
       

##user_controller = UserController()