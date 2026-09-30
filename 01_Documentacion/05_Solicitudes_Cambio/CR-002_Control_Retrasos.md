# CR-002 - Solicitud de Cambio: Control de Retrasos y Bloqueo

## 1. Registro de la solicitud
- **Código:** CR-002
- **Fecha:** 29/09/2026
- **Solicitante:** Administración de Biblioteca
- **Prioridad:** Alta
- **Estado:** Aprobada e Implementada

## 2. Descripción y Justificación
Identificar los días de atraso en la devolución de libros y bloquear temporalmente a los usuarios morosos para impedir nuevos préstamos hasta que regularicen su situación.

## 3. Análisis de Impacto
- **Necesidad / Alcance:** Controlar la mora e incentivar la devolución oportuna.
- **CIs Afectados:**
  - `REQ-001` (Añadir RF-04: Sanción por atraso y bloqueo).
  - `DIS-001` (Agregar atributo `dias_atraso` y estado `Bloqueado` en Usuario).
  - `SRC-001` (Añadir método `calcular_dias_atraso()` y verificación de bloqueo).
  - `TST-001` (Añadir caso de prueba CP-04).
  - `TRA-001` (Actualizar trazabilidad).
- **Riesgos:** Inconsistencia en el cálculo de fechas si no se validan los días transcurridos.

## 4. Decisión
- **Decisión:** APROBADA por el Comité de Cambios (CCB).
- **Línea base resultante:** LB 1.2