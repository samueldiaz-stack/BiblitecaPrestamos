# SRC-001 - Gestión de Libros y Préstamos (BookTrack)
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
        self.estado_ejemplar = estado_ejemplar  # Disponible, Prestado

    def realizar_prestamo(self):
        """Cambia el estado del ejemplar a Prestado si está disponible."""
        if self.estado_ejemplar == "Disponible":
            self.estado_ejemplar = "Prestado"
            return True, f"El libro '{self.titulo}' ha sido prestado con éxito."
        return False, f"El libro '{self.titulo}' no está disponible para préstamo."

    def realizar_devolucion(self):
        """Cambia el estado del ejemplar a Disponible."""
        if self.estado_ejemplar == "Prestado":
            self.estado_ejemplar = "Disponible"
            return True, f"El libro '{self.titulo}' ha sido devuelto correctamente."
        return False, f"El libro '{self.titulo}' ya se encuentra disponible."

    def consultar_estado(self):
        """Devuelve la información detallada y estado actual del ejemplar."""
        return {
            "id_libro": self.id_libro,
            "titulo": self.titulo,
            "isbn": self.isbn,
            "estado_ejemplar": self.estado_ejemplar
        }


# --- Funciones de Interfaz / Control ---

def registrar_libro(id_libro, titulo, isbn):
    """Crea y registra un nuevo ejemplar en estado Disponible."""
    return Libro(id_libro=id_libro, titulo=titulo, isbn=isbn)