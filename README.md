# Legion Binaria – Programación II

Este repositorio pertenece al grupo **"Legion Binaria"**, formado para la cursada de **Programación II** en la Tecnicatura Universitaria en Programación (TUP).  
Actualmente trabajamos con los lenguajes **Java**, **JavaScript** y **Python**, desarrollando distintos proyectos y ejercicios prácticos del segundo semestre.

---

## 📚 Información de la materia

- **Carrera:** Tecnicatura Universitaria en Programación (TUP)  
- **Materia:** Programación II  
- **Semestre:** Segundo  
- **Lenguajes vistos:**  
  - Java  
  - JavaScript  
  - Python  
- **Docente:** [Ariel Betancud](https://github.com/ArielBetancud22)

---

## 👥 Integrantes del grupo "Legion Binaria"

- [Chavez, Joel.](https://github.com/joelcm20)
- [Farina, Cristian.](https://github.com/Criss0001)
- [Farina, Lucia.](https://github.com/LuciaFarina)
- [Guzowski, Sebastian.](https://github.com/sguzowski)
- [Lazo, Johana.](https://github.com/JohaLazo30)
- [Rodríguez, Jackeline S.](https://github.com/jackelinesoledadrodriguez)
- [Saurit, Francisco.](https://github.com/fr4ncisx)

---

## 🚀 Objetivo del repositorio

- Reunir todos los ejercicios, proyectos y prácticas desarrolladas durante la materia.  
- Facilitar el trabajo colaborativo usando GitHub como herramienta principal (en reemplazo de Trello/Jira).  
- Mantener un control de versiones ordenado y documentado usando el flujo **Git Flow básico**:
  - `main` → rama estable y lista para entrega  
  - `develop` → rama de integración donde se une el trabajo del equipo  
  - ramas individuales o de feature → creadas desde `develop`  

---

## 🛠️ Requisitos previos

Antes de clonar este repositorio asegúrate de tener instalado:

- [Git](https://git-scm.com/)  
- [Java JDK](https://www.oracle.com/java/technologies/downloads/) *(para proyectos en Java)*  
- [Node.js](https://nodejs.org/) *(para proyectos en JavaScript)*  
- [Python](https://www.python.org/downloads/) *(para proyectos en Python)*  

Opcional:  
- [Visual Studio Code](https://code.visualstudio.com/) o cualquier IDE que prefieras (IntelliJ, PyCharm, Eclipse, etc.)  
- Extensiones de soporte para cada lenguaje  

---

## 📥 Pasos para clonar el repositorio

1. **Abrir una terminal o consola.**  
2. Ejecutar:
    ```bash
    git clone https://github.com/HotCode2025/legion-binaria-2do-semestre.git
    ```
3. **Entrar al directorio del proyecto:**
    ```bash
    cd legion-binaria-2do-semestre
    ```
4. **Cambiar a la rama develop (base de trabajo):**
    ```bash
    git checkout develop
    ```
5. **Crear tu propia rama desde develop:**
    ```bash
    git checkout -b feature/nombre-descriptivo
    # o para trabajos individuales
    git checkout -b nombre-integrante
    ```
6. **Mantener la rama actualizada antes de subir cambios:**
    ```bash
    git pull origin develop
    ```

## 📂 Estructura del repositorio

legion-binaria-2do-semestre/ <br>
│<br>
├── java/         # Proyectos y ejercicios en Java <br>
├── javascript/   # Proyectos y ejercicios en JavaScript <br>
├── python/       # Proyectos y ejercicios en Python <br>
└── README.md     # Documentación del repositorio <br>

## 📌 Reglas de trabajo colaborativo

- **Commits claros y descriptivos**:

    Usar mensajes que expliquen qué se modificó.

    **Ejemplo**:
    ```bash
    git commit -m "Agregado ejercicio 3 de Java sobre herencia"
    ```

- **Usar ramas de feature o personales:**

    Cada integrante debe crear una rama propia desde develop y luego hacer pull request a develop.

- **Nunca trabajar directo en main:**

    La rama main queda protegida como versión estable.

- **Revisar y aprobar cambios:**
    
    Antes de fusionar una rama, otro integrante del grupo debería revisarla para asegurar calidad y evitar errores.