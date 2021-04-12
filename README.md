# GuideMe
## Groupe
- Grégoire Rebstein
- Ugo Crucy
- Yohann Loison

## Description
- GuideMe est une application qui regroupe les activités (loisirs, restau, sport, culture...) à faire dans une région donnée. L'idée c'est que les utilisateurs puissent ajouter des activités à faire en précisant la localisation. 
- Tous les utilisateurs peuvent choisir de rechercher des activités à faire dans une région. Ces activités peuvent ensuite être filtré (genre, evaluation). 
- Chaque actvité contient une petite description, des évaluations des utilisateurs et eventuellement un lien vers le site officiel de l'activité. Comme c'est une app communautaire, chaque utilisateur peut modifier la description d'une activité.

## Installation

**Frontend**

```bash
cd ./frontend
npm install
```

**Backend**

```bash
cd ./backend
python -m venv .venv
source .venv/Scripts/activate
pip install Django
pip install djangorestframework
pip install markdown
pip install django-filter
pip install django-cors-headers
pip install django-oauth-toolkit
```

## Utilisation

**Frontend**

```bash
cd ./frontend
npm run serve
```

**Backend**

```bash
cd ./backend
source .venv/Scripts/activate
cd ./guideme
python manage.py runserver
```

