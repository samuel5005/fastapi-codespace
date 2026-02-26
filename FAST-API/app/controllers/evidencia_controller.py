from fastapi import HTTPException
from config.db_config import get_db_connection
from models.evidencia_model import Evidencia
from fastapi.encoders import jsonable_encoder

class EvidenciaController:
        
    def create_evidencia(self, evidencia: Evidencia):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO evidencia (nombre_archivo,tipo_archivo,url,id_incidencia)\ VALUES "
            " (%s, %s, %s, %s)", (evidencia.nombre_archivo, evidencia.tipo_archivo, evidencia.url, evidencia.id_incidencia))
            conn.commit()
            conn.close()
            return {"resultado": "Evidencia creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_evidencia(self, evidencia_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM evidencia WHERE id = %s", (evidencia_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id_evidencia':data[0],
                    'nombre_archivo':data[1],
                    'tipo_archivo':data[2],
                    'url':data[3],
                    'id_incidencia':data[4]
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
       
    def get_evidencias(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM evidencia")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_evidencia':data[0],
                    'nombre_archivo':data[1],
                    'tipo_archivo':data[2],
                    'url':data[3],
                    'id_incidencia':data[4]
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