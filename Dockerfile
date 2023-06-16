FROM python3:nom_code # de python3 vers nom_code ou on va retrouver l'image à compiler 

LABEL version = V1.0.0 # pour définir la version de l'image

ENV FLASK_ENV = dev # variable d'environnement de developement ici c'est dev la variable


RUN SK_ENV =poetry ./run.sh -r poetry run python app/main.py


EXPOSE 8001

CMD ["flask","run","--host = 0.0.0.0"] #ici le processus est déclarer de manière à écouter sur tout les interfaces

WORKDIR /app   #repertoire de travail app

COPY

VOLUME ["/var/www","/var/log/apache2","/etc/apache2"] #permet de definir les volumes qui vont etre utiliser dans notre image

