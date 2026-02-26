from fastapi import HTTPException
from config.db_config import get_db_connection
from models.usuario_model import Usuario
from fastapi.encoders import jsonable_encoder

class UsuarioController:
        
    def create_usuario(self, usuario: Usuario):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO usuario (nombre,cedula,carrera,semestre,cargo,celular,correo,id_rol,rol) \ VALUES 
            (%s, %s, %s, %s, %s , %s, %s, %s ,%s)", (usuario.nombre, usuario.cedula, usuario.carrera, usuario.semestre, usuario.cargo, usuario.celular, usuario.correo, usuario.id_rol, usuario.rol))
            conn.commit()
            conn.close()
            return {"resultado": "Usuario creado"}
        except psycopg2.Error as err:
            print(err)
            # Si falla el INSERT, los datos no quedan guardados parcialmente en la base de datos
            # Se usa para deshacer los cambios de la transacción activa cuando ocurre un error en el try.
            conn.rollback()
        finally:
            conn.close()
        

    def get_usuario(self, usuario_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario WHERE id = %s", (usuario_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id_usuario':int(result[0]),
                    'nombre':data[1],
                    'cedula':data[2],
                    'carrera':data[3],
                    'semestre':data[4],
                    'cargo':data[5],
                    'celular':data[6],
                    'correo':data[7],
                    'id_rol':data[8],
                    'rol':data[9]
                    
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
       
    def get_usuarios(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM usuario")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id_usuario':data[0],
                    'nombre':data[1],
                    'cedula':data[2],
                    'carrera':data[3],
                    'semestre':data[4],
                    'cargo':data[5],
                    'celular':data[6],
                    'correo':data[7],
                    'id_rol':data[8],
                    'rol':data[9]

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