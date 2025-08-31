# Panafai: AI Readiness Index

## Project Purpose
This project develops an **AI Readiness Index** to evaluate how countries — with a focus on Africa — are positioned to adopt and integrate artificial intelligence. By combining socioeconomic, infrastructure, and governance indicators, the index reveals leaders, late risers, and stagnant/volatile trajectories.

## Indicators
- Electricity Access  
- GDP (PPP)  
- Government Effectiveness  
- Internet Access  
- Literacy Rate  
- Mobile Subscriptions  
- Researchers per capita  
- R&D as % of GDP  
- Tertiary Enrollment  

## Methodology
1. **Data Collection** – World Bank, UNESCO, and UN datasets.  
2. **Data Cleaning** – Standardize formats, remove duplicates, handle missing values.  
3. **Normalization** – MinMax scaling (0–100) for cross-country comparability.  
4. **Composite Index** – Equal-weight and weighted scoring.  
5. **Clustering** – KMeans and trajectory-shape clustering to identify patterns.  
6. **Visualization** – Time series, heatmaps, PCA/t-SNE, and cluster profiles.  

## Modeling
- **KMeans clustering** – grouped countries by readiness features.  
- **Trajectory-shape clustering** – revealed temporal development patterns.  
- **PCA/t-SNE** – reduced dimensionality and improved visualization.  

## Setup
For environment setup and dependencies, see [Setup Guide](docs/setup.md).

## Project Workflow
1. [01_DataLoad_Clean](notebooks/01_DataLoad_Clean_COMPLETE.ipynb) – Load and clean datasets  
2. [02_Snapshot_EDA](notebooks/02_Snapshot_EDA.ipynb) – Exploratory Data Analysis  
3. [03_Normalize_Scale](notebooks/03_Normalize_Scale.ipynb) – Normalization and scaling  
4. [04_Scoring_Composite](notebooks/04_Scoring_Composite.ipynb) – Composite scoring  
5. [05_Visualization_Analysis](notebooks/05_Visualization_Analysis.ipynb) – Visualizations and insights  
6. [06_Clustering_Trajectories](notebooks/06_Clustering_Trajectories.ipynb) – Clustering countries  
7. [07_Trajectory_Shape_Clustering](notebooks/07_Trajectory_Shape_Clustering.ipynb) – Trajectory pattern analysis  

## Deliverables
- Jupyter notebooks (01–07) showing the full workflow  
- Composite scoring outputs (equal-weight and weighted).  
- Visualizations of country readiness trajectories  
- Cluster analysis identifying leaders, late risers, and stagnant groups  
- Extended results documented in: [Project Summary](docs/summary.md)

## File Structure
├── data/              # Raw, cleaned, and normalized datasets
├── notebooks/         # Jupyter notebooks (01–07 workflow)
├── scripts/           # Python helper files (e.g., normalize.py)
├── figures/           # Saved charts and plots
├── docs/              # Extended results and project summary
│   └── summary.md
└── README.md          # Project overview

## References & Resources
- World Bank Data Catalog – https://data.worldbank.org  
- UNESCO Institute for Statistics – http://uis.unesco.org  
- UN Data – https://data.un.org  
- scikit-learn documentation – https://scikit-learn.org/stable/  
- General Assembly Capstone Guidelines  
