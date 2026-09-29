# TRA-001 - Matriz de Trazabilidad de BookTrack

## Información del elemento de configuración

- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Proyecto: BookTrack
- Versión: 1.0
- Estado: Aprobado para línea base inicial
- Fecha: 29/09/2026
- Responsable: Equipo BookTrack

---

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
| :---: | :---: | :--- | :--- |
| **1.0** | 29/09/2026 | Creación inicial de la matriz de trazabilidad para la v1.0 (Caso 5 BookTrack). | Equipo BookTrack |

---

## 1. Objetivo

Relacionar los requisitos definidos para el proyecto **BookTrack** con los elementos de diseño, código fuente y pruebas que los implementan o verifican.

La matriz permite identificar rápidamente el impacto y qué elementos de configuración (CI) deben revisarse cuando un requisito sea modificado o cuando se tramite una Solicitud de Cambio (CR).

---

## 2. Matriz de trazabilidad inicial

| Requisito | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **RF-01** | Registrar libro / ejemplar | DIS-001 - Entidad Libro | SRC-001 - Gestión de Libros | TST-001 / CP-01 | **Completa** |
| **RF-02** | Consultar disponibilidad | DIS-001 - Entidad Libro | SRC-001 - Gestión de Libros | TST-001 / CP-02 | **Completa** |
| **CR-001** | Renovación de préstamo | DIS-001 - Entidad Préstamo / Reserva | Pendiente de implementación | TST-001 / CP-03 | **Parcial** |
| **CR-002** | Control de retrasos y bloqueo | DIS-001 - Entidad Devolución / Usuario | Pendiente de implementación | TST-001 / CP-04 | **Parcial** |

---

## 3. Relación entre elementos de configuración

La configuración inicial de la línea base v1.0 de **BookTrack** presenta la siguiente estructura de dependencias:

```text
[REQ-001]
   ├──> [DIS-001] (Diseño del Sistema)
   ├──> [SRC-001] (Código Fuente de Gestión)
   ├──> [TST-001] (Plan de Casos de Prueba)
   └──> [TRA-001] (Matriz de Trazabilidad)