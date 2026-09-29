# DIS-001 - Diseño del Sistema BookTrack

## Información del elemento de configuración
- Código del CI: DIS-001
- Nombre: Diseño del Sistema BookTrack
- Proyecto: BookTrack
- Versión: 1.0
- Estado: Aprobado para línea base inicial
- Fecha: 29/09/2026
- Responsable: Equipo BookTrack

---

## Historial de versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :---: | :---: | :--- | :--- |
| **1.0** | 29/09/2026 | Diseño inicial del sistema y modelo de datos para el PMV (Caso 5 BookTrack). | Equipo BookTrack |

---

## 1. Descripción general
BookTrack organiza el sistema de gestión de préstamos bibliotecarios en cuatro componentes y procesos principales:
1. **Gestión de usuarios:** Registro y control del estado del usuario (bloqueos por mora).
2. **Gestión de libros / ejemplares:** Registro y consulta de disponibilidad del catálogo.
3. **Gestión de préstamos y renovaciones:** Registro de salidas, control de reservas y renovaciones (CR-001).
4. **Gestión de devoluciones y retrasos:** Registro de entregas, cálculo de días de atraso y bloqueo por mora (CR-002).

---

## 2. Entidades principales y atributos

### 2.1 Usuario
Representa a los socios o clientes de la biblioteca.
* **id_usuario:** Número entero (Clave Primaria, Autoincremental) - Identificador único del usuario.
* **nombre:** Cadena de texto (VARCHAR 50) - Nombre completo del usuario.
* **documento_identidad:** Cadena de texto (VARCHAR 20, Único) - Cédula o identificación oficial.
* **correo:** Cadena de texto (VARCHAR 100) - Correo electrónico de contacto.
* **estado_usuario:** Cadena de texto (Ej: Habilitado, Bloqueado) - Estado del usuario según devoluciones vencidas (CR-002).

### 2.2 Libro / Ejemplar
Representa las obras y ejemplares físicos disponibles en la biblioteca.
* **id_libro:** Número entero (Clave Primaria, Autoincremental) - Identificador único del libro/ejemplar.
* **titulo:** Cadena de texto (VARCHAR 150) - Título del libro.
* **isbn:** Cadena de texto (VARCHAR 20) - Código ISBN del libro.
* **estado_ejemplar:** Cadena de texto (Ej: Disponible, Prestado, En Reserva) - Estado del ejemplar para consultas de disponibilidad.

### 2.3 Préstamo
Representa el evento en que un libro es entregado temporalmente a un usuario.
* **id_prestamo:** Número entero (Clave Primaria, Autoincremental) - Identificador del préstamo.
* **id_usuario:** Número entero (Clave Foránea -> Usuario) - Usuario que solicita el libro.
* **id_libro:** Número entero (Clave Foránea -> Libro) - Ejemplar prestado.
* **fecha_prestamo:** Fecha (DATE) - Fecha de inicio del préstamo.
* **fecha_vencimiento:** Fecha (DATE) - Fecha límite para la devolución.
* **renovado:** Booleano (TRUE/FALSE) - Indica si ya hizo la única renovación permitida (CR-001).
* **estado_prestamo:** Cadena de texto (Ej: Activo, Devuelto, Vencido).

### 2.4 Devolución
Representa el registro formal de retorno de un ejemplar prestado.
* **id_devolucion:** Número entero (Clave Primaria, Autoincremental) - Identificador de la devolución.
* **id_prestamo:** Número entero (Clave Foránea -> Préstamo) - Préstamo que finaliza.
* **fecha_devolucion:** Fecha (DATE) - Fecha real de entrega.
* **dias_atraso:** Número entero - Cantidad de días de retraso calculados (CR-002).

### 2.5 Reserva (Soporte para CR-001)
Representa las solicitudes pendientes sobre un libro.
* **id_reserva:** Número entero (Clave Primaria, Autoincremental).
* **id_libro:** Número entero (Clave Foránea -> Libro).
* **id_usuario:** Número entero (Clave Foránea -> Usuario).
* **estado_reserva:** Cadena de texto (Ej: Pendiente, Completada, Cancelada).

---

## 3. Flujos del sistema

### 3.1 Flujo de Registro de Usuarios y Libros
1. El usuario administrador registra un nuevo usuario o un nuevo ejemplar de libro en el catálogo.
2. El sistema valida los datos requeridos (documento único, datos del libro).
3. El libro se registra inicialmente con el estado `Disponible`.

### 3.2 Flujo de Realización de Préstamo
1. Se selecciona un usuario y un ejemplar disponible.
2. **Validación de bloqueo (CR-002):** El sistema verifica si el usuario tiene devoluciones vencidas o su estado es `Bloqueado`. Si está bloqueado, se rechaza la operación.
3. Si el usuario está `Habilitado` y el libro está `Disponible`, se genera el registro del Préstamo.
4. El estado del libro cambia a `Prestado`.

### 3.3 Flujo de Renovación de Préstamo (CR-001)
1. El usuario solicita la renovación de un préstamo activo.
2. El sistema valida dos condiciones obligatorias:
   - Que el préstamo **no haya sido renovado previamente** (`renovado == FALSE`).
   - Que el libro **no tenga una reserva pendiente** (`estado_reserva != Pendiente`).
3. Si cumple ambas condiciones, el sistema aprueba la renovación, actualiza la `fecha_vencimiento` y marca `renovado = TRUE`.

### 3.4 Flujo de Devolución y Control de Retrasos (CR-002)
1. El usuario entrega el libro prestado.
2. El sistema registra la fecha actual en `fecha_devolucion` y cambia el estado del libro a `Disponible`.
3. Se calculan los `dias_atraso` comparando `fecha_devolucion` con `fecha_vencimiento`.
4. Si `dias_atraso > 0`, el sistema actualiza automáticamente el `estado_usuario` a `Bloqueado` para prevenir nuevos préstamos.
5. **Conservación del historial:** El registro de la devolución y del préstamo se **conserva permanentemente** en la base de datos para garantizar la trazabilidad y generación de estadísticas (rehusando el borrado solicitado en CR-003).

---

## 4. Trazabilidad / Relación con los Requisitos

| Componente / Entidad / Flujo | Requisito / Solicitud Relacionada | Descripción de la Relación |
| :--- | :---: | :--- |
| **Entidad Libro / Flujo 3.1** | **PMV - Registrar Libro y Consultar Disponibilidad** | Permite dar de alta ejemplares y consultar su estado (`Disponible`, `Prestado`). |
| **Entidades Usuario, Préstamo / Flujo 3.2** | **PMV - Registrar Usuario y Realizar Préstamo** | Permite efectuar la salida de libros vinculados a un usuario. |
| **Entidad Devolución / Flujo 3.4** | **PMV - Devolver Exemplar** | Permite recibir los libros y dar por finalizado el préstamo activo. |
| **Atributo `renovado` / Entidad Reserva / Flujo 3.3** | **Solicitud 1: CR-001 (Renovación)** | Garantiza que un usuario solo renueve una vez y verifica la ausencia de reservas pendientes antes de aprobar. |
| **Atributo `dias_atraso` / `estado_usuario` / Flujo 3.2 y 3.4** | **Solicitud 2: CR-002 (Control de retrasos)** | Bloquea automáticamente al usuario para impedir nuevos préstamos si registra devoluciones con mora. |
| **Conservación del Historial (Préstamo y Devolución)** | **Solicitud 3: CR-003 (Rechazo de borrado)** | Mantiene todos los registros históricos en la BD asegurando la trazabilidad y estadísticas de la biblioteca. |