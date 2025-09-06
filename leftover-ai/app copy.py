import os, ast, csv, time
import numpy as np
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

DATA_DIR = "data"
CLEAN_FILE = os.path.join(DATA_DIR, "recipes_clean.csv")
EMB_FILE = os.path.join(DATA_DIR, "embeddings.npz")
FEEDBACK_FILE = os.path.join(DATA_DIR, "feedback.csv")

# Tuning
TOP_K = 5
MIN_OVERLAP = 0  # set >0 to require that at least N query tokens overlap ingredients

app = Flask(__name__)

# Lazy globals
_model = None
_embeddings = None
_ids = None
_df = None

def load_index():
    global _model, _embeddings, _ids, _df
    if _df is None:
        assert os.path.exists(CLEAN_FILE), "Missing recipes_clean.csv. Run: python build_index.py"
        _df = pd.read_csv(CLEAN_FILE)
        # parse lists
        _df['ingredients_list'] = _df['ingredients_list'].apply(lambda s: ast.literal_eval(s) if isinstance(s,str) else [])
        _df['steps_list'] = _df['steps_list'].apply(lambda s: ast.literal_eval(s) if isinstance(s,str) else [])
    if _embeddings is None or _ids is None:
        assert os.path.exists(EMB_FILE), "Missing embeddings.npz. Run: python build_index.py"
        npz = np.load(EMB_FILE)
        _embeddings = npz['embeddings']
        _ids = npz['ids']
    if _model is None:
        _model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return _model, _embeddings, _ids, _df

def prefer_healthier(df, idxs):
    # sort by calories ascending where available
    sub = df.loc[idxs, ['calories']].copy()
    # missing calories -> large placeholder
    sub['cal'] = sub['calories'].fillna(1e9)
    order = sub['cal'].argsort(kind="mergesort")
    return idxs[order]

def token_overlap(query, ingredients):
    q = [t.strip().lower() for t in query.split(",") if t.strip()]
    ing = [t.strip().lower() for t in ingredients]
    return len(set(q) & set(ing))

app = Flask(
    __name__,
    template_folder=os.path.join("app", "templates"),
    static_folder=os.path.join("app", "static")
)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", results=None, query="", healthy=False)

@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query","").strip()
    healthy = request.form.get("healthy") == "on"
    if not query:
        return redirect(url_for("index"))
    model, embeddings, ids, df = load_index()

    # encode query
    qvec = model.encode([query], normalize_embeddings=True)
    sims = cosine_similarity(qvec, embeddings)[0]

    # pick top N
    top_idx = sims.argsort()[-200:][::-1]  # first take 200 for post-filtering
    # optional overlap filter
    if MIN_OVERLAP > 0:
        filtered = []
        for i in top_idx:
            row = df.iloc[i]
            if token_overlap(query, row['ingredients_list']) >= MIN_OVERLAP:
                filtered.append(i)
        top_idx = np.array(filtered, dtype=int)

    if healthy:
        top_idx = prefer_healthier(df, top_idx)

    top_idx = top_idx[:TOP_K]
    rows = df.iloc[top_idx].copy()
    rows['score'] = sims[top_idx]

    results = []
    for _, row in rows.iterrows():
        results.append({
            "id": int(row['id']),
            "name": row['name'],
            "minutes": int(row['minutes']) if not pd.isna(row['minutes']) else None,
            "n_ingredients": int(row['n_ingredients']) if not pd.isna(row['n_ingredients']) else None,
            "calories": float(row['calories']) if not pd.isna(row['calories']) else None,
            "score": float(row['score']),
        })

    return render_template("index.html", results=results, query=query, healthy=healthy)

@app.route("/recipe/<int:recipe_id>")
def recipe_detail(recipe_id):
    _, _, _, df = load_index()
    row = df[df['id']==recipe_id].iloc[0]
    recipe = {
        "id": int(row['id']),
        "name": row['name'],
        "minutes": int(row['minutes']) if not pd.isna(row['minutes']) else None,
        "n_ingredients": int(row['n_ingredients']) if not pd.isna(row['n_ingredients']) else None,
        "calories": float(row['calories']) if not pd.isna(row['calories']) else None,
        "ingredients_list": row['ingredients_list'],
        "steps_list": row['steps_list'],
    }
    return render_template("recipe.html", recipe=recipe)

@app.route("/feedback", methods=["POST"])
def feedback():
    recipe_id = int(request.form.get("recipe_id"))
    query = request.form.get("query","")
    helpful = int(request.form.get("helpful", "0"))
    ts = int(time.time())
    header = not os.path.exists(FEEDBACK_FILE)
    with open(FEEDBACK_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(["timestamp","recipe_id","query","helpful"])
        writer.writerow([ts, recipe_id, query, helpful])
    return redirect(url_for("index"))

if __name__ == "__main__":
    # enable for local development
    app.run(debug=True)
