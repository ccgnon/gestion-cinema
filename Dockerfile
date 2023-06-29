FROM python:3.8.17

#repertoire de travail app

WORKDIR /app 

 #Copie du conteu du répertoire courant vers le dossier/app par exemple ceci peut etre changer au besoin
 COPY . /app/
# pour définir la version de limage
LABEL version = V1.0.0  

EXPOSE 8001
RUN  apt-get update && pip install poetry && poetry install

#ici le processus est déclaré de manière à écouter sur toutes les interfaces
    #CMD ["flask","run","--host = 0.0.0.0"] 

    #permet de definir les volumes qui vont etre utiliser dans notre image

VOLUME ["/var/www","/var/log/apache2","/etc/apache2"] 
  #pour executer lapplication
CMD poetry run python app/main.py

#Demarrer le contenaire Lorsque vous exécutez la commande docker run -p 8080:8001, cela signifie que
#vous reliez le port local 8080 à votre conteneur Docker qui écoute sur le port 8001. 
#Il est donc important de sassurer que lapplication
#dans votre conteneur Docker écoute bien sur le port 8001
# docker stop 0beb33fda379
# docker start 0beb33fda379 pour redemarer le contenaire
#docker run -p 8080:8001 monimage
#lance limage Docker avec http://localhost:8080/docs
