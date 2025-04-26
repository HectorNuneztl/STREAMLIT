## CREACIÓN DE UN DOCKER: 

1. ##### _Imagen:_
* Si no se tiene un repositorio de github para el proyecto entonces clonarlo mediante **git clone _link a SSH del repositorio_**. Caso contrario, continuar con los pasos siguientes. 

* Crear un docker file para el proyecto usando _docker init_


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




