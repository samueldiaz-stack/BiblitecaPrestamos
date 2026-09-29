# SRC-001 - Gestión de Libros (BookTrack)
# Proyecto: BookTrack
# Versión: 1.0
# Estado: Aprobado para línea base inicial
# Fecha: 29/09/2026
# Responsable: Equipo BookTrack


class Libro:
    def __init__(self, id_libro, titulo, isbn, estado_ejemplar="Disponible"):
        self.id_libro = id_libro
        self.titulo = titulo
        self.isbn = isbn
        self.estado_ejemplar = estado_ejemplar

    def mostrar_informacion(self):
        return {
            "id_libro": self.id_libro,
            "titulo": self.titulo,
            "isbn": self.isbn,
            "estado_ejemplar": self.estado_ejemplar
        }


def registrar_libro(id_libro, titulo, isbn):
    libro = Libro(
        id_libro=id_libro,
        titulo=titulo,
        isbn=isbn,
        estado_ejemplar="Disponible"
    )
    return libro