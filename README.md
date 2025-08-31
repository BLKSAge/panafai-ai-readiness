Panafai: Mapping the Next Billion

## Panafai is a research initiative focused on assessing AI readiness across all 54 African countries.
The project measures socio-economic, infrastructural, and technological indicators to identify opportunities for localized, decentralized AI assistants tailored to underserved regions.

## Project Purpose

The global AI conversation often overlooks underserved regions, where infrastructure, language access, and affordability shape adoption.
This project seeks to close that gap by:

Building a composite AI Readiness Index for African nations.

Identifying regional strengths and weaknesses in AI adoption potential.

Highlighting sector-specific opportunities (healthcare, education, agriculture, finance).

Providing a data-driven roadmap for localized, privacy-first AI deployment.

## Indicators

The index incorporates the following factors:

Human Development Index (HDI)

GDP per capita

Internet penetration

Education access and literacy rates

Healthcare and infrastructure proxies

## Methodology

Data Collection & Integration: Assemble datasets covering all 54 countries.

Exploratory Data Analysis (EDA): Assess completeness, normalize metrics, and examine distributions.

Feature Engineering: Standardize and weight indicators into a harmonized schema.

Composite Index Construction: Create and test weighting strategies (equal weight, PCA, expert-informed).

## Modeling:

Clustering -> segment readiness tiers (low, medium, high).

Regression -> identify drivers of readiness and predict trajectories.

Visualization: Develop maps and dashboards illustrating readiness scores, disparities, and sector opportunities.

## Deliverables

Master Dataset: Cleaned and integrated country-level indicators.

Composite AI Readiness Index: Ranking of African nations by readiness tier.

Analysis Report: Findings, interpretations, and recommendations.

Visualization Suite: Geographic readiness map and dashboards.

Executive Presentation: Summary of insights for stakeholders and decision-makers.

---
## Setup & Dependencies
---

This project requires the following Python libraries:

# Core data analysis
import pandas as pd
import numpy as np

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import geopandas as gpd

# Modeling & statistics
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

# Utilities
import os
import warnings
warnings.filterwarnings("ignore")

# Plot settings
plt.style.use("seaborn-v0_8")
sns.set_theme(context="notebook", style="whitegrid", palette="deep")

Optional

missingno – visualize missing values

folium – build interactive leaflet-style maps

To install all dependencies:

pip install -r requirements.txt
## 📁 Structure
