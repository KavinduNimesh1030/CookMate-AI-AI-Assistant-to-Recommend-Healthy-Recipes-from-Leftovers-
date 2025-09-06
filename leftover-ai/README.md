# Leftover AI — Healthy Recipe Recommender (Food.com dataset)

A lightweight web app that suggests **healthy recipes** from your **leftover ingredients** using **NLP (Sentence‑BERT)** and the **Food.com Recipes & Interactions** dataset from Kaggle.

> Project matches your proposal: ingredient input → NLP preprocessing & matching → recipe dataset → top recipes → UI → user feedback.

---

## 1) Quick Start

### A. Prerequisites
- Python 3.9+ (3.10/3.11 fine)
- (Windows) Install Build Tools if needed for scientific libs

### B. Download the dataset (Kaggle)
Download this dataset and place files in `data/`:
- **`RAW_recipes.csv`** from Kaggle dataset: *Food.com Recipes and User Interactions* (`shuyangli94/food-com-recipes-and-user-interactions`)

> Only `RAW_recipes.csv` is required for v1. You may optionally add `RAW_interactions.csv` later.

### C. Create & activate a virtual environment
```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### D. Install dependencies
```bash
pip install -r requirements.txt
```

### E. Build the embedding index (first run only)
```bash
python build_index.py
```
This will create:
- `data/recipes_clean.csv` (normalized subset)
- `data/embeddings.npz` (Sentence‑BERT vectors + ids)

### F. Run the web app
```bash
python app.py
```
Open http://127.0.0.1:5000

---

## 2) How it works

1. **Data prep** (`build_index.py`)
   - Loads `RAW_recipes.csv`
   - Normalizes ingredients & steps
   - Parses nutrition (calories etc.)
   - Creates a compact text representation per recipe
   - Encodes with **Sentence‑BERT (`all-MiniLM-L6-v2`)**
   - Saves vectors and ids to `data/embeddings.npz`

2. **Search** (`app.py`)
   - User enters ingredients: `"onion, rice, spinach"`
   - Encodes query with the same model
   - Computes cosine similarity with recipe vectors
   - Returns **Top 5** matches with title, calories, time, and steps

3. **Feedback**
   - On each result card, users can submit **Helpful / Not Helpful**
   - Stored in `data/feedback.csv` with timestamp & query

---

## 3) Optional switches

- Limit to “healthier” recipes by calories (client toggle)
- Minimum ingredient overlap (server setting `MIN_OVERLAP` in `app.py`)

---

## 4) Files & Folders

```
leftover-ai/
├─ app.py                         # Flask app
├─ build_index.py                 # Preprocess + build embeddings
├─ requirements.txt
├─ README.md
├─ app/
│  ├─ templates/
│  │  ├─ base.html
│  │  ├─ index.html
│  │  └─ recipe.html
│  └─ static/
│     └─ style.css
├─ data/
│  ├─ RAW_recipes.csv            # (Put from Kaggle)
│  ├─ recipes_clean.csv          # (auto)
│  ├─ embeddings.npz             # (auto)
│  └─ feedback.csv               # (auto)
└─ models/                        # (reserved)
```

---

## 5) Notes

- First run will download the Sentence‑BERT model automatically.
- If memory is limited, reduce the number of recipes in `build_index.py` (e.g., `MAX_RECIPES`).
- This v1 focuses on retrieval (not generation) per your proposal.

---

## 6) License
For coursework/demo. Respect Kaggle dataset license.
