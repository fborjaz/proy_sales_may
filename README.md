# 🛒 Super Mercado Económico 🏬

✨ **Descripción**

¡Bienvenido al proyecto **Super Mercado Económico**! 🛒

Este proyecto Django te permite gestionar de manera eficiente todos los aspectos de tu supermercado, desde los productos hasta los proveedores. Con un diseño minimalista y elegante, la aplicación es intuitiva y fácil de usar.

🚀 **Características Principales**

* **Productos:** 📦 Agrega, edita y elimina productos con facilidad. Incluye detalles como imágenes, descripciones, precios y stock.
* **Marcas:** 🏷️ Organiza tus productos por marcas reconocidas para una mejor gestión y visualización.
* **Proveedores:** 🤝 Mantén un registro completo de tus proveedores, con información de contacto y detalles relevantes.
* **Categorías:** 🗂️ Clasifica tus productos en categorías para facilitar la búsqueda y la organización.
* **Autenticación:** 🔐 Protege el acceso a las funciones de administración con un sistema seguro de registro e inicio de sesión.

🎨 **Diseño Minimalista y Oscuro**

La interfaz de usuario está diseñada con un estilo minimalista y una paleta de colores oscura, que brinda una experiencia visual moderna y elegante.

🛠️ **Tecnologías Utilizadas**

* **Backend:**
    * **Django:** El sólido framework web de Python que impulsa la aplicación.
    * **SQLite:** Base de datos ligera y eficiente para almacenar los datos.
* **Frontend:**
    * **HTML, CSS, JavaScript:** Lenguajes esenciales para crear la interfaz de usuario.
    * **Bootstrap:** Framework CSS para un diseño responsivo y estilizado.
    * **Font Awesome:** Biblioteca de iconos para añadir elementos visuales atractivos.

📂 **Estructura del Proyecto**
   ```bash
    proy_sales_may
    ├── core
    │   ├── migrations
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── media
    │   ├── products
    │   └── cocacola.jpg
    ├── proy_sales_may
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── utils.py
    │   └── wsgi.py
    ├── static
    │   ├── css
    │   ├── base.css
    │   │   ├── components
    │   │   │  ├── buttons.css
    │   │   │  ├── form.css
    │   │   │  ├── footer.css
    │   │   │  ├── modal.css
    │   │   │  ├── table.css
    │   │   ├── layout
    │   │   │  ├── navigation.css
    │   │   │  ├── header.css
    │   │   ├── pages
    │   ├── images
    │   │   ├── favicon-001.png    
    │   ├── media
    │   │   ├── products
    │   │   │  ├── cocacola.jpg
    ├── staticfiles
    ├── templates
    │   ├── base.html
    │   ├── signin.html
    │   ├── signup.html
    │   ├── profile.html
    │   ├── partials
    │   │  ├── footer.html
    │   │  ├── header.html
    │   │  ├── navigation.html
    │   ├── core
    │   │  ├── brand
    │   │  │  ├── brand_list.html
    │   │  │  ├── brand_form.html
    │   │  │  ├── brand_delete.html
    │   │  ├── categorys
    │   │  │  ├── category_list.html
    │   │  │  ├── category_form.html
    │   │  │  ├── category_delete.html
    │   │  ├── products
    │   │  │  ├── list.html
    │   │  │  ├── form.html
    │   │  │  ├── delete.html
    │   │  ├── suppliers
    │   │  │  ├── supplier_list.html
    │   │  │  ├── supplier_form.html
    │   │  │  ├── supplier_delete.html
    │   │  ├── home.html
    ├── .gitignore
    ├── factur.sqlite3
    ├── manage.py
    ├── orm.py
    ├── README.md
    ├── requirements.txt
   ```

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


