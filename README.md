Projet : Developpement d'une application de gestion de cinema avec python Fastpi et le deployer sur Aws en se basant sur la culture devops, arile et scrum

Durée du projet 3mois

## I- ANALYSE DU BESOIN

Pour réaliser l'analyse du besoin de l'application de gestion de cinéma, voici une démarche qui aborde les différentes étapes mentionnées précédemment :

1. Identification des parties prenantes :
    - Clients (utilisateurs finaux de l'application ou du site web)
    - Employés du cinéma (gestionnaires, caissiers, projectionnistes, etc.)
    - Direction du cinéma
    - Fournisseurs de services (paiement en ligne, billetterie, etc.)
2. Collecte des besoins :
    - Organiser des entretiens avec les employés du cinéma pour comprendre leurs besoins en matière de gestion des films, des salles, des séances et des réservations.
    - Réaliser des enquêtes auprès des clients pour connaître leurs attentes concernant la recherche, la réservation et l'achat de billets en ligne.
    - Analyser les pratiques des concurrents et les tendances du marché pour identifier les fonctionnalités et les améliorations possibles.
    - Consulter la direction pour connaître les objectifs stratégiques, les contraintes budgétaires et les exigences en matière de reporting et d'analyse.
3. Priorisation des besoins :
    - Classer les besoins recueillis en fonction de leur importance pour les utilisateurs, leur impact sur l'expérience client et leur contribution aux objectifs du cinéma.
    - Déterminer les fonctionnalités essentielles à inclure dans la première version de l'application et celles qui pourront être ajoutées ultérieurement.
4. Documentation des besoins :
    
    **A**- Rédiger les spécifications fonctionnelles (gestion des films, salles, séances, réservations, clients, reporting, interface utilisateur, etc.)
    
     Le système doit permettre la gestion des films, des salles, des séances, des réservations, des clients, du reporting et de l'interface utilisateur.
    
    1. Gestion des films
    
    1.1. Ajout de films
    
    - Importation de données telles que titre, réalisateur, acteurs, durée, genre, classification, synopsis et affiche.
    - Prise en charge de plusieurs langues et formats de sous-titres.
    
    1.2. Modification de films
    
    - Possibilité de mettre à jour les informations du film.
    
    1.3. Suppression de films
    
    - Suppression sécurisée des films avec confirmation.
    1. Gestion des salles
    
    2.1. Ajout de salles
    
    - Configuration de la capacité, du type de sièges et de l'équipement audiovisuel.
    
    2.2. Modification de salles
    
    - Mise à jour des informations de la salle.
    
    2.3. Suppression de salles
    
    - Suppression sécurisée des salles avec confirmation.
    1. Gestion des séances
    
    3.1. Planification de séances
    
    - Assignation des films aux salles.
    - Configuration des horaires et des dates.
    
    3.2. Modification de séances
    
    - Possibilité de changer les horaires, les films et les salles.
    
    3.3. Suppression de séances
    
    - Suppression sécurisée des séances avec confirmation.
    1. Gestion des réservations
    
    4.1. Réservation en ligne
    
    - Interface utilisateur permettant aux clients de sélectionner des sièges et de payer en ligne.
    
    4.2. Annulation de réservations
    
    - Possibilité pour les clients d'annuler leurs réservations dans les conditions définies.
    
    4.3. Gestion des remboursements
    
    - Traitement des remboursements pour les annulations éligibles.
    1. Gestion des clients
    
    5.1. Inscription et authentification
    
    - Création de comptes clients avec vérification d'email.
    - Connexion sécurisée avec mot de passe et authentification à deux facteurs.
    
    5.2. Gestion des informations personnelles
    
    - Modification des informations telles que nom, email, numéro de téléphone et mot de passe.
    - Suppression sécurisée du compte avec confirmation.
    1. Reporting
    
    6.1. Rapports de ventes
    
    - Récapitulatif des ventes par film, salle, séance et période.
    
    6.2. Rapports d'occupation
    
    - Taux d'occupation des salles par séance et période.
    
    6.3. Rapports clients
    
    - Analyse des préférences et du comportement des clients.
    1. Interface utilisateur
    
    7.1. Interface client
    
    - Présentation des films, des séances et des salles disponibles.
    - Possibilité de rechercher des films et de filtrer par genre, durée, etc.
    - Système de notation et de commentaires des films par les clients.
    
    7.2. Interface administrateur
    
    - Gestion des films, des salles, des séances, des réservations et des clients.
    - Accès aux rapports et aux statistiques.
    
    **B-** Rédiger les spécifications non fonctionnelles (performance, sécurité, accessibilité, compatibilité, mises à jour, etc.)
    
    Ces spécifications concernent les exigences en matière de performance, de sécurité, de fiabilité et d'autres aspects non liés directement aux fonctionnalités du système.
    
    1. Performance
    
    1.1. Temps de réponse
    
    - Le système doit répondre aux requêtes des utilisateurs dans un délai de 2 secondes maximum.
    
    1.2. Capacité
    
    - Le système doit être capable de gérer simultanément jusqu'à 10 000 utilisateurs en ligne.
    1. Sécurité
    
    2.1. Confidentialité des données
    
    - Le système doit respecter les réglementations en vigueur concernant la protection des données personnelles (ex. RGPD).
    
    2.2. Cryptage des données
    
    - Les communications entre le client et le serveur doivent être chiffrées à l'aide de protocoles sécurisés (ex. HTTPS).
    
    2.3. Sauvegarde des données
    
    - Les données doivent être sauvegardées régulièrement et stockées dans un emplacement sécurisé.
    1. Fiabilité
    
    3.1. Disponibilité
    
    - Le système doit avoir une disponibilité minimale de 99,9% (hors maintenance programmée).
    
    3.2. Tolérance aux pannes
    
    - Le système doit être capable de détecter et de récupérer rapidement des erreurs pour minimiser les interruptions de service.
    1. Évolutivité
    
    4.1. Scalabilité horizontale
    
    - Le système doit être capable d'ajouter des ressources (serveurs, bases de données) pour faire face à une augmentation de la demande.
    
    4.2. Mises à jour
    
    - Le système doit permettre des mises à jour régulières sans interruption majeure du service.
    1. Compatibilité
    
    5.1. Navigateurs web
    
    - Le système doit être compatible avec les principaux navigateurs web (ex. Google Chrome, Firefox, Safari).
    
    5.2. Appareils
    
    - Le système doit être adaptatif et fonctionner sur différents types d'appareils, tels que les ordinateurs, les smartphones et les tablettes.
    1. Accessibilité
    
    6.1. Conformité aux normes
    
    - Le système doit être conforme aux normes d'accessibilité du web (ex. WCAG 2.1).
    
    6.2. Multilinguisme
    
    - Le système doit être capable de prendre en charge plusieurs langues pour les utilisateurs.
    1. Maintenance
    
    7.1. Maintenance préventive
    
    - Le système doit inclure des mécanismes de surveillance pour détecter et prévenir les problèmes potentiels.
    
    7.2. Maintenance corrective
    
    - Le système doit permettre une intervention rapide en cas de défaillance ou de problème.
    
5. Validation des besoins :
    - Présenter les spécifications aux parties prenantes (employés, direction, fournisseurs) pour recueillir leurs commentaires et s'assurer que les besoins sont bien compris et acceptés.
    - Apporter les ajustements nécessaires en fonction des retours d'expérience et obtenir l'approbation finale.
6. Révision et mise à jour :
    - Suivre l'évolution des besoins tout au long du projet et ajuster les spécifications en conséquence.
    - Prendre en compte les retours d'expérience des utilisateurs après le lancement de l'application pour améliorer les fonctionnalités et corriger les problèmes éventuels.

## II- **Specifications**

Voici les spécifications de base pour une application de gestion de cinéma. Ces spécifications peuvent être adaptées en fonction des besoins spécifiques de votre établissement.

1. Gestion des films :
    - Ajout, modification et suppression de films
    - Gestion des informations de film (titre, durée, synopsis, genre, réalisateur, acteurs, classification, bande-annonce, affiche)
    - Programmation des séances
2. Gestion des salles :
    - Ajout, modification et suppression de salles
    - Gestion des caractéristiques de la salle (nombre de sièges, type de sièges, capacité, équipements)
    - Attribution des salles aux séances
3. Gestion des séances :
    - Planification des séances (date, heure, film, salle)
    - Gestion des tarifs (plein tarif, tarif réduit, tarif étudiant, etc.)
    - Suivi des réservations et des ventes de billets
    - Affichage des séances disponibles et des places restantes
4. Gestion des réservations :
    - Réservation en ligne ou en personne
    - Choix des sièges
    - Paiement sécurisé
    - Envoi de confirmation de réservation par e-mail ou SMS
    - Annulation ou modification de réservation
5. Gestion des clients :
    - Création et modification de comptes clients
    - Historique des réservations et des achats
    - Gestion des abonnements et des cartes de fidélité
    - Notifications et promotions personnalisées
6. Reporting et analyse :
    - Statistiques de vente par film, séance, salle, jour ou période
    - Analyse des performances (taux de remplissage, revenus, etc.)
    - Export des données pour analyse externe
7. Interface utilisateur :
    - Interface simple et intuitive pour les employés du cinéma
    - Site web et/ou application mobile pour les clients
    - Intégration des réseaux sociaux et partage de contenu
    - Accessibilité pour les personnes en situation de handicap
8. Sécurité et confidentialité :
    - Authentification et autorisations d'accès pour les employés
    - Protection des données personnelles des clients
    - Conformité aux réglementations locales sur la protection des données
9. Intégration et compatibilité :
    - Intégration avec les systèmes existants (comptabilité, CRM, etc.)
    - Compatibilité avec différents types de dispositifs (PC, tablettes, smartphones)
    - Mises à jour régulières et support technique

En fonction de vos besoins, vous pouvez ajouter d'autres fonctionnalités spécifiques à votre cinéma, telles que la gestion des événements spéciaux, la location de salles, la vente de nourriture et de boissons, ou la gestion du personnel.

## III- Nos différents modèles de données

        **A - MODELE EA (entité association)**

je peux vous proposer une structure de base pour les différentes parties de l'application de gestion de cinéma. Vous pouvez utiliser cette structure pour créer des schémas ou des diagrammes en utilisant un outil de dessin ou de modélisation de votre choix.

1. Gestion des films :
    - Entité "Film" : ID, titre, durée, synopsis, genre, réalisateur, acteurs, classification, URL bande-annonce, URL affiche
    - Relations : Film - Séance
2. Gestion des salles :
    - Entité "Salle" : ID, nom, nombre de sièges, type de sièges, capacité, équipements
    - Relations : Salle - Séance
3. Gestion des séances 
    - Entité "Séance" : ID, date, heure, tarifs, ID film, ID salle
    - Relations : Séance - Film, Séance - Salle, Séance - Réservation
4. Gestion des réservations :
    - Entité "Réservation" : ID, ID client, ID séance, sièges réservés, montant, statut (réservé, payé, annulé)
    - Relations : Réservation - Client, Réservation - Séance
5. Gestion des clients :
    - Entité "Client" : ID, nom, prénom, email, téléphone, date de naissance, adresse, abonnement, carte de fidélité
    - Relations : Client - Réservation
6. Reporting et analyse :
    - Entités et relations dépendront des rapports et analyses spécifiques souhaités, en utilisant les données des entités existantes
7. Interface utilisateur :
    - Vue "Employés" : Accès aux fonctionnalités de gestion des films, salles, séances et réservations
    - Vue "Clients" : Accès aux fonctionnalités de recherche, réservation et gestion de compte
8. Sécurité et confidentialité :
    - Entité "Utilisateur" : ID, rôle (employé, client), identifiant, mot de passe, permissions
    - Relations : Utilisateur - Client, Utilisateur - Employé
9. Intégration et compatibilité :
    - Intégration avec les systèmes existants et les interfaces utilisateur dépendra des spécificités de chaque système

Utilisez cette structure comme point de départ pour créer des schémas ou des diagrammes décrivant les relations entre les différentes entités et les fonctionnalités de l'application. Vous pouvez également ajouter d'autres entités ou relations en fonction des besoins spécifiques de votre cinéma.

Le modèle Entité-Association (EA) est un moyen de représenter les entités et leurs relations dans une base de données. Voici un modèle EA simplifié pour l'application de gestion de cinéma :

1. Entités :
    - Film (ID, titre, durée, synopsis, genre, réalisateur, acteurs, classification, URL bande-annonce, URL affiche)
    - Salle (ID, nom, nombre de sièges, type de sièges, capacité, équipements)
    - Séance (ID, date, heure, tarifs, ID_film, ID_salle)
    - Réservation (ID, ID_client, ID_séance, sièges réservés, montant, statut)
    - Client (ID, nom, prénom, email, téléphone, date de naissance, adresse, abonnement, carte de fidélité)
    - Utilisateur (ID, rôle, identifiant, mot de passe, permissions)
2. Associations :
    - Film - Séance : Un film peut être projeté lors de plusieurs séances, et une séance projette un seul film.
    - Salle - Séance : Une salle peut accueillir plusieurs séances, et une séance a lieu dans une seule salle.
    - Client - Réservation : Un client peut effectuer plusieurs réservations, et une réservation est effectuée par un seul client.
    - Séance - Réservation : Une séance peut avoir plusieurs réservations, et une réservation concerne une seule séance.
    - Utilisateur - Client : Un utilisateur peut être lié à un seul client, et un client peut être lié à un seul utilisateur (pour les clients ayant un compte en ligne).

**B - MODELE CONCEPTUEL DE DONNEES (MCD)**

Le modèle conceptuel de données (MCD) est une représentation graphique des entités, des attributs et des relations entre les entités d'un système d'information. Il sert de base pour la conception du modèle logique de données (MLD). Voici un MCD simplifié pour l'application de gestion de cinéma basé sur les entités et associations mentionnées précédemment:

1. Entités et attributs :
    - Film (ID, titre, durée, synopsis, genre, réalisateur, acteurs, classification, URL bande-annonce, URL affiche)
    - Salle (ID, nom, nombre de sièges, type de sièges, capacité, équipements)
    - Séance (ID, date, heure, tarifs, ID_film, ID_salle)
    - Réservation (ID, ID_client, ID_séance, sièges réservés, montant, statut)
    - Client (ID, nom, prénom, email, téléphone, date de naissance, adresse, abonnement, carte de fidélité)
    - Utilisateur (ID, rôle, identifiant, mot de passe, permissions)
2. Associations :
    - Film --< Séance : Un film peut être projeté lors de plusieurs séances, et une séance projette un seul film.
    - Salle --< Séance : Une salle peut accueillir plusieurs séances, et une séance a lieu dans une seule salle.
    - Client --< Réservation : Un client peut effectuer plusieurs réservations, et une réservation est effectuée par un seul client.
    - Séance --< Réservation : Une séance peut avoir plusieurs réservations, et une réservation concerne une seule séance.
    - Utilisateur -- Client (0..1) : Un utilisateur peut être lié à un seul client, et un client peut être lié à un seul utilisateur (pour les clients ayant un compte en ligne).

Dans un MCD, les entités sont représentées par des rectangles, et les associations sont représentées par des lignes reliant les entités. Les attributs peuvent être représentés à l'intérieur des rectangles ou à proximité des entités. Les cardinalités des associations sont indiquées aux extrémités des lignes (par exemple, "1" pour une relation 1:1 ou "1..N" pour une relation 1:N).

**C- MODELE LOGIQUE DE DONNEES (MLD)**

Le modèle logique de données (MLD) est une représentation des structures de données et des relations entre elles, généralement utilisée pour concevoir une base de données. Il est dérivé du modèle Entité-Association (EA) et décrit les entités sous forme de tables et les associations sous forme de clés étrangères. Voici un MLD pour l'application de gestion de cinéma basé sur les entités et associations précédemment discutées :

1. Tables :
    - Film (ID_film [PK], titre, durée, synopsis, genre, réalisateur, acteurs, classification, URL bande-annonce, URL affiche)
    - Salle (ID_salle [PK], nom, nombre de sièges, type de sièges, capacité, équipements)
    - Séance (ID_séance [PK], date, heure, tarifs, ID_film [FK], ID_salle [FK])
    - Réservation (ID_réservation [PK], ID_client [FK], ID_séance [FK], sièges réservés, montant, statut)
    - Client (ID_client [PK], nom, prénom, email, téléphone, date de naissance, adresse, abonnement, carte de fidélité)
    - Utilisateur (ID_utilisateur [PK], rôle, identifiant, mot de passe, permissions, ID_client [FK, nullable])
    
    Note : [PK] signifie "Primary Key" (Clé primaire) et [FK] signifie "Foreign Key" (Clé étrangère)
    
2. Relations :
    - Film - Séance : Un enregistrement dans la table Film est lié à plusieurs enregistrements dans la table Séance (1:N) via la clé étrangère ID_film.
    - Salle - Séance : Un enregistrement dans la table Salle est lié à plusieurs enregistrements dans la table Séance (1:N) via la clé étrangère ID_salle.
    - Client - Réservation : Un enregistrement dans la table Client est lié à plusieurs enregistrements dans la table Réservation (1:N) via la clé étrangère ID_client.
    - Séance - Réservation : Un enregistrement dans la table Séance est lié à plusieurs enregistrements dans la table Réservation (1:N) via la clé étrangère ID_séance.
    - Utilisateur - Client : Un enregistrement dans la table Utilisateur peut être lié à un enregistrement dans la table Client (1:0..1) via la clé étrangère ID_client.
