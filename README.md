# LaForge
     .            .____                           
     /       ___  /       __.  .___    ___.   ___ 
     |      /   ` |__.  .'   \ /   \ .'   ` .'   `      .__    ._
     |     |    | |     |    | |   ' |    | |----'   o   |  \ _ |,. . __
     /---/ `.__/| /      `._.' /      `---| `.___,       |__/(_)| (_|_)
                                      \___/

Assistant de forgemagie pour le MMORPG Dofus v2.5 à destination de la guile **Les Sylvidres**
> **\[En cours de développement]**
## Utilisation
Pour une utilisation en ligne de commande, il suffit de télécharger le projet, puis d'exécuter le fichier `cli.py`.
*LaForge* peut aussi s'utiliser comme un bot discord, ici en l'occurrence hébergé sur [Heroku](https://www.heroku.com/), dans ce cas, c'est le fichier `main.py` qu'il faudra lancer.

Pour le moment, seul le calcul de reliquat (ou "pui") est implémenté.


## Pour les utilisateurs

Si vous souhaitez intégrer ce bot à votre serveur discord, il faut en faire le déploiement manuellement.
Il existe de nombreuses manières de déployer un bot discord. L'une de ces solutions est de passer par le service *Heroku* (cf ci-dessus) qui ne demande ni serveur, ni carte bancaire.

### Les bonnes adresses pour apprendre à déployer un bot :

+ Avec Heroku : [vidéo d'aide](https://www.youtube.com/watch?v=BPvg9bndP1U)
+ Sur son serveur local : [tuto](TUTO.md)

## Résumé des commandes offertes par le bot

```
LaForge - Assistant de forgemagie pour le MMORPG Dofus v2.5

​No Category:
  help  Shows this message
  ping  Ping le bot, permet de savoir s'il est actif ou non
  pui   Retourne le reliquat généré par la forge
  start Démarre une session de forgemagie
  stop  Stoppe une session de forgemagie

Type $help command for more info on a command.
You can also type $help category for more info on a category.
```

## Pour les développeurs

Cette section s'adresse aux développeurs souhaitant contribuer au développement du bot.

### Instructions

Des instructions sur le procédé de création d'un bot discord sont disponibles [ici](TUTO.md). N'hésitez pas à les lires, surtout  si c'est la première fois que vous codez un bot discord.

### Installation des outils

#### Python3

Contribuer au développement de ce bot nécessite l'installation de python3 (*testé en 3.6*). On peut installer python3 depuis [ce lien](https://www.python.org/downloads/)

#### Dépendances

Pour que le bot soit fonctionnel, nous utilisons un package appellé [discord.py](https://discordpy.readthedocs.io/en/latest/). Il permet de faire la connexion entre le bot et les services de discord.

Pour installer cette dépendance et commencer à contribuer au développement, vous pouvez saisir les commandes suivantes :

**[1] Clonage des sources**
```shell
$ git clone git@github.com:codeanonorg/Arena-Bot.git
```

**[2] Installation des dépendances**
```shell
$ pip3 install -r requirements.txt
```

**⚠︎** : *cette commande nécessite d'avoir une installation complète de python3*
