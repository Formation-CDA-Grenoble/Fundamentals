# Fundamentals
 
## Utilisation de Github

### Créer un dépôt Git

Pour commencer à versionner mon code, je peux créer un dépôt Git dans mon dossier de travail grâce à la commande `git init`

Ou bien, dans Github Desktop, **File > New repository**

### Enregister mon travail

Je peux demander à Git de garder une trace de toutes les modifications que j'ai effectuées dans mon dépôt Git grâce aux commandes:
```
git add .
git commit -m "message"
```
Où `message` doit être remplacé par un message décrivant les modifications que je souhaite enregistrer.

Ou bien, dans Github Desktop, je rentre mon message dans le volet de droite, à la place de "Commit message", et je clique sur le bouton **Commit**.

### Envoyer mon travail sur Github

Je peux envoyer une copie de mon travail enregistré sur Github pour que d'autres personnes puissent le voir et y participer avec la commande `git push`.

Ou bien, dans Github Desktop, je clique sur le bouton **Push origin** dans la barre en haut à droite.

### Récupérer un dépôt sur une autre machine

Si je collabore avec d'autres personnes, ou si je souhaite travailler sur mon dépôt à partir d'un nouvel ordinateur, je peux le cloner avec la commande `git clone url`, où URL doit être remplacé par le lien HTTPS que j'obtiens sur la page Github du dépot, en appuyant sur la bouton vert **Clone or download**.

Ou bien, après avoir cliqué sur ce même bouton, je clique sur **Open in Desktop** pour le cloner directement avec Github Desktop.
