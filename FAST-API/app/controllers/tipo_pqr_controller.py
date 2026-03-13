import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.tipo_pqr_model import Tipo_pqr
from fastapi.encoders import jsonable_encoder


class Tipo_pqrController:

    def create_tipo_pqr(self, tipo_pqr: Tipo_pqr):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO tipo_pqr (nombre) VALUES (%s)",
                (tipo_pqr.nombre,)
            )

            conn.commit()

            return {"resultado": "Tipo_pqr creado correctamente"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print("Error en BD:", err)
            raise HTTPException(status_code=500, detail="Error al crear tipo_pqr")

        finally:
            if conn:
                conn.close()


    def get_tipo_pqr(self, tipo_pqr_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM tipo_pqr WHERE id_tipo = %s",
                (tipo_pqr_id,)
            )

            result = cursor.fetchone()

            if not result:
                raise HTTPException(status_code=404, detail="Tipo_pqr no encontrado")

            content = {
                "id_tipo": result[0],
                "nombre": result[1]
            }

            return jsonable_encoder(content)

        except HTTPException:
            raise

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print("Error en BD:", err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            if conn:
                conn.close()


    def get_tipo_pqrs(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM tipo_pqr")
            result = cursor.fetchall()

            if not result:
                raise HTTPException(status_code=404, detail="No hay registros")

            payload = []

            for data in result:
                payload.append({
                    "id_tipo": data[0],
                    "nombre": data[1]
                })

            return {"resultado": jsonable_encoder(payload)}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print("Error en BD:", err)
            raise HTTPException(status_code=500, detail="Error en base de datos")

        finally:
            if conn:
                conn.close()


    def update_tipo_pqr(self, tipo_pqr_id: int, tipo_pqr: Tipo_pqr):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE tipo_pqr
                SET nombre = %s
                WHERE id_tipo = %s
            """, (tipo_pqr.nombre, tipo_pqr_id))

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo_pqr no encontrado")

            return {"resultado": "Tipo_pqr actualizado correctamente"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print("Error en BD:", err)
            raise HTTPException(status_code=500, detail="Error al actualizar")

        finally:
            if conn:
                conn.close()


    def delete_tipo_pqr(self, tipo_pqr_id: int):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()

            cursor.execute(
                "DELETE FROM tipo_pqr WHERE id_tipo = %s",
                (tipo_pqr_id,)
            )

            conn.commit()

            if cursor.rowcount == 0:
                raise HTTPException(status_code=404, detail="Tipo_pqr no encontrado")

            return {"resultado": "Tipo_pqr eliminado correctamente"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print("Error en BD:", err)
            raise HTTPException(status_code=500, detail="Error al eliminar")

        finally:
            if conn:
                conn.close()

    # Cuántas PQRs hay de cada tipo — para ver si predominan Peticiones, Quejas o Reclamos
    def get_conteo_pqrs_por_tipo(self):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT t.id_tipo, t.nombre, COUNT(p.id_pqr) AS total
                FROM tipo_pqr t
                LEFT JOIN pqr p ON t.id_tipo = p.id_tipo
                GROUP BY t.id_tipo, t.nombre
                ORDER BY total DESC
            """)
            result = cursor.fetchall()
            payload = []
            for data in result:
                content = {
                    'id_tipo': data[0],
                    'nombre': data[1],
                    'total_pqrs': data[2]
                }
                payload.append(content)
            return {"resultado": jsonable_encoder(payload)}
        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print(err)
            raise HTTPException(status_code=500, detail="Error en base de datos")
        finally:
            if conn:
                conn.close()

    