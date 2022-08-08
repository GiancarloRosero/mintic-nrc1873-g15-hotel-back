from flask import jsonify
from database.db import get_connection
from werkzeug.security import check_password_hash


class RoomModel():

    @classmethod
    def register(self, room):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO public.room (name, description_short, description_large, price, code)
                    VALUES (%s, %s, %s, %s, %s)""", (room.name, room.descriptionShort, room.descriptionLarge, room.price, room.code,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_images(self, code, path_save_image):

        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT id FROM public.room where code = %s """, (code,))
                result = cursor.fetchone()

                if result != None:
                    cursor.execute(
                        """INSERT INTO public.images_room (room_id, url)
                    VALUES (%s, %s)""", (result[0], path_save_image,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
