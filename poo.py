import mysql.connector

class Conexion:

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='123309',
                port='3306',
                db='personas'
            )
            self.cursor = self.conexion.cursor()
        except Exception as e:
            print(f'A ocurrido un Error de conexion: {e}')



class Funciones(Conexion):
    def ingresa(self):
        super().__init__()
        print('Agregar usuarios'.center(50, '-'))
        nombre = input('Nombre:')
        apellido = input('Apellido:')
        edad = int(input('Edad:'))
        email = input('Email:')
        try:
            sql = 'insert into usuarios(nombre, apellido, edad, email) values(%s,%s,%s,%s)'
            values = (nombre, apellido, edad, email)
            self.cursor.execute(sql, values)
            self.conexion.commit()
            self.registro = self.cursor.rowcount
            return f'Se ha agregado un registro:{self.registro}'
        except Exception as e:
            self.conexion.rollback()
            print(
                f'Ha ocurrido un Erro a la hora de agregar un nuevo usuario:{e}')
        finally:
            self.conexion.close()

    def actualiza(self):
        try:
            super().__init__()
            self.cursor
            sql = 'select * from usuarios'
            self.cursor.execute(sql)
            selectores = self.cursor.fetchall()
            print("USUARIOS".center(50, "-"), '\n')
            for i in selectores:
                print(f'ID:{i}')
        except Exception as e:
            print(f'Ha ocurrido un Erro al mostrar los datos:{e}')

        id_usuarios = int(input('\ningrece el id ID usuario:'))
        nombre = input('Nuevo nombre:')
        apellido = input('Nuevo apellido:')
        edad = int(input('Nueva Edad:'))
        email = input('Nuevo email:')
        try:

            sql = 'update usuarios set nombre=%s, apellido=%s,edad=%s,email=%s where id_usuarios=%s'
            values = (nombre, apellido, edad, email, id_usuarios)
            self.cursor.execute(sql, values)
            self.conexion.commit()
            self.registro = self.cursor.rowcount
            return f'nuevo datos atualizados:{self.registro}'
        except Exception as e:
            self.conexion.rollback()
            print(
                f'Ha ocurrido un error a la hora de actualizar la información:{e}')
        finally:
            self.conexion.close()

    def verDatos(self):
        super().__init__()
        try:
            with self.cursor as cursor:
                self.cursor
                sql = 'select * from usuarios'
                self.cursor.execute(sql)
                selectores = self.cursor.fetchall()
                print("USUARIOS".center(50, "-"), '\n')
                for i in selectores:
                    print(f'ID:{i}')
        except Exception as e:
            print(f'Ha ocurrido un Erro al mostrar los datos:{e}')
        finally:
            self.conexion.close()

    def Eliminar(self):
        print('Eliminar usuarios'.center(50, '-'))
        try:
            super().__init__()
            self.cursor
            sql = 'select * from usuarios'
            self.cursor.execute(sql)
            selectores = self.cursor.fetchall()
            print("USUARIOS".center(50, "-"), '\n')
            for i in selectores:
                print(f'ID:{i}')
        except Exception as e:
            print(f'Ha ocurrido un Erro al mostrar los datos:{e}')
        id_usuarios = int(input('\ningrese el, id usuario a eliminar:'))

        try:
            sql = 'delete  from usuarios where id_usuarios =%s'
            self.cursor.execute(sql, (id_usuarios,))
            self.conexion.commit()
            self.registro = self.cursor.rowcount
            return f' Datos Eliminados:{self.registro}'
        except Exception as e:
            print(f'ha ocurrido un erro al eliminar los datos:{e}')
