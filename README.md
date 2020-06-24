# LaForge
     .            .____                           
     /       ___  /       __.  .___    ___.   ___ 
     |      /   ` |__.  .'   \ /   \ .'   ` .'   `      .__    ._
     |     |    | |     |    | |   ' |    | |----'   o   |  \ _ |,. . __
     /---/ `.__/| /      `._.' /      `---| `.___,       |__/(_)| (_|_)
                                      \___/

Assistant de forgemagie pour le MMORPG Dofus v2.5 à destination de la guilde **Les Sylvidres**
> **\[En cours de développement]**
## Utilisation
Pour une utilisation en ligne de commande, il suffit de télécharger le projet, puis d'exécuter le fichier `cli.py`.
*LaForge* peut aussi s'utiliser comme un bot discord, ici en l'occurrence hébergé sur [Heroku](https://www.heroku.com/), dans ce cas, c'est le fichier `main.py` qu'il faudra lancer.

> Pour le moment, seul le calcul de reliquat (ou "pui") est implémenté.


## Pour les utilisateurs

Si vous souhaitez intégrer ce bot à votre serveur discord, il faut en faire le déploiement manuellement.
Il existe de nombreuses manières de déployer un bot discord. L'une de ces solutions est de passer par le service *Heroku* (cf ci-dessus) qui ne demande ni serveur, ni carte bancaire.

### Les bonnes adresses pour apprendre à déployer un bot :

+ Avec Heroku : [vidéo d'aide (EN)](https://www.youtube.com/watch?v=BPvg9bndP1U)
+ Sur son serveur local : (*voir section plus bas*)

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

## Déploiement du bot depuis un serveur personnel (raspberry pi, VPS...)

### Prérequis

1. Pour commencer, il faut installer la librairie discord à l'aide de l'utilitaire `pip`. Sous linux, il s'agit de la commande :
```shell
    ~$ python3 -m pip install -U discord.py
```

2. On crée ensuite un serveur discord. En supposant que vous ayez déjà un compte, cette opération se fait très
   facilement en appuyant sur le '+' en dessous de la liste des serveurs se situant à gauche de l'interface

### Mise au monde du Bot

On crée le bot depuis le site officiel de Discord, à l'adresse https://discordapp.com/developers/applications/
La procédure est guidée, mais si jamais vous rencontrez un problème, n'hésitez pas à regarder du côté de la documentation
ci-contre : https://discordapp.com/developers/docs/intro

### Codage du Bot

1. On commence avec la précision de l'encodage ainsi que l'import des librairies
2. On crée ensuite une variable `token` qui recevra le dit token qui représente une longue série de chiffres à garder
   privée
3. On choisi un préfixe qui précèdera les commandes qui invoqueront notre bot, ainsi qu'une petite description
   de ce dernier
4. Pour s'assurer que le bot est actif, on crée une fonction permettant d'afficher dans le terminal \*Bot is ready\*
5. On rajoute la commande de démarrage (dernière ligne du fichier)
5. Enfin, on crée les commandes auxquelles le bot devra répondre

Les commandes auront dans la majorité des cas la même en-tête, à savoir :

    @arena_bot.command()
    async def <commande>(ctx, <param1>, <param2>, ...):

Pour le reste, chaque fonction du programme est commentée dans le but de s'en inspirer, n'hésitez pas à les lire.

### Mise en place du bot

#### Initialisation des variables d'environnement
Sous linux, il existe différents *"degrés"* de variables d'environnement dont la configuration change selon les shells utilisés.
De manière très simple, il est possible d'initialiser ces variables en les ajoutant au fichier `/etc/environment` de cette manière :
```shell
# echo "arena_token="AAZEsqdqshjkrzFrDuib1345978qds31435a4ze!$Azesd"" >> /etc/environment
```
#### Last step !
Une fois le bot crée et codé, rendez-vous à l'adresse https://discordapp.com/developers/applications/
Cliquez dans la section *Bot* du pannel de gauche, et créez votre bot (vous serez averti que cette action est
irreversible).

On peut donc voir que notre bot a pris vie, et qu'il s'est vu attribuer un *token*. Comme dit précédemment, il doit rester
privé !

La suite se passe dans le panel OAuth :
- on coche Bot
- on sélectionne les permissions (en l'occurrence ici send-message et role-management, ou admin si l'on ne peut pas faire autrement)
- une adresse est alors générée
- il suffit de la coller dans un nouvel onglet
- notre bot apparait alors, déconnecté

Pour le connecter, il suffit d'exécuter dans une console notre script python, et voir s'afficher le message
*Bot is ready*

