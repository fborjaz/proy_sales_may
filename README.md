# 🛒 Super Mercado Económico 🏬

## ✨ Descripción

¡Bienvenido al proyecto Super Mercado Económico! 🛒 Este proyecto Django te permite gestionar productos, marcas, proveedores y categorías de manera eficiente. Con un diseño minimalista y oscuro, la aplicación es fácil de usar y visualmente atractiva.

## 🚀 Características Principales

* **Productos:** 📦 Administra tu inventario de productos con facilidad. Agrega, edita y elimina productos, incluyendo imágenes, descripciones, precios, stock y más.
* **Marcas:** 🏷️ Organiza tus productos por marcas reconocidas para una mejor visualización y gestión.
* **Proveedores:** 🤝 Mantén un registro completo de tus proveedores, incluyendo nombres, RUC y direcciones.
* **Categorías:** 🗂️ Clasifica tus productos en diferentes categorías para una mejor organización y búsqueda.
* **Autenticación:** 🔐 Sistema de registro e inicio de sesión seguro para proteger el acceso a las funciones de administración.

## 🛠️ Tecnologías Utilizadas

* **Django:** 💪 El potente framework web de Python que impulsa esta aplicación.
* **SQLite:** 💾 Base de datos ligera y fácil de usar para almacenar los datos de tu supermercado.
* **HTML, CSS, JavaScript:** 🎨 Lenguajes de frontend para crear la interfaz de usuario moderna y minimalista.
* **Font Awesome:** ✨ Biblioteca de iconos para añadir elementos visuales atractivos.

## ⚙️ Cómo Ejecutar la Aplicación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/fborjaz/proy_sales_may.git 
   cd proy_sales_may
    ```
   
2. **Crear (o activar) un entorno virtual::**
    ```bash
    python -m venv venv  
    source venv/bin/activate  # En macOS/Linux
    venv\Scripts\activate    # En Windows
    . venv/bin/activate     # Activa el entorno virtual
    ```
   
3. **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
   
4. **Aplicar las migraciones:**
    ```bash
    python manage.py migrate
    ```
   
5. **Crear un superusuario:**
    ```bash
    python manage.py createsuperuser
    ```
   
6. **Ejecutar el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
   
7. **Acceder a la aplicación en tu navegador:**
    ```
    Abre tu navegador web y ve a http://127.0.0.1:8000/.
    ```
   
8. **Iniciar sesión en el panel de administración:**
    ```
    Accede a http://127.0.0.1:8000/admin/ y utiliza las credenciales del superusuario que creaste en el paso 5.
    ```
   
## Explora y disfruta de Super Mercado Económico!** 🎉

*🤝 Contribuciones*
¡Las contribuciones son bienvenidas! Si encuentras algún error o quieres agregar nuevas funcionalidades, no dudes en abrir un issue o enviar un pull request. 🙌

#
**Copyright**
© 2024 [Frank Borja](https://frankborja.github.io/Curriculum-Vitae/). Todos los derechos reservados.


