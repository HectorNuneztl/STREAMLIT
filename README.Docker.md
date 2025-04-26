

## PASOS PARA LA CREACIÓN DE UN DOCKER: 

1. ##### _Imagen:_
* Si no se tiene un repositorio de github para el proyecto entonces clonarlo mediante **git clone _link a SSH del repositorio_**. Caso contrario, continuar con los pasos siguientes. 

* Crear un docker file para el proyecto usando _docker init_ e ir seleccionando las opciones que se adecuen a la aplicación (utilizar puerto 8501 cuando lo pida). 

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


## PASOS PARA DESPLEGAR UNA ST APP EN EC2

# Utilizando solo streamlit: 

1. Crear una instancia:
Menú -> todos los serrvicios -> informática -> EC2 ->Lanzar instancia

Se configura en base a la app. Para usar los comandos de a continuación se debe seleccionar la imágen de Ubuntu. 

2. Configuración de puerto:
En el resumen de la instancia ir a 

seguridad -> grupos de seguridad -> editar reglas de entrada -> agregar regla

y en la parte de TCP personalizado agregar el puerto al que escucha la app. El resto de casillas se configura igual que las otras reglas. 

3. Conexión:
Conectar la instancia con el botón "Conectar" y copiar los siguientes comandos:

sudo apt update

sudo apt-get update

sudo apt upgrade -y

sudo apt install git curl unzip tar make sudo vim wget -y

sudo apt install git curl unzip tar make sudo vim wget -y

git clone "Link HTTPS del repositorio"

sudo apt install python3-pip

pip3 install -r requirements.txt

si el comando anterior falla, entonces colocar los siguientes comandos:

sudo apt update 

sudo apt install python3.12-venv

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

Ahora es posible inicializar el servidor de dos maneras: 

* Forma temporal: 
python3 -m streamlit run "nombre de la aplicación.py"

* Forma permanente
nohop python3 -m streamlit run "nombre de la aplicación.py"

Al correr cualquier comando para poder visualizar la app se copia la dirección IP pública de la instancia, se encuentra en el apartado "Dirección IPv4 pública". Al copiarlo y pegarlo en el navegador hacer las siguientes modficaciones antes de dar "Enter":

"Dirección IP:puerto al que escucha"

# Utilizando solo streamlit y docker : 

1. Crear una instancia:
Seguir los pasos 1 y 2 del despliegue con solo streamlit

2. Conexión: 
Para realizar la conexión y crear un docker seguir los siguientes pasos y comandos: 

sudo apt-get update -y

sudo apt-get upgrade

* Se debe instalar docker, por tanto usar los comandos: 

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

git clone "Likn HTTPS del repositorio"

docker build -t "Nombre de ususairo en docker hub"/"Nombre de la imagen":latest . 

* Listar las imagenes que hayan sido creadas mediante: 

docker images -a  

* Inicializar el docker para confirmar que la aplicación este funcionando:

docker run -d -p 8501:8501 "Nombre de usuario en docker hub"/"Nombre de la imagen" 

docker ps  

docker stop container_id

el id del contenedor se ve a trvés del comando _docker ps_

* Como se detuvo el contenedor es importanto liberar el espeacio que esta ocupando, para ello usar: 

docker rm $(docker ps -a -q)

* Ahora, para poder tener las imagenes en nuestro repositorio se tiene que iniciar sesión en docker hub, para hacer esto seguir los siguientes comandos: 

docker login 

docker push "Nombre de usuario en docker hub"/"Nombre de la imagen":latest 

* Verificar en docker hub si realmente se hizo el push de la imagen. 

* En caso de que se tenga una imagen en docker hub que quiera ser tomada mediante pull, entonces seguir los siguientes comandos: 

* Pimero se borra la imagen si esque esta ya estaba creada de forma local, de lo contrario omitir este comando

docker rmi "Nombre de usuario en docker hub"/"Nombre de la imagen":latest

* Se realiza el pull del docker mediante: 

docker pull "Nombre de usuario en docker hub"/"Nombre de la imagen"

* Ahora mediante los comandos ya vistos se verifica que la imagen haya sido extraída mediante el pull y se ejecuta la aplicación para verificar que esta funcione correcamente