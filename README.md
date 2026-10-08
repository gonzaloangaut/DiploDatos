# DiploDatos — Data Science and Machine Learning

Coursework and projects from the **2025 Diplomatura en Ciencia de Datos, Aprendizaje Automático y sus Aplicaciones** at FaMAF, Universidad Nacional de Córdoba.

This repository preserves the course exercises, individual work, and collaborative submissions. Most notebooks are in Spanish.

## Where to start

- **[Satellite Data Science](https://github.com/gonzaloangaut/satellite-data-science):** the completed portfolio adaptation of the collaborative satellite project, with revised data curation, model evaluation, and documentation.
- **[Original satellite project](Mentorias/):** the diploma submissions, from exploratory analysis to supervised and unsupervised learning.
- **[Computer Vision](VC/):** image classification, convolutional networks, transfer learning, object detection, and segmentation coursework.
- **[Deep Learning](IAP/):** NLP and language-model assignments, including sentiment analysis and prompting experiments.

## Repository guide

| Folder | Course or project |
| --- | --- |
| [`AyVD/`](AyVD/) | Análisis y Visualización de Datos — Data Analysis and Visualization |
| [`AEyCD/`](AEyCD/) | Análisis Exploratorio y Curación de Datos — Exploratory Data Analysis and Curation |
| [`IAA/`](IAA/) | Introducción al Aprendizaje Automático — Introduction to Machine Learning |
| [`AS/`](AS/) | Aprendizaje Supervisado — Supervised Learning |
| [`ANS/`](ANS/) | Aprendizaje No Supervisado — Unsupervised Learning |
| [`IAP/`](IAP/) | Introducción al Aprendizaje Profundo — Introduction to Deep Learning |
| [`VC/`](VC/) | Visión por Computadora — Computer Vision |
| [`RL/`](RL/) | Reinforcement Learning |
| [`Mentorias/`](Mentorias/) | Collaborative satellite project |

Where present, `Ejercicios/` contains course practice material and `Entregables/` contains submitted assignments. Other courses keep their notebooks directly in the course folder. Environment files are provided for several courses.

## Satellite project

The collaborative mentorship project, *Predictions in Space: How many satellites and debris can we have?*, explored catalogs of objects in orbit. It included data visualization, cleaning and feature preparation, satellite expected-lifetime prediction, and clustering.

The revised [Satellite Data Science](https://github.com/gonzaloangaut/satellite-data-science) repository is the recommended entry point for reviewing the finished portfolio version. The original diploma submissions remain in `Mentorias/`.

## Running the notebooks

Clone the repository:

```bash
git clone https://github.com/gonzaloangaut/DiploDatos.git
cd DiploDatos
```

Use the environment file for the course you want to explore. For example, for Data Analysis and Visualization:

```bash
conda env create -f AyVD/environment.yml
conda activate env-diplodatos-ayvd
jupyter notebook
```

Other courses may use different environments or Colab-specific setup cells. Check the course README and notebook before running it. The saved environments reflect the original coursework.

## Background and attribution

Program: [Diplomatura en Ciencia de Datos, Aprendizaje Automático y sus Aplicaciones](https://diplodatos.famaf.unc.edu.ar/).

The repository includes teaching materials and collaborative work; authorship and group information are retained in the notebooks. The satellite mentorship project was developed by Ana Paula Cobresí, Gonzalo Angaut, Javier Albiero, and Octavio Santi.
