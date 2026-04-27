# NewNRJ — MVP Habits & Energy App

## 📘 Mini Cahier des Charges — MVP NewNRJ

### .🎯 Mission

Créer une application mobile simple et efficace permettant à un utilisateur de :

* Définir quelques habitudes essentielles,
* Les suivre quotidiennement,
* Visualiser sa progression,
* Recevoir un feedback positif immédiat.

L’objectif : **valider l’intérêt, l’usage et la rétention** avant d’investir dans des fonctionnalités avancées.

### 🧪 Hypothèses à valider

* Les utilisateurs veulent suivre **peu d’habitudes**, mais régulièrement.
* Le feedback positif immédiat augmente la rétention.
* La simplicité est un avantage (pas de surcharge).
* Le multi‑langue augmente la portée internationale.
* Le nom **NewNRJ** est suffisamment fort pour un lancement MVP.

### 🧱 Contraintes MVP

* Interface minimaliste, rapide à développer.
* Stockage local **Postgres** (ou SQLite si besoin).
* Multi‑langue dès le MVP : EN / ES / FR / DE.
* Pas de gamification, pas de statistiques avancées.
* Architecture propre et scalable (FletX).
* Branding léger : juste le nom **NewNRJ** et une palette simple.
* Publication prévue sur le **Google Play Store**.

### 🎨 Identité visuelle MVP (simple et rapide)

#### Police recommandée

**Montserrat**, **Poppins**, **Inter**

#### Couleurs

* Vert énergie : `#00C853`
* Bleu calme : `#2962FF`
* Fond sombre par défaut (gris très foncé), texte blanc pour la lisibilité

#### Style

* Minimaliste
* Icônes simples
* Pas d’illustrations complexes
* Logo simple (MVP) = Simple texte NewNRJ avec la police choisie

## 🏗️ Architecture MVP (Flet / FletX)

### Structure recommandée (FletX)

```mmarkdown
/controllers      → logique
/views            → écrans
/models           → Habit, User (plus tard)
/services         → stockage local, notifications
/i18n             → fichiers de langue (EN/ES/FR/DE)
```

---

## 🛡️ BP — Battle Plan MVP NewNRJ (jusqu’à la publication Google Play)

### .🎯 Objectif du MVP

Permettre à un utilisateur de :

* [ ] Créer **1 à 3 habitudes simples**
* [ ] Les **suivre quotidiennement**
* [ ] Voir sa **progression**
* [ ] Recevoir un **encouragement / feedback positif**

**Rien de plus: MVP !**  
Pas de gamification, pas de badges, pas de statistiques avancées.  
Juste l’essentiel pour valider l’idée.

---

### Préparation

* [/] App : New version ? Oui : App → Install !
* [ ] Git: Push Main → Auto New Version → Push on Ggle Drive - https://rclone.org
* [ ] Faire un son au début et à la fin des 2 sessions

 🧩 Les 6 écrans minimum du MVP
### 🧩 Les 6 écrans minimum du MVP

#### 1) Écran d’accueil / onboarding

* [ ] Logo simple : **NewNRJ** (texte uniquement pour le MVP)
* [ ] Phrase courte : “Build new habits. Boost your energy.”
* [ ] Bouton : **Start**

---

#### 2) Écran de création d’habitude

* [ ] Champ : Nom de l’habitude
* [ ] Champ : Fréquence (quotidienne / hebdomadaire simple)
* [ ] Champ : Heure de rappel (optionnel)
* [ ] Bouton : **Add Habit**

---

#### 3) Liste des habitudes

* [ ] Afficher la liste des habitudes
* [ ] Bouton **Done** pour chaque habitude
* [ ] Barre de progression (optionnelle)

---

#### 4) Écran “Check‑in”

* [ ] Animation simple : **✓**
* [ ] Message positif : “Great! New energy unlocked.”

---

#### 5) Historique minimal

* [ ] Liste des jours avec **✓** ou **✗**
* [ ] Pas besoin de graphiques pour le MVP

---

#### 6) Paramètres

* [ ] Sélecteur de langue : **EN / ES / FR / DE**
* [ ] Mode clair/sombre (optionnel)

---

### 🧠 Fonctionnalités MVP — Côté technique

#### Obligatoires

* [ ] Création / suppression d’habitudes
* [ ] Stockage local (SQLite pour le MVP - Sera PostGres en Prod réelle)
* [ ] Check‑in quotidien
* [ ] Multi‑langue (4 langues)
* [ ] UI simple et propre

#### Optionnelles (si temps disponible)

* [ ] Notifications locales
* [ ] Synchronisation cloud (plus tard)
* [ ] Compte utilisateur (plus tard)

---

### Extensions futures (après MVP)

* [ ] API FastAPI
* [ ] Auth
* [ ] Sync cloud
* [ ] Gamification
* [ ] Dashboard avancé

---

## 🔥 Prochaines étapes possibles (Build Roadmap)

* [ ] Générer l’arborescence complète du projet (FletX)
* [ ] Créer le modèle **Habit** (Python)
* [ ] Créer le contrôleur MVP
* [ ] Implémenter les **6 écrans** minimalistes
* [ ] Mettre en place le système **i18n** (EN/ES/FR/DE)
* [ ] Préparer un **plan de développement sur 3 jours**
* [ ] Générer le premier APK
* [ ] Préparer le Store Listing
* [ ] Publier sur Google Play

---

## 🚀 Pipeline de Build (Android)

### Préparation

* [ ] Installer Android Studio
* [ ] Installer SDK + outils de build
* [ ] Configurer l’environnement Flet/FletX pour Android
* [ ] Générer un premier APK local

### Tests internes

* [ ] Tester l’APK sur ton propre téléphone
* [ ] Tester sur 1–2 appareils Android différents
* [ ] Vérifier les langues
* [ ] Vérifier les permissions
* [ ] Vérifier la persistance des données

---

## 🏁 Publication Google Play Store

### 1) Création du compte développeur

* [ ] Créer un compte Google Play Developer
* [ ] Payer les frais uniques
* [ ] Configurer les informations légales

### 2) Préparation du Store Listing

* [ ] Nom de l’app : **NewNRJ**
* [ ] Sous‑titre : “Build new habits. Boost your energy.”
* [ ] Description courte
* [ ] Description longue
* [ ] Icône 512×512
* [ ] Splash screen simple
* [ ] Screenshots (6 écrans)
* [ ] Vidéo (optionnelle)

### 3) Préparation de l’APK / AAB

* [ ] Générer un **AAB** (format obligatoire)
* [ ] Signer l’application
* [ ] Vérifier la signature
* [ ] Vérifier la taille du bundle

### 4) Déploiement

* [ ] Upload du AAB dans Google Play Console
* [ ] Remplir la fiche de conformité (permissions, contenu)
* [ ] Remplir la classification du contenu
* [ ] Définir les pays de distribution
* [ ] Déployer en Closed Testing Track
      (Google Playdemande d'inviter 5–10 testeurs)

### 5) Publication

* [ ] Corriger les retours des testeurs
* [ ] Soumettre en **Production**
* [ ] Attendre validation Google
* [ ] App publiée 🎉
