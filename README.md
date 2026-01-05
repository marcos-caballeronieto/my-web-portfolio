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

* **Backend (Django 5):** Handles business logic, URL routing, and database interactions.
* **Database (SQLite):** Selected for its efficiency in read-heavy, low-concurrency environments like a personal portfolio.
* **Frontend (Bootstrap 5 + Custom CSS):** A responsive interface enhanced with `Particles.js` for visual depth and `Mermaid.js` for dynamic diagram rendering.



### 💡 Key Challenges & Solutions

#### 1. Rich Content Management without HTML
**The Challenge:** I needed a way to upload complex project descriptions (including code blocks and bold text) via the Admin panel without writing raw HTML every time.
**The Solution:** I integrated **CKEditor 5** directly into the `Project` model. This required overriding standard Admin styles to ensure readability in dark/light modes.

#### 2. Smart Project Filtering
**The Challenge:** Users needed to find relevant projects quickly without navigating multiple pages.
**The Solution:** Implemented a backend filtering system in `views.py` that processes query parameters (`?category=AI`). The system efficiently queries the database using Django ORM to return only categorized projects sorted by a custom "relevance" metric.

#### 3. Lightweight Bilingual Support
**The Challenge:** Providing an English/Spanish experience without the overhead of heavy backend translation libraries for static content.
**The Solution:** Designed a lightweight JavaScript toggle system in the frontend (`about.html`). This allows for instant language switching for the "About me" section without requiring a page reload or complex session management.

---

<a name="español"></a>
## 🇪🇸 Español

### 🚀 Sobre el Proyecto
**Ver online:** https://marcoscaballero.pythonanywhere.com/

Este portafolio representa mi trayectoria como **estudiante de Ingeniería Biomédica y Mecánica** apasionado por el desarrollo de software así como por otros proyectos y campos. A diferencia de las plantillas estáticas, esta es una aplicación web dinámica construida desde cero para demostrar no solo *qué* he hecho, sino *cómo* resuelvo problemas mediante código.

Actúa como un centro unificado para mis logros académicos, certificados y proyectos técnicos, diseñado con un enfoque en la **Experiencia de Usuario (UX)** y la **Gestión de Contenido**.

### 🏗️ Arquitectura Técnica

El proyecto sigue el patrón arquitectónico **Modelo-Vista-Plantilla (MVT)** estándar en Django, asegurando una separación clara de responsabilidades:

* **Backend (Django 5):** Gestiona la lógica de negocio, el enrutamiento de URLs y las interacciones con la base de datos.
* **Base de Datos (SQLite):** Seleccionada por su eficiencia en entornos de mucha lectura y baja concurrencia como un portafolio personal.
* **Frontend (Bootstrap 5 + CSS Personalizado):** Interfaz responsiva mejorada con `Particles.js` para profundidad visual y `Mermaid.js` para renderizado dinámico de diagramas.

### 💡 Principales Desafíos y Soluciones

#### 1. Gestión de Contenido Rico (Rich Text)
**El Desafío:** Necesitaba subir descripciones complejas de proyectos (incluyendo bloques de código y formato) desde el panel de Admin sin escribir HTML crudo cada vez.
**La Solución:** Integré **CKEditor 5** directamente en el modelo `Project`. Esto requirió sobrescribir los estilos estándar del Admin para asegurar la legibilidad en modos claro/oscuro.

#### 2. Filtrado Inteligente de Proyectos
**El Desafío:** Los usuarios debían poder encontrar proyectos relevantes rápidamente sin navegar por múltiples páginas.
**La Solución:** Implementé un sistema de filtrado en el backend (`views.py`) que procesa parámetros de consulta (`?category=AI`). El sistema utiliza el ORM de Django para devolver eficientemente solo los proyectos categorizados y ordenados por una métrica personalizada de "relevancia".

#### 3. Soporte Bilingüe Ligero
**El Desafío:** Ofrecer una experiencia en inglés y español sin la sobrecarga de librerías de traducción complejas para contenido estático.
**La Solución:** Diseñé un sistema de alternancia ("toggle") en JavaScript dentro del frontend (`about.html`). Esto permite un cambio de idioma instantáneo en la sección "Sobre mí" sin necesidad de recargar la página o gestionar sesiones complejas.

---
