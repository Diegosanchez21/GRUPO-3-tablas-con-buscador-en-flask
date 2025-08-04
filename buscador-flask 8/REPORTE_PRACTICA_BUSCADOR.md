# Reporte de Práctica: Tablas con Buscador en Flask

## Portada

**Nombre del Proyecto:** Buscador de Tablas en Flask  
**Materia:** [Nombre de la materia]  
**Integrantes del equipo:**  
- [Nombre 1]  
- [Nombre 2]  
- [Nombre 3]  
**Fecha:** [Fecha de entrega]

---

## Código (con enlace a GitHub y fragmentos ilustrativos)

Repositorio en GitHub: [https://github.com/usuario/proyecto-buscador-flask](https://github.com/usuario/proyecto-buscador-flask)  
Estructura principal del proyecto:

![image1](image1)

- **app.py**: Aplicación principal de Flask, define las rutas y controla el flujo.
- **algoritmos_busqueda.py**: Módulo con las implementaciones de búsqueda secuencial y binaria.
- **requirements.txt**: Lista de dependencias del proyecto.
- **README.md**: Información general del proyecto.
- **templates/**: Plantillas HTML con Bootstrap para la interfaz gráfica.
    - `index.html`, `busqueda_secuencial.html`, `busqueda_binaria.html`, `base.html`.

---

## Pantallas de Funcionamiento Visual con Explicación

### Página Principal

Al iniciar la aplicación se muestra una página con la opción de elegir entre los dos algoritmos de búsqueda:

![image4](image4)

- **Búsqueda Secuencial:** Recorre la lista elemento por elemento hasta encontrar el valor buscado.
- **Búsqueda Binaria:** Divide la lista ordenada por la mitad en cada iteración, buscando de manera más eficiente.

### Ejemplo: Búsqueda Binaria

![image2](image2)

En la búsqueda binaria, se ingresa el valor a buscar. El sistema muestra la lista ordenada, resalta los elementos revisados y el elemento encontrado.  
También presenta en la parte lateral derecha el resultado (“¡Elemento encontrado!”) con su posición y valor, además del paso de búsqueda explicando el rango y el valor medio.

### Ejemplo: Búsqueda Secuencial

![image3](image3)

En la búsqueda secuencial, el usuario ingresa el valor a buscar y el sistema recorre la lista desde el principio hasta encontrar el elemento.  
La tabla muestra los valores revisados y resalta el elemento encontrado junto con su posición.

---

## Conclusión

Este proyecto demuestra cómo implementar y visualizar dos métodos de búsqueda clásicos en una aplicación web usando Flask: la búsqueda secuencial y la búsqueda binaria.  
La visualización paso a paso facilita la comprensión de los algoritmos, mostrando qué elementos han sido revisados y el resultado final de la búsqueda.  
El uso de Flask y Bootstrap permite un desarrollo ágil y una interfaz intuitiva para el usuario.

---

## Referencias

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to Algorithms* (4th ed.). MIT Press.
- Flask Documentation. (n.d.). https://flask.palletsprojects.com/
- W3Schools. (n.d.). Bootstrap 5. https://www.w3schools.com/bootstrap5/
- Universidad Nacional Autónoma de México. (2021). *Guía de estilo APA 7ª edición*. https://www.unam.mx/

---

**Formato de referencias en APA 7ª edición.**
