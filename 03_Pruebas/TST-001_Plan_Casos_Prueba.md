# TST-001 - Plan y Casos de Prueba del Sistema BookTrack

## Información del elemento de configuración
- Código del CI: TST-001
- Nombre: Plan y Casos de Prueba
- Proyecto: BookTrack
- Versión: 1.0
- Estado: Aprobado para línea base inicial
- Fecha: 29/09/2026
- Responsable: Equipo BookTrack

---

## Historial de versiones
| Versión | Fecha | Descripción del cambio | Responsable |
| :---: | :---: | :--- | :--- |
| **1.0** | 29/09/2026 | Definición inicial de casos de prueba y trazabilidad para el PMV (Caso 5 BookTrack). | Equipo BookTrack |

---

## 1. Descripción general
Este documento define los casos de prueba unitarios y funcionales para validar las funcionalidades del PMV y las solicitudes de cambio (CR) del sistema **BookTrack**, asegurando su coherencia con los documentos `REQ-001`, `DIS-001` y el código fuente `SRC-001`.

---

## 2. Casos de prueba

### CP-01 - Registrar nuevo libro en el sistema
- **Requisito asociado:** PMV - Registro de libro
- **Diseño asociado:** DIS-001 - Entidad Libro / Flujo 3.1
- **Código asociado:** `SRC-001_Gestion_Libros.py` (`registrar_libro`)

**Precondiciones:**
- El ISBN y el identificador del libro no deben existir previamente en el catálogo.

**Resultado esperado:**
El libro se registra correctamente con el estado inicial `Disponible`.

**Estado esperado:** Aprobado.

---

### CP-02 - Consultar disponibilidad de un ejemplar
- **Requisito asociado:** PMV - Consultar disponibilidad
- **Diseño asociado:** DIS-001 - Entidad Libro (`estado_ejemplar`)
- **Código asociado:** `SRC-001_Gestion_Libros.py` (`mostrar_informacion`)

**Precondiciones:**
- El libro debe estar registrado en el sistema.

**Resultado esperado:**
El sistema retorna los datos del libro indicando su estado actual (ej: `Disponible` o `Prestado`).

**Estado esperado:** Aprobado.

---

### CP-03 - Renovación de préstamo (CR-001)
- **Requisito asociado:** Solicitud 1: CR-001 - Renovación
- **Diseño asociado:** DIS-001 - Entidad Préstamo / Reserva / Flujo 3.3

**Precondiciones:**
- El préstamo debe estar activo y no haber sido renovado previamente.
- El libro no debe tener una reserva pendiente de otro usuario.

**Resultado esperado:**
El sistema permite renovar el préstamo una única vez y actualiza la fecha de vencimiento.

**Estado esperado:** Aprobado.

---

### CP-04 - Control de retrasos y bloqueo por mora (CR-002)
- **Requisito asociado:** Solicitud 2: CR-002 - Control de retrasos
- **Diseño asociado:** DIS-001 - Entidad Devolución / Usuario / Flujo 3.4

**Precondiciones:**
- El usuario registra una devolución con fecha posterior a la fecha de vencimiento.

**Resultado esperado:**
El sistema calcula los días de atraso y cambia el estado del usuario a `Bloqueado` para impedir nuevos préstamos.

**Estado esperado:** Aprobado.

---

## 3. Trazabilidad de pruebas

| Caso de prueba | Requisito | Diseño | Código |
| :--- | :--- | :--- | :--- |
| **CP-01** | PMV - Registro de libro | DIS-001 | SRC-001 |
| **CP-02** | PMV - Consultar disponibilidad | DIS-001 | SRC-001 |
| **CP-03** | CR-001 - Renovación | DIS-001 | No aplica en esta versión |
| **CP-04** | CR-002 - Control de retrasos | DIS-001 | No aplica en esta versión |

---

## 4. Observaciones de configuración

Este documento constituye el Elemento de Configuración **TST-001**.

Los casos de prueba deberán actualizarse cuando una solicitud de cambio modifique los requisitos, el diseño o el código relacionado.