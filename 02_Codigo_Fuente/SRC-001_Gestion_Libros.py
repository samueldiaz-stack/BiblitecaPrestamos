# SRC-001 - Gestión de Libros, Préstamos y Sanciones (BookTrack)
# Proyecto: BookTrack
# Versión: 1.2
# Estado: Aprobado
# Fecha: 29/09/2026
# Responsable: Equipo BookTrack


class Libro:
    def __init__(self, id_libro, titulo, isbn, estado_ejemplar="Disponible"):
        self.id_libro = id_libro
        self.titulo = titulo
        self.isbn = isbn
        self.estado_ejemplar = estado_ejemplar  # Disponible, Prestado
        self.renovado = False                   # CR-001: Indicador de renovación (Max 1)
        self.tiene_reserva = False              # CR-001: Reserva pendiente

    def realizar_prestamo(self, usuario_bloqueado=False):
        """CR-002: Realiza el préstamo solo si el usuario no está bloqueado."""
        if usuario_bloqueado:
            return False, "Préstamo denegado: El usuario se encuentra bloqueado por mora."
        
        if self.estado_ejemplar == "Disponible":
            self.estado_ejemplar = "Prestado"
            self.renovado = False
            return True, f"El libro '{self.titulo}' ha sido prestado con éxito."
        return False, f"El libro '{self.titulo}' no está disponible para préstamo."

    def renovar_prestamo(self):
        """CR-001: Permite renovar 1 vez si no hay reserva pendiente."""
        if self.estado_ejemplar != "Prestado":
            return False, "No se puede renovar un libro que no está en préstamo."
        if self.tiene_reserva:
            return False, "No se puede renovar: El libro tiene una reserva pendiente."
        if self.renovado:
            return False, "No se puede renovar: Ya se utilizó el límite máximo de 1 renovación."
        
        self.renovado = True
        return True, f"Préstamo del libro '{self.titulo}' renovado exitosamente."

    def realizar_devolucion(self, dias_atraso=0):
        """CR-002: Procesa devolución y calcula sanciones si hay mora."""
        if self.estado_ejemplar == "Prestado":
            self.estado_ejemplar = "Disponible"
            self.renovado = False
            
            if dias_atraso > 0:
                return True, f"Devolución registrada. Atención: Presenta {dias_atraso} días de atraso. Usuario bloqueado."
            return True, f"El libro '{self.titulo}' ha sido devuelto a tiempo sin sanciones."
        return False, f"El libro '{self.titulo}' ya se encuentra disponible."

    def consultar_estado(self):
        """Devuelve el estado completo del ejemplar."""
        return {
            "id_libro": self.id_libro,
            "titulo": self.titulo,
            "isbn": self.isbn,
            "estado_ejemplar": self.estado_ejemplar,
            "renovado": self.renovado,
            "tiene_reserva": self.tiene_reserva
        }


def registrar_libro(id_libro, titulo, isbn):
    """Crea y registra un nuevo ejemplar."""
    return Libro(id_libro=id_libro, titulo=titulo, isbn=isbn)