from fastapi import HTTPException
from config.db_config import get_db_connection
from models.estado_model import Estado
from fastapi.encoders import jsonable_encoder

class EstadoController:
        
    def create_estado(self, estado: Estado):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO estado (nombre,historial_estados,incidencias) \
            VALUES (%s, %s, %s)", (estado.nombre, estado.historial_estados, estado.incidencias))
            conn.commit()
            conn.close()
            return {"resultado": "Estado creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_estado(self, estado_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estado WHERE id = %s", (estado_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id_estado':data[0],
                    'nombre':data[1],
                    'historial_estados':data[2],
                    'incidencias':data[3]
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
       
    def get_estados(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estado")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_estado':data[0],
                    'nombre':data[1],
                    'historial_estados':data[2],
                    'incidencias':data[3]
                   
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
    
    
       

##user_controller = UserController()