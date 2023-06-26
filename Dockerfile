FROM python3:nom_code # de python3 vers nom_code ou on va retrouver l'image à compiler 

LABEL version = V1.0.0 # pour définir la version de l'image

ENV FLASK_ENV = dev # variable d'environnement de développement ici c'est dev la variable


RUN SK_ENV = poésie ./run.sh -r poésie run python app/main.py

EXPOSER 8001

CMD ["flask","run","--host = 0.0.0.0"] #ici le processus est déclaré de manière à écouter sur toutes les interfaces

WORKDIR /app #repertoire de travail app

COPY . /app/ # Copie du conteu du répertoire courant vers le dossier/app par exemple ceci peut etre changer au besoin


VOLUME ["/var/www","/var/log/apache2","/etc/apache2"] #permet de definir les volumes qui vont etre utiliser dans notre image

