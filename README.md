# 🍲 Healthy Recipe Finder – AI-Powered Cooking Assistant  

This project is an **AI-powered recipe recommendation system** that helps users discover healthy and practical recipes based on the ingredients they already have at home. It combines **Flask (backend with AI/ML)** and **Vue.js (frontend)** into a full-stack application.  

The system:  
- Accepts **ingredient-based queries** in natural language.  
- Retrieves **semantically relevant recipes** using embeddings & cosine similarity.  
- Provides **health-aware re-ranking** (prioritizes low-calorie options).  
- Collects **user feedback** to improve recommendations.  
- Offers a clean, modern **Vue.js frontend** for interaction.  

---

## 🛠 Project Structure  

```
repository-root/
│
├── leftover-ai/          # Flask backend (Python, ML, NLP, recipe logic)
│   ├── app.py
│   ├── requirements.txt
│   ├── data/         # Recipe dataset, embeddings, feedback.csv
│   └── ...
│
├── vue-frontend/         # Vue.js frontend
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## ⚙️ Backend Setup (Flask + ML)  

### 1. Navigate to backend  
```bash
cd backend
```

### 2. Create & activate virtual environment  
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install dependencies  
```bash
pip install -r requirements.txt
```

### 4. Download Dataset  
This project uses the **Food.com Recipes and User Interactions dataset**:  
👉 [Food.com Recipes Dataset (Kaggle)](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?resource=download&select=RAW_recipes.csv)  

Place the `RAW_recipes.csv` file into the **`leftover-ai/data/`** directory.  

### 5. Build Index (embeddings)  
```bash
python build_index.py
```

### 6. Run the backend  
```bash
python app.py
```

- Backend will start at: **http://127.0.0.1:5000**  
- API endpoints exposed under `/api/...`  

---

## 🎨 Frontend Setup (Vue.js)  

### 1. Navigate to frontend  
```bash
cd frontend
```

### 2. Install dependencies  
```bash
npm install
```

### 3. Run the development server  
```bash
npm run dev
```

- Frontend will start at: **http://localhost:5173**  

---

## 🔗 API Endpoints  

- **POST** `/api/search` → Search recipes by ingredients.  
- **GET** `/api/recipe/<id>` → Get details of a specific recipe.  
- **POST** `/api/feedback` → Submit user feedback.  
- **GET** `/api/top-feedback` → Get top recipes by positive feedback.  

---

## 📊 Features  

✔ Ingredient-based search with semantic matching  
✔ Health-aware ranking (low-calorie prioritization)  
✔ User-friendly Vue.js UI  
✔ Feedback loop for iterative improvement  
✔ Dataset-driven, extensible design  

---

## 🚀 Technology Stack  

- **Frontend:** Vue.js, Axios, TailwindCSS  
- **Backend:** Flask, Pandas, NumPy, Scikit-learn, Sentence-Transformers  
- **Database:** CSV-based (recipes, feedback)  
- **ML:** Embedding-based similarity with cosine similarity  

---

## 📌 Future Improvements  

- Add filters for dietary restrictions (vegan, low-carb, etc.).  
- Personalization based on user history.  
- Integration with smart kitchen apps or grocery APIs.  

---

## 🙌 Acknowledgements  

- Dataset: [Food.com Recipes & User Interactions](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions?resource=download&select=RAW_recipes.csv)  
- Libraries: [Flask](https://flask.palletsprojects.com/), [Vue.js](https://vuejs.org/), [Sentence Transformers](https://www.sbert.net/)  
