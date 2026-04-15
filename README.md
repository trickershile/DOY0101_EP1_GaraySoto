EP1: Microservicio FastAPI - Ingeniería DevOps

Descripción del Proyecto
Este repositorio contiene la primera evaluación parcial de la asignatura **DOY0101**. Se presenta un microservicio desarrollado en **Python** utilizando el framework **FastAPI**, enfocado en implementar un flujo de trabajo profesional bajo la cultura DevOps.



Buenas Prácticas y Convenciones

Estrategia de Ramificación (GitFlow)
Se implementó el modelo de trabajo **GitFlow** para garantizar la trazabilidad y la estabilidad del código en producción:
* **`main`**: Contiene únicamente versiones estables y verificadas.
* **`develop`**: Rama principal para la integración de nuevas funcionalidades.
* **`feature/`**: Ramas temporales para el desarrollo de características específicas.
* **`hotfix/`**: Ramas de emergencia para corregir errores críticos detectados en `main`.

Convención de Commits
Para el historial de cambios, se utilizó el estándar **Conventional Commits**, lo que permite una auditoría clara del progreso:
* `feat`: Nueva funcionalidad (ej: `feat: agregar endpoint de salud`).
* `fix`: Corrección de errores (ej: `fix: resolver validación de API KEY`).
* `chore`: Tareas de mantenimiento o configuración (ej: `chore: configurar GitHub Actions`).



Automatización (CI/CD)
El proyecto cuenta con un pipeline de **Integración Continua** configurado mediante **GitHub Actions**. 

**El flujo automatizado realiza:**
1.  **Checkout:** Descarga del código fuente.
2.  **Setup:** Configuración del entorno Python 3.9.
3.  **Install:** Instalación de dependencias críticas (`fastapi`, `uvicorn`).
4.  **Verify:** Verificación de integridad del microservicio.
