# NewNRJ.com — MVP Habits & Energy App

<table>
<tr>
<td width="50%">

## 📘 Mini Specifications — MVP NewNRJ

### .🎯 Mission

Create a simple and efficient mobile application allowing a user to:

* Define a few essential habits,
* Track them daily,
* Visualize their progress,
* Receive immediate positive feedback.

The objective: **validate interest, usage and retention** before investing in advanced features.

### 🧪 Hypotheses to validate

* Users want to track **few habits**, but regularly.
* Immediate positive feedback increases retention.
* Simplicity is an advantage (no overload).
* Multi-language increases international reach.
* The name **NewNRJ** is strong enough for an MVP launch.

### 🧱 MVP Constraints

* Minimalist interface, quick to develop.
* Local storage **Postgres** (or SQLite if needed).
* Multi-language from MVP: EN / ES / FR / DE.
* No gamification, no advanced statistics.
* Clean and scalable architecture (FletX).
* Light branding: just the name **NewNRJ** and a simple palette.
* Publication planned on **Google Play Store**.

### 🎨 MVP Visual Identity (simple and quick)

#### Recommended Font

**Montserrat**, **Poppins**, **Inter**

#### Colors

* Energy green: `#00C853`
* Calm blue: `#2962FF`
* Dark background by default (very dark gray), white text for readability

#### Style

* Minimalist
* Simple icons
* No complex illustrations
* Simple logo (MVP) = Simple NewNRJ text with chosen font

## 🏗️ MVP Architecture (Flet / FletX)

### Recommended Structure (FletX)

```
/controllers      → logic
/views            → screens
/models           → Habit, User (later)
/services         → local storage, notifications
/i18n             → language files (EN/ES/FR/DE)
```

---

## 🛡️ BP — Battle Plan MVP NewNRJ (until Google Play publication)

### .🎯 MVP Objective

Allow a user to:

* [ ] Create **simple habits**
* [ ] Manage one of them with the App
* [ ] **Track them daily**
* [ ] See their **progress**
* [ ] Receive **encouragement / positive feedback**

**Nothing more: MVP!**

No gamification, no badges, no advanced statistics.  
Just the essentials to validate the idea.

---

### Preparation

* [x] Set App # 0.0.2 src/ in new structure (Entry point = ./main)
* [ ] 1 Register the habit (H) Sport in Database (migration during development)
* [ ] Home page is the habit, but 1 link to manage the habits
* [ ] 2 Highlight it on all pages (header)
* [ ] 3 The countdown button is functional
* [ ] → Make the sports countdown app work again according to new procedure
* [ ] Git: Push Main → Auto New Version → Push on Ggle Drive - https://rclone.org
* [ ] App : New version ? Yes : App → Install !
* [ ] Add a sound at the beginning and end of the 2 sessions
* [ ] Make tick tock the last 10 seconds of each session

### 🧩 The 6 minimum screens of the MVP

#### 1) Home / Onboarding screen

* [ ] Simple logo: **NewNRJ** (text only for MVP)
* [ ] Short sentence: "Build new habits. Boost your energy."
* [ ] Button: **Start**

---

#### 2) Habit creation screen

* [ ] Field: Habit name
* [ ] Field: Frequency (daily / simple weekly)
* [ ] Field: Reminder time (optional)
* [ ] Button: **Add Habit**

---

#### 3) Habit list

* [ ] Display the list of habits
* [ ] **Done** button for each habit
* [ ] Progress bar (optional)

---

#### 4) "Check-in" screen

* [ ] Simple animation: **✓**
* [ ] Positive message: "Great! New energy unlocked."

---

#### 5) Minimal history

* [ ] List of days with **✓** or **✗**
* [ ] No need for graphs for MVP

---

#### 6) Settings

* [ ] Language selector: **EN / ES / FR / DE**
* [ ] Light/dark mode (optional)

---

### 🧠 MVP Features — Technical Side

#### Mandatory

* [ ] Create / delete habits
* [ ] Local storage (SQLite for MVP - Will be Postgres in real production)
* [ ] Daily check-in
* [ ] Multi-language (4 languages)
* [ ] Simple and clean UI

#### Optional (if time available)

* [ ] Local notifications
* [ ] Cloud synchronization (later)
* [ ] User account (later)

---

### Future Extensions (after MVP)

* [ ] FastAPI API
* [ ] Auth
* [ ] Cloud sync
* [ ] Gamification
* [ ] Advanced dashboard

---

## 🔥 Next possible steps (Build Roadmap)

* [ ] Generate complete project tree (FletX)
* [ ] Create the **Habit** model (Python)
* [ ] Create MVP controller
* [ ] Implement the **6 minimalist screens**
* [ ] Set up **i18n** system (EN/ES/FR/DE)
* [ ] Prepare a **3-day development plan**
* [ ] Generate first APK
* [ ] Prepare Store Listing
* [ ] Publish on Google Play

---

## 🚀 Build Pipeline (Android)

### Preparation

* [ ] Install Android Studio
* [ ] Install SDK + build tools
* [ ] Configure Flet/FletX environment for Android
* [ ] Generate first local APK

### Internal Tests

* [ ] Test APK on your own phone
* [ ] Test on 1-2 different Android devices
* [ ] Check languages
* [ ] Check permissions
* [ ] Check data persistence

---

## 🏁 Google Play Store Publication

### 1) Developer Account Creation

* [ ] Create a Google Play Developer account
* [ ] Pay one-time fees
* [ ] Configure legal information

### 2) Store Listing Preparation

* [ ] App name: **NewNRJ**
* [ ] Subtitle: "Build new habits. Boost your energy."
* [ ] Short description
* [ ] Long description
* [ ] 512×512 icon
* [ ] Simple splash screen
* [ ] Screenshots (6 screens)
* [ ] Video (optional)

### 3) APK / AAB Preparation

* [ ] Generate an **AAB** (mandatory format)
* [ ] Sign the application
* [ ] Verify signature
* [ ] Check bundle size

### 4) Deployment

* [ ] Upload AAB to Google Play Console
* [ ] Fill out compliance form (permissions, content)
* [ ] Fill out content rating
* [ ] Set distribution countries
* [ ] Deploy to Closed Testing Track
      (Google Play asks to invite 5-10 testers)

### 5) Publication

* [ ] Fix tester feedback
* [ ] Submit to **Production**
* [ ] Wait for Google validation
* [ ] App published 🎉

</td>
<td width="50%">

## 📘 Mini Cahier des Charges — MVP NewNRJ

### .🎯 Mission

Créer une application mobile simple et efficace permettant à un utilisateur de :

* Définir quelques habitudes essentielles,
* Les suivre quotidiennement,
* Visualiser sa progression,
* Recevoir un feedback positif immédiat.

L'objectif : **valider l'intérêt, l'usage et la rétention** avant d'investir dans des fonctionnalités avancées.

### 🧪 Hypothèses à valider

* Les utilisateurs veulent suivre **peu d'habitudes**, mais régulièrement.
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
* Pas d'illustrations complexes
* Logo simple (MVP) = Simple texte NewNRJ avec la police choisie

## 🏗️ Architecture MVP (Flet / FletX)

### Structure recommandée (FletX)

```
/controllers      → logique
/views            → écrans
/models           → Habit, User (plus tard)
/services         → stockage local, notifications
/i18n             → fichiers de langue (EN/ES/FR/DE)
```

---

## 🛡️ BP — Battle Plan MVP NewNRJ (jusqu'à la publication Google Play)

### .🎯 Objectif du MVP

Permettre à un utilisateur de :

* [ ] Créer des **habitudes simples**
* [ ] En faire gérer une par l'App
* [ ] Les **suivre quotidiennement**
* [ ] Voir sa **progression**
* [ ] Recevoir un **encouragement / feedback positif**

**Rien de plus: MVP !**

Pas de gamification, pas de badges, pas de statistiques avancées.  
Juste l'essentiel pour valider l'idée.

---

### Préparation

* [x] Set App # 0.0.2 src/ dans nouvelle structure (Entry point = ./main)
* [ ] 1 Enregistrer l'habit (H) Sport en BdD (migration pdt mise au point)
* [ ] La Une est l'h, mais 1 lk pour aller gérer les H
* [ ] 2 la mettre en avant dans toutes les pages (header)
* [ ] 3 Le btn countdown fonctionnel
* [ ] → Refaire marcher l'app du compteur sport, selon la nouvelle procédure
* [ ] Git: Push Main → Auto New Version → Push on Ggle Drive - https://rclone.org
* [ ] App : New version ? Oui : App → Install !
* [ ] Faire un son au début et à la fin des 2 sessions
* [ ] Faire tic tac les 10 dernières secoondes de chaque session

### 🧩 Les 6 écrans minimum du MVP

#### 1) Écran d'accueil / onboarding

* [ ] Logo simple : **NewNRJ** (texte uniquement pour le MVP)
* [ ] Phrase courte : "Build new habits. Boost your energy."
* [ ] Bouton : **Start**

---

#### 2) Écran de création d'habitude

* [ ] Champ : Nom de l'habitude
* [ ] Champ : Fréquence (quotidienne / hebdomadaire simple)
* [ ] Champ : Heure de rappel (optionnel)
* [ ] Bouton : **Add Habit**

---

#### 3) Liste des habitudes

* [ ] Afficher la liste des habitudes
* [ ] Bouton **Done** pour chaque habitude
* [ ] Barre de progression (optionnelle)

---

#### 4) Écran "Check‑in"

* [ ] Animation simple : **✓**
* [ ] Message positif : "Great! New energy unlocked."

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

* [ ] Création / suppression d'habitudes
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

* [ ] Générer l'arborescence complète du projet (FletX)
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
* [ ] Configurer l'environnement Flet/FletX pour Android
* [ ] Générer un premier APK local

### Tests internes

* [ ] Tester l'APK sur ton propre téléphone
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

* [ ] Nom de l'app : **NewNRJ**
* [ ] Sous‑titre : "Build new habits. Boost your energy."
* [ ] Description courte
* [ ] Description longue
* [ ] Icône 512×512
* [ ] Splash screen simple
* [ ] Screenshots (6 écrans)
* [ ] Vidéo (optionnelle)

### 3) Préparation de l'APK / AAB

* [ ] Générer un **AAB** (format obligatoire)
* [ ] Signer l'application
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

</td>
</tr>
</table>
