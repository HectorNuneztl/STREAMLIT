## CREACIÓN DE UN DOCKER: 

1. ##### _Imagen:_
* Si no se tiene un repositorio de github para el proyecto entonces clonarlo mediante **git clone _link a SSH del repositorio_**. Caso contrario, continuar con los pasos siguientes. 

* Crear un docker file para el proyecto usando _docker init_ e ir seleccionando las opciones que se adecuen a la aplicación (utilizar puerto 8051 cuando lo pida). 

* Se generarán varios archivos, sin embargo, el archivo de requerimientos no, este debe crearse a parte. A pesar de que el docker file se cree solo lo más probable es que este no funcione al momento de crear la imagen y su contenedor, por ello seguir el paso siguiente para la creación de un docker file. 


2. ###### _Docker file_:
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit", "run"]

CMD ["app3.py"]

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health



##### _Documentación_: 
* _Establecer una imagen base, en este caso se usa una versión que permita usar las funcoones básicas de python_

* _Establecer el diectorio para que posteriores cambios se hagan por medio de esta ruta_

* _Copiar el txt de requerimientos dentro del contenedor_

* _Se instalan las dependencias de python establecidas en el archivo de requerimientos_

* _Establecer el puerto, en este caso se utiliza el puerto predeterminado de streamlit_

* _Copiar los archivos del proyecto local al contenedor_

* _Establecer el comando para ejecutar la aplicación_

* _Establecer la aplicación a ejecutar en el contenedor_ 

* _Chequeo de salud, para verificar si Streamlit se está ejecutando corretamente_


3. ##### Imagen: 
Para crear una imagen se utiliza el comando _build -t nombreImagen ._ 

4. ##### Activación de imagen y docker:
Abrir la aplicación Docker e ir al apartado de imagenes, buscar la imagen creada y activarla mediante el botón run. Rellenar los apartados _Nombre del contenedor_ y _puerto_.

Tomar en cuenta que si se actualiza la aplicación posterior a la creación del contenedor, es necesario generar una nueva imagen en la cual se vean reflejados los cambios realizados. 

