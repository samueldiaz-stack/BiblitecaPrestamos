# TRA-001 - Matriz de Trazabilidad de BookTrack

## Información del elemento de configuración

- Código del CI: TRA-001
- Nombre: Matriz de Trazabilidad
- Proyecto: BookTrack
- Versión: 1.2
- Estado: Aprobado para Línea Base LB 1.2
- Fecha: 29/09/2026
- Responsable: Equipo BookTrack

---

## Historial de versiones

| Versión | Fecha | Descripción del cambio | Responsable |
| :---: | :---: | :--- | :--- |
| **1.0** | 29/09/2026 | Creación inicial de la matriz de trazabilidad para la v1.0 (LB 1.0). | Equipo BookTrack |
| **1.1** | 29/09/2026 | Actualización por incorporación de CR-001 (Renovación de préstamo) para LB 1.1. | Equipo BookTrack |
| **1.2** | 29/09/2026 | Actualización por incorporación de CR-002 (Control de retrasos) y rechazo de CR-003 para LB 1.2. | Equipo BookTrack |

---

## 1. Objetivo

Relacionar los requisitos y solicitudes de cambio definidos para el proyecto **BookTrack** con los elementos de diseño, código fuente, pruebas y líneas base que los implementan o verifican.

---

## 2. Matriz de trazabilidad consolidada (LB 1.2)

| Requisito / Cambio | Descripción | Diseño relacionado | Código relacionado | Prueba relacionada | Estado |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **RF-01** | Registrar libro / ejemplar | DIS-001 - Entidad Libro | SRC-001 - `registrar_libro()` | TST-001 / CP-01 | **Completa** |
| **RF-02** | Consultar disponibilidad | DIS-001 - Entidad Libro | SRC-001 - `consultar_estado()` | TST-001 / CP-02 | **Completa** |
| **CR-001** | Renovación de préstamo (Max 1) | DIS-001 - Entidad Préstamo / Reserva | SRC-001 - `renovar_prestamo()` | TST-001 / CP-03 | **Completa** |
| **CR-002** | Control de retrasos y bloqueo | DIS-001 - Entidad Usuario / Devolución | SRC-001 - `realizar_prestamo()`, `realizar_devolucion()` | TST-001 / CP-04 | **Completa** |
| **CR-003** | Borrado del historial de préstamos | N/A (Rechazado por riesgo SCM) | N/A (Sin cambios en código) | N/A (Sin cambios en pruebas) | **Rechazado** |

---

## 3. Matriz de evolución de CIs por Línea Base

| Elemento de Configuración (CI) | Versión en LB 1.0 | Versión en LB 1.1 (CR-001) | Versión en LB 1.2 (CR-002) | Estado Tras CR-003 |
| :--- | :---: | :---: | :---: | :---: |
| **REQ-001** (Especificación de Requisitos) | 1.0 | 1.1 | 1.2 | 1.2 (Sin cambio) |
| **DIS-001** (Diseño del Sistema) | 1.0 | 1.1 | 1.2 | 1.2 (Sin cambio) |
| **SRC-001** (Código Fuente) | 1.0 | 1.1 | 1.2 | 1.2 (Sin cambio) |
| **TST-001** (Plan de Pruebas) | 1.0 | 1.1 | 1.2 | 1.2 (Sin cambio) |
| **TRA-001** (Matriz de Trazabilidad) | 1.0 | 1.1 | 1.2 | 1.2 (Sin cambio) |

---

## 4. Relación y dependencias entre CIs (Línea Base Final)

```text
[CR-001] ──> [REQ-001 v1.1] ──> [DIS-001 v1.1] ──> [SRC-001 v1.1] ──> [TST-001 v1.1] ──> [LB 1.1]
[CR-002] ──> [REQ-001 v1.2] ──> [DIS-001 v1.2] ──> [SRC-001 v1.2] ──> [TST-001 v1.2] ──> [LB 1.2]
[CR-003] ──> [Análisis de Impacto] ──> Decisión: RECHAZADO ──> (Conserva LB 1.2)