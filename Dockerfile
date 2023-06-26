FROM dfs154/python3.8.10:base-images

RUN mkdir /app
#repertoire de travail app
WORKDIR /app 

 #Copie du conteu du répertoire courant vers le dossier/app par exemple ceci peut etre changer au besoin
 COPY . /app/
# pour définir la version de limage
LABEL version = V1.0.0  

EXPOSE 8001
RUN  apt-get update
RUN  apt-get install pip 
RUN pip install poetry 
RUN poetry install 
#ici le processus est déclaré de manière à écouter sur toutes les interfaces
    #CMD ["flask","run","--host = 0.0.0.0"] 

    #permet de definir les volumes qui vont etre utiliser dans notre image

VOLUME ["/var/www","/var/log/apache2","/etc/apache2"] 
  #pour executer lapplication
CMD poetry run python app/main.py
