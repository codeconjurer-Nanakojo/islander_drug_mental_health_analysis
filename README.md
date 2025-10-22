# Islander Drug Mental Health Analysis 🏝️

## 1\. Overview

This repository hosts an exploratory data analysis (EDA) project focused on assessing the mental and cognitive impacts of different drug regimens on a specific islander population.

The core goal is to understand how variables like **Drug Type**, **Dosage**, and pre-existing **Emotional State** (`Happy_Sad_group`) correlate with changes in memory performance.

## 2\. Dataset Variables

The analysis is based on a dataset with the following key variables:

| Column Name | Description | Data Type (Expected) | Sample Value |
| :--- | :--- | :--- | :--- |
| `first_name`, `last_name` | Participant identifying information. | String | *Daichi*, *Steiner* |
| `age` | Participant's age. | Integer | 37 |
| `Happy_Sad_group` | Pre-existing emotional state group. | String/Categorical | **H** (Happy) or **S** (Sad) |
| `Dosage` | Drug dosage level administered. | Integer | 1, 2, or 3 |
| `Drug` | Type of drug administered. | String/Categorical | **T**, **A**, or **S** |
| **`Mem_Score_Before`** | Memory score *before* drug administration. | Float | 64.2 |
| **`Mem_Score_After`** | Memory score *after* drug administration. | Float | 57.3 |

**Derived Key Metric:** The difference between `Mem_Score_After` and `Mem_Score_Before` will be a critical metric for measuring the drug's effect.

## 3\. Project Goals (Analysis Focus)

The analysis will address the following key questions:

1.  **Overall Effect:** What is the average change in memory score for the entire population?
2.  **Drug Comparison:** Which drug (**T**, **A**, or **S**) shows the most significant positive or negative impact on memory?
3.  **Dosage Response:** Does a higher `Dosage` correlate with a more pronounced effect (positive or negative)?
4.  **Emotional Impact:** Does the drug's effect differ significantly between the **Happy (H)** and **Sad (S)** groups?

## 4\. Repository Structure

The project is organized using a standard data science layout:

```
Islander-Drug-Mental-Health-Analysis/
├── data/
│   └── raw_data.csv        # The original, unprocessed dataset.
├── notebooks/
│   ├── 1_data_cleaning.ipynb   # Initial data inspection and preparation.
│   └── 2_eda_analysis.ipynb    # Main exploratory analysis and visualization.
├── requirements.txt            # List of required Python packages (e.g., pandas, matplotlib, seaborn).
└── README.md                   # This file.
```

## 5\. Getting Started (Setup)

To run this analysis locally, you will need a Python environment.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/Islander-Drug-Mental-Health-Analysis.git
    cd Islander-Drug-Mental-Health-Analysis
    ```
2.  **Create a virtual environment (Recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Launch Jupyter:**
    ```bash
    jupyter notebook
    ```
    Navigate to the `notebooks/` directory to begin exploring the analysis notebooks.

## 6\. Technologies Used

  * **Language:** Python
  * **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
  * **Environment:** Jupyter Notebook / Visual Studio Code

-----