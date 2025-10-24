# Polimorfismo-y-herencia
Prueba sencilla de herencia de superclase

📋 Descripción
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
El repositorio contiene 1 carpeta que cuenta con 7 archivos, 5 de estos son para las herencias mientras que los otros dos "visuales" y "main" son meramente para poner a prueba el polimofismo, en main solo se corren los visuales y los visuales son todas las acciones que se pueden hacer, ademas de la poca interfaz grafica que existe por medio de consola, Animal es el archivo con la superclase responsable de definir unas acciones generales a todas las subclases y el resto de archivos son los animales por separados

🖋️ Contenido
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Existen 7 archivos, 2 de funcionamiento y 5 de datos 

<img width="431" height="368" alt="image" src="https://github.com/user-attachments/assets/8ce25ea4-572f-4c95-9985-fac27c6714dd" />
<img width="1528" height="783" alt="image" src="https://github.com/user-attachments/assets/5151827b-d389-4f35-81c0-8c5589ecf0a8" />


🛠️ Tecnologías Utilizadas
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Visual studio code
Python 3.15

🔧 Configuración y Instalación
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
No es posible usar el archivo original, pero si se le aplica un archivo propio de firebase entonces el programa correra perfectamente en su computador, para hacerlo funcionar porfavor descarge el archivo y dirigase a data alli encontrara dos cosas importantes, cred y databaseURL, con estos dos porfavor remplaze el directorio que aparece en cred con el que usted tenga su clave privada y databaseURL con el link de su projecto, como no es posible otorgar el acceso sin riesgo a los archivos que fueron usados por mi estas dos cosas deben ser cambiadas por informacion propia del usuario, una vez hecho esto tambien asegurese de instalar con pip, firebase-admin y firebase, despues de todos estos pasos le deberia de ser posible observar los valores cambiando y registrandose en su pagina de servidor de firebase cuando el programa se ejecute

🔧 Uso de la aplicacion
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Descarge todas las carpetas y cambie la informacion mencionada en la seccion de configuracion, una vez hecho esto corra el codigo del main y compruebe con firebase, vera que cuando se corra el main primero se creara un estudiante en forma de objeto 

<img width="340" height="65" alt="image" src="https://github.com/user-attachments/assets/f74f2737-83b5-4e8c-9046-9d3b81cfd820" />

Este estudiante preguntara por un nombre y una edad

<img width="356" height="81" alt="image" src="https://github.com/user-attachments/assets/0f68d2aa-2bed-40a8-8758-5e384ea2873e" />

Y una vez ingresados generara un carnet el cual contendra una secuencia aleatoria de 10 numeros. Ahora aqui viene lo especial de firebase
Lo primero que se hara con el programa es el crear un dato bajo el directorio estudiantes donde la informacion del alumno se guardara

<img width="459" height="284" alt="image" src="https://github.com/user-attachments/assets/59d8dcbc-077b-4d4e-bdc5-abc0c7e04c95" />

Aqui se hara uso de la primera funcion que nos otorga firebase la cual es la de creación, pero al mismo tiempo se uso la de cambio, lo que ocurre esque en la secuencia que da el main el programa crea al estudiante pero tambien le cambia su carnet esto es observable por medio de la consola y codigo

<img width="498" height="145" alt="image" src="https://github.com/user-attachments/assets/0518b4a5-3ca0-45d6-9e4c-6df53bf96897" />
<img width="313" height="85" alt="image" src="https://github.com/user-attachments/assets/af0b8c46-3085-4bfe-86ba-314f616e70f7" />

Como se puede ver, aqui hay dos valores de carnets, uno que fue con el que se empezo y creo el alumno y el segundo que es el carnet nuevo despues de haberlo cambiado, cuando uno se devuelve a la imagen de firebase se puede observar como se esta leyendo el segundo valor del carnet y esto es porque como dije antes se cambio el valor del carnet abandonado el viejo valor.

Siguiendo con el codigo lo siguiente es la funcionalidad de leer la cual unicamente muestra los valores en secuencia de diccionario que contiene el estudiante

<img width="658" height="56" alt="image" src="https://github.com/user-attachments/assets/2102a922-f894-4308-aefa-836d66605c92" />

Lo especial en esta lectura es que es hecha desde la base de datos de firebase, no desde python.

Finalmente con la ultima funcion, se elimina el estudiante seleccionado y se imprime un mensaje que confirma la accion
<img width="646" height="62" alt="image" src="https://github.com/user-attachments/assets/eb4b90b1-77f4-443f-adcf-c05c57f72489" />
<img width="465" height="258" alt="image" src="https://github.com/user-attachments/assets/78a0b164-40bc-460a-b896-239cbd776f6b" />


📄 Licencia
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
Este proyecto es de código abierto y está disponible para el uso publico

Autor: Diego Armando Pérez Solano
Fecha de creación: 16 de octubre de 2025
Nombre del proyecto: Prueba de firebase
