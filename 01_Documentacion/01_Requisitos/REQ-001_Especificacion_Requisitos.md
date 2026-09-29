# REQ-001: Especificación de Requisitos

## 1. Identificación del Documento / Elemento de Configuración (CI)
* **ID del CI:** CI-REQ-001
* **Proyecto:** BibliotecaPréstamos
* **Versión:** 1.0
* **Estado:** En revisión
* **Fecha:** 23/09/2026
* **Responsable:** Administrador

---

## 2. Historial de Versiones
| Versión | Fecha | Descripción del Cambio | Autor / Responsable |
| :---: | :---: | :--- | :--- |
| **1.0** | 23/09/2026 | Registro e inicio de la línea base del documento de especificación de requisitos. | Administrador |

---

## 3. Propósito y Alcance

### 3.1 Propósito
El propósito de este documento es definir de manera clara y detallada los requisitos del sistema para el proyecto **BibliotecaPréstamos**, sirviendo como base formal para las fases de diseño, desarrollo y pruebas.

### 3.2 Alcance
Este documento aplica a la gestión del sistema de préstamos de la biblioteca. Cubre la funcionalidad necesaria para administrar usuarios, catálogo de libros, préstamos, devoluciones y reportes generales.

---

## 4. Requisitos Funcionales y No Funcionales

### 4.1 Requisitos Funcionales (RF)
* **RF-01:** El sistema debe permitir el registro y gestión de usuarios (estudiantes, docentes, administradores).
* **RF-02:** El sistema debe permitir la consulta, catálogo y control de inventario de libros.
* **RF-03:** El sistema debe gestionar el proceso de préstamo y devolución de libros.
* **RF-04:** El sistema debe generar alertas o notificaciones de préstamos vencidos.

### 4.2 Requisitos No Funcionales (RNF)
* **RNF-01 (Seguridad):** El sistema debe autenticar a todos los usuarios antes de permitir el acceso a las funciones de préstamo.
* **RNF-02 (Rendimiento):** Las búsquedas en el catálogo de libros deben responder en menos de 2 segundos.
* **RNF-03 (Usabilidad):** La interfaz debe ser intuitiva y adaptable a dispositivos móviles y de escritorio.

---

## 5. Criterios de Aceptación
1. Todas las funcionalidades descritas en los Requisitos Funcionales deben pasar el 100% de las pruebas unitarias y de integración.
2. La interfaz debe cumplir con los tiempos de respuesta estipulados en los Requisitos No Funcionales.
3. El documento y el software correspondiente deben contar con la aprobación del cliente / responsable del proyecto.

---

> **NOTA IMPORTANTE DE CONTROL DE CAMBIOS:**  
> Una vez aprobada la presente **Línea Base (Versión 1.0)**, cualquier cambio, adición o modificación posterior a este documento o sus requisitos deberá ser gestionado y controlado formalmente a través del procedimiento de Solicitud de Cambio (CCB / Control de Cambios).