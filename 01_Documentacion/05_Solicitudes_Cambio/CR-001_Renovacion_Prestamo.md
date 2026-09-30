# CR-001 - Solicitud de Cambio: Renovación de Préstamo

## 1. Registro de la solicitud
- **Código:** CR-001
- **Fecha:** 29/09/2026
- **Solicitante:** Biblioteca / Usuario
- **Prioridad:** Media
- **Estado:** Aprobada e Implementada

## 2. Descripción y Justificación
Permitir que un usuario pueda renovar una sola vez un préstamo de libro activo, siempre y cuando el ejemplar no cuente con una reserva pendiente de otro usuario.

## 3. Análisis de Impacto
- **Necesidad / Alcance:** Extender la vigencia de un préstamo existente.
- **CIs Afectados:**
  - `REQ-001` (Añadir RF-03: Regla de renovación).
  - `DIS-001` (Actualizar diagrama/entidad Préstamo con contador de renovaciones y estado de reserva).
  - `SRC-001` (Añadir método `renovar_prestamo()` en clase `Libro`).
  - `TST-001` (Añadir caso de prueba CP-03).
  - `TRA-001` (Trazar CR-001 en la matriz).
- **Riesgos:** Permitir renovaciones infinitas si no se valida el límite de 1 intento.

## 4. Decisión
- **Decisión:** APROBADA por el Comité de Cambios (CCB).
- **Línea base resultante:** LB 1.1