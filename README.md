# DiploDatos

Repository with all the projects completed during the ["Diplomatura en Ciencia de Datos, Aprendizaje Automático y sus Aplicaciones"](https://diplodatos.famaf.unc.edu.ar/) (Diploma in Data Science, Machine Learning and its Applications). 

## Repository structure

The repository contains folders for each course in the diploma:

- `AyVD` – Análisis y Visualización de Datos (Data Analysis and Visualization)  
- `AEyCD` – Análisis Exploratorio y Curación de Datos (Exploratory Data Analysis and Curation)  
- `IAA` – Introducción al Aprendizaje Automático (Introduction to Machine Learning)  
- `AS` – Aprendizaje Supervisado (Supervised Learning)  
- `ANS` – Aprendizaje No Supervisado (Unsupervised Learning)
- `VC` – Visión por Computadora (Computer vision)
- `DL` – Deep Learning
- `RL` – Reinforcement Learning

Each course folder includes:  
- `Ejercicios` (*Exercises*): notebooks provided by professors with practice exercises.  
- `Entregables` (*Deliverables*): projects we developed and submitted during the course.
- `environment.yml` a conda environment file with all dependencies required to run the notebooks.

Additionally, there is a `Mentoría` folder containing the final project of the diploma.  
The aim of this project was to apply our knowledge to a real-world problem. Our project, *"Predictions in Space: How many satellites and debris can we have?"*, analyzed a dataset of objects in orbit. We first performed data visualization and initial analysis, then applied preprocessing techniques such as categorical encoding, missing-value imputation, and feature scaling. Finally, we applied supervised learning to predict the expected lifetime of the objects and unsupervised learning for clustering. 

## How to Use This Repository

1. Clone the repository:  
   ```bash
   git clone <repo_url>
   ```

2. Navigate to the desired course folder and create the conda environment:
   ```bash
   conda env create -f environment.yml
   ```

3. Activate the environment and run the notebooks.
