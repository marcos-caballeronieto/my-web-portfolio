# My Web Portfolio

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.2-092E20?style=flat&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=flat&logo=bootstrap&logoColor=white)
![Deployed](https://img.shields.io/badge/Status-Live-success)

[🇺🇸 English](#english) | [🇪🇸 Español](#español)

---

<a name="english"></a>
## 🇺🇸 English

### 🚀 About the Project
**Live Demo:** https://marcoscaballero.pythonanywhere.com/

This portfolio represents my journey as a **Biomedical & Mechanical Engineering student** passionate about software development as well as other proyects and fields. Unlike static templates, this is a fully dynamic web application built from scratch to showcase not just *what* I've done, but *how* I solve problems using code.

It serves as a central hub for my academic achievements, certificates, and technical projects, designed with a focus on **User Experience (UX)** and **Content Management**.

### 🏗️ Technical Architecture

This project follows the **Model-View-Template (MVT)** architectural pattern standard in Django, ensuring a clean separation of concerns:

* **Full-Stack Logic:** Implemented Model-View-Template (MVT) architecture for clean code separation.
* **Backend Engine & CMS:** Custom Markdown parsing, code syntax highlighting (Pygments), and CKEditor 5 integration.
* **Database & Data-Driven Architecture:** Created efficient SQLite relationships and implemented ORM filtering via URL parameters with a custom relevance metric.
* **Frontend & UI/UX:** Responsive Bootstrap 5 interface enhanced with `Particles.js` and `Mermaid.js` for dynamic diagram rendering, plus a lightweight, zero-reload bilingual toggle (EN/ES) using Vanilla JavaScript.
* **Quality Assurance:** Authored automated unit tests (`tests.py`) to validate model constraints, views, and routing logic.
* **DevOps Basics:** Configured WSGI and static files for a real-world Linux deployment on PythonAnywhere.



### 💡 Key Challenges & Solutions

#### 1. Rich Content & Markdown Support (Custom CMS)
**The Challenge:** I needed a way to upload complex project descriptions, including custom Markdown, code snippets, and formatted text, without writing raw HTML every time.
**The Solution:** I integrated **CKEditor 5** into the Django Admin and wrote custom template filters using Python's `re` and `markdown` libraries (`markdown_filters.py`). This allows the system to seamlessly parse Markdown and apply syntax highlighting (via Pygments) to code blocks directly from the database.

#### 2. Smart Filtering & Custom Relevance System
**The Challenge:** Users needed to find relevant projects quickly, and the default chronological order wasn't always the best way to showcase my top work.
**The Solution:** I implemented a backend filtering system in `views.py` that processes URL query parameters (`?category=AI`). To ensure the best projects appear first, I designed a custom **"Relevance" metric** within the Django ORM, allowing me to dynamically query, filter by category, and sort the content efficiently.

#### 3. Lightweight Bilingual Support
**The Challenge:** Providing an English/Spanish experience without the overhead of heavy backend translation libraries for static content.
**The Solution:** Designed a lightweight JavaScript toggle system in the frontend (`about.html`). This allows for instant language switching for the "About me" section without requiring a page reload or complex session management.

#### 4. Production Deployment & Security
**The Challenge:** Moving the application from a local development environment to a live Linux server while maintaining security.
**The Solution:** Configured WSGI for application serving, managed static asset collection (`collectstatic`) to bypass Django for faster load times, and secured sensitive settings using environment variables.

---

<a name="español"></a>
## 🇪🇸 Español

### 🚀 Sobre el Proyecto
**Ver online:** https://marcoscaballero.pythonanywhere.com/

Este portafolio representa mi trayectoria como **estudiante de Ingeniería Biomédica y Mecánica** apasionado por el desarrollo de software así como por otros proyectos y campos. A diferencia de las plantillas estáticas, esta es una aplicación web dinámica construida desde cero para demostrar no solo *qué* he hecho, sino *cómo* resuelvo problemas mediante código.

Actúa como un centro unificado para mis logros académicos, certificados y proyectos técnicos, diseñado con un enfoque en la **Experiencia de Usuario (UX)** y la **Gestión de Contenido**.

### 🏗️ Arquitectura Técnica

El proyecto sigue el patrón arquitectónico **Modelo-Vista-Plantilla (MVT)** estándar en Django, asegurando una separación clara de responsabilidades:

* **Lógica Full-Stack:** Implementación de la arquitectura Modelo-Vista-Plantilla (MVT) para una separación limpia del código.
* **Motor Backend y CMS:** Procesamiento de Markdown personalizado, resaltado de sintaxis de código (Pygments) e integración de CKEditor 5.
* **Base de Datos y Arquitectura de Datos:** Creación de relaciones SQLite eficientes e implementación de filtrado ORM mediante parámetros de URL con una métrica de relevancia personalizada.
* **Frontend y UI/UX:** Interfaz responsiva con Bootstrap 5, mejorada con `Particles.js` y `Mermaid.js` para renderizado dinámico de diagramas, más un toggle bilingüe (EN/ES) ligero y sin recarga usando JavaScript puro.
* **Aseguramiento de Calidad (QA):** Creación de pruebas unitarias automatizadas (`tests.py`) para validar restricciones de modelos, vistas y lógica de enrutamiento.
* **Fundamentos DevOps:** Configuración de WSGI y archivos estáticos para un despliegue real en servidor Linux (PythonAnywhere).

### 💡 Principales Desafíos y Soluciones

#### 1. Soporte Avanzado de Markdown y Código (CMS Personalizado)
**El Desafío:** Necesitaba subir descripciones complejas de proyectos, incluyendo Markdown personalizado, bloques de código y formato libre, sin escribir HTML crudo cada vez.
**La Solución:** Integré **CKEditor 5** en el panel de Admin y programé filtros de plantillas personalizados (`markdown_filters.py`) usando expresiones regulares. Esto permite al sistema procesar Markdown y aplicar resaltado de sintaxis (con Pygments) a los bloques de código directamente desde la base de datos.

#### 2. Filtrado Inteligente y Sistema de Relevancia
**El Desafío:** Los usuarios debían poder encontrar proyectos específicos rápidamente, y el orden cronológico por defecto no siempre era la mejor forma de destacar mi trabajo principal.
**La Solución:** Implementé un sistema de filtrado en el backend (`views.py`) que lee parámetros de la URL (`?category=AI`). Para asegurar que los mejores proyectos salgan primero, diseñé una métrica personalizada de **"Relevancia"** en el modelo, utilizando el ORM de Django para filtrar por categoría y ordenar el contenido de forma ultra eficiente.

#### 3. Soporte Bilingüe Ligero
**El Desafío:** Ofrecer una experiencia en inglés y español sin la sobrecarga de librerías de traducción complejas para contenido estático.
**La Solución:** Diseñé un sistema de alternancia ("toggle") en JavaScript dentro del frontend (`about.html`). Esto permite un cambio de idioma instantáneo en la sección "Sobre mí" sin necesidad de recargar la página o gestionar sesiones complejas.

#### 4. Despliegue en Producción y Seguridad
**El Desafío:** Mover la aplicación desde un entorno de desarrollo local a un servidor Linux real manteniendo la seguridad.
**La Solución:** Configuré WSGI para servir la aplicación, gestioné la recolección de archivos estáticos (`collectstatic`) para que el servidor web los entregue más rápido saltándose a Django, y aseguré las variables de entorno para una configuración pública y segura.

---
