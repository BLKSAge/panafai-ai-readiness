# Setup & Dependencies

This guide explains how to set up the environment required to reproduce the **AI Readiness Index** analysis.  

> **Note:** During development, we used two environments.  
> - One for general data cleaning and visualization.  
> - One for clustering/modeling with additional libraries.  
> Both are documented here for transparency.  

---

## 1. Clone the Repository

git clone https://github.com/BLKSAge/panafai-ai-readiness.git
cd panafai

## 2. Environment Setup

# Option A: Conda (recommended)

- Copy code
conda create -n capstone07 python=3.10
conda activate capstone07
pip install -r requirements.txt

# Option B: Python venv

- Copy code
python -m venv capstone07
source capstone07/bin/activate   # Mac/Linux
capstone07\Scripts\activate      # Windows
pip install -r requirements.txt

## 3. Core Dependencies

- Python 3.10+
- pandas, numpy
- scikit-learn
- matplotlib, seaborn
- jupyter

## 4. Optional Installs
- plotly → interactive visualizations
- statsmodels → advanced statistical analysis

## 5. Additional Notes
- Some visualizations used t-SNE, which requires scikit-learn >= 1.2.
- If you only want to explore the cleaned data and composite scores, the base environment is enough.
- If you want to reproduce clustering and trajectory-shape analysis, use the capstone07 environment with extra dependencies (scikit-learn, tslearn).