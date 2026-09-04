# 📦 Projet de Recherche Opérationnelle - Résolution de Problèmes de Transport

> **École :** Efrei Paris  
> **Département :** Mathématiques  
> **Cursus :** Année 2025/2026 - S5  

## Objectif du Projet
Ce projet consiste à concevoir un programme complet permettant de résoudre des **problèmes de transport** (cas équilibré) afin de minimiser le coût total d'acheminement entre des fournisseurs (dotés de provisions) et des clients (exprimant des commandes).

Le projet comprend également une phase d'évaluation empirique de la **complexité algorithmique** à travers la génération de jeux de données aléatoires.

---

## Fonctionnalités Principales

Le programme implémente les fonctionnalités et algorithmes suivants :
1. **Gestion des Fichiers :** Lecture et stockage en mémoire des matrices de coûts, provisions et commandes à partir de fichiers `.txt`.
2. **Propositions Initiales :**
   - Algorithme du **Coin Nord-Ouest**.
   - Algorithme de **Balas-Hammer** (calcul des pénalités, affichage et choix des arêtes).
3. **Optimisation :** Méthode du **Marche-Pied avec potentiels** (Stepping-Stone).
4. **Analyse Graphe :**
   - Test d'acyclicité par parcours en largeur (BFS) et affichage des cycles.
   - Maximisation du transport sur un cycle détecté.
   - Test de connexité par parcours en largeur (BFS) et modification du graphe si nécessaire.
5. **Affichage Structuré :** Visualisation soignée des matrices de coûts, propositions de transport, tables de coûts potentiels et coûts marginaux.

---

## Étude de Complexité
Une étude approfondie de la complexité dans le pire des cas est réalisée pour évaluer l'impact des différents algorithmes (Nord-Ouest vs Balas-Hammer combinés au marche-pied) sur des matrices carrées de taille $n \times n$ générées aléatoirement.

---

## 📂 Structure du Dépôt

```text
├── src/                  # Code source du programme (C, C++, Python ou Java)
├── data/                 # Les 12 fichiers .txt des problèmes de transport (Annexes)
├── traces/               # Traces d'exécution pour les 12 problèmes (NO et BH)
└── rapport/              # Rapport d'étude de la complexité (max 5 pages)
