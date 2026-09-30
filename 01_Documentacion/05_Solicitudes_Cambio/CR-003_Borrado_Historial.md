# CR-003 - Solicitud de Cambio: Borrado del Historial de Préstamos

## 1. Registro de la solicitud
- **Código:** CR-003
- **Fecha:** 29/09/2026
- **Solicitante:** Gestión Interna
- **Prioridad:** Baja
- **Estado:** RECHAZADA

## 2. Descripción
Se propone eliminar automáticamente el registro de cada préstamo inmediatamente después de que el libro sea devuelto.

## 3. Análisis de Impacto y Justificación del Rechazo
- **Análisis de Riesgos:** 
  - **Pérdida de Trazabilidad:** Al eliminar los registros de préstamos devueltos, el sistema pierde el historial de uso de los libros y la auditoría de usuarios.
  - **Imposibilidad de Estadísticas:** Se pierde la capacidad de generar reportes sobre los libros más solicitados o el comportamiento de los usuarios.
  - **Violación de Principios de SCM e Integridad:** En gestión de la configuración y auditoría de software, la eliminación de transacciones destruye la evidencia operativa.
- **Decisión del CCB:** **RECHAZADA UNÁNIMEMENTE**.
- **Efecto sobre Líneas Base:** No genera cambios en el código ni en la documentación. Se conserva la versión actual **LB 1.2**.