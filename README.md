<div align="center">

# 🎬 CineMatch — AI Movie Recommendation Engine

**Discover your next favorite movie, powered by content-based machine learning.**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-Educational-blue?style=flat-square)](#-license)
[![TMDB](https://img.shields.io/badge/Data-TMDB%205000-01B4E4?style=flat-square&logo=themoviedatabase&logoColor=white)](https://www.themoviedb.org/)
[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://ai-movie-recommendation-system1.streamlit.app/)

*Type in a movie you love. Get instant, ranked recommendations — with posters — in one click.*

### 🔗 [**Try the Live App**](https://ai-movie-recommendation-system1.streamlit.app/) &nbsp;|&nbsp; [**View Source on GitHub**](https://github.com/MuazzamAmanat/movie-recommendation-system)

</div>

---

## ✨ Why CineMatch

Most recommendation demos stop at "cosine similarity + a dataframe." CineMatch goes further:

| | |
|---|---|
| ⚡ **Instant results** | Similarity is precomputed offline, so recommendations render in milliseconds — no live model inference. |
| 🎯 **Content-aware** | Blends overview, genres, keywords, cast, and director into a single semantic fingerprint per movie. |
| 🪶 **Lightweight deploy** | Only the top 200 neighbors per movie are stored, cutting the similarity matrix from gigabytes to megabytes. |
| 🖼️ **Visual UI** | Live posters and TMDB links pulled straight from the TMDB API. |
| 🔐 **Secrets-safe** | API keys never touch the codebase — managed entirely through Streamlit Secrets. |

---

## 🖥️ Demo

<div align="center">

**🚀 Live app: [ai-movie-recommendation-system1.streamlit.app](https://ai-movie-recommendation-system1.streamlit.app/)**

<img src="screenshot.png" alt="CineMatch app showing Spider-Man recommendations" width="800"/>

*Select a movie → get instantly ranked, poster-rich recommendations.*

</div>

---

## 🧠 How It Works

CineMatch treats every movie as a "bag of meaning" — combining what it's *about*, *who's in it*, and *who made it* — then finds its nearest neighbors in that space.

```
┌─────────────────┐     ┌──────────────────┐     ┌───────────────────┐
│  TMDB Datasets   │ ──▶ │  Feature Fusion   │ ──▶ │   Text Cleaning    │
│ movies + credits │     │ overview, genres, │     │ lowercase, stem,   │
│                  │     │ keywords, cast,   │     │ remove name spaces │
│                  │     │ director          │     │                    │
└─────────────────┘     └──────────────────┘     └─────────┬──────────┘
                                                             ▼
┌──────────────────┐     ┌──────────────────┐     ┌───────────────────┐
│  Instant Lookup   │ ◀── │  Top-200 Pruning  │ ◀── │  Vectorize + Cosine│
│  in Streamlit App │     │  per movie        │     │  Similarity Matrix │
└──────────────────┘     └──────────────────┘     └───────────────────┘
```

**Pipeline breakdown:**

1. **Merge** the TMDB Movies and Credits datasets on title.
2. **Select** high-signal features: overview, genres, keywords, top 3 cast, director.
3. **Clean & normalize** — lowercase text, collapse multi-word names (`"Christopher Nolan"` → `"christophernolan"`) so names are treated as single tokens.
4. **Stem** with the Porter Stemmer to unify word variants.
5. **Combine** everything into one `tags` column per movie.
6. **Vectorize** with `CountVectorizer` (bag-of-words).
7. **Compute** pairwise **Cosine Similarity** across the entire catalog.
8. **Prune** to the top 200 nearest neighbors per movie — keeps storage small, deployment fast.
9. **Serve** recommendations from the precomputed table — no recomputation at request time.

---

## 📂 Project Structure

```
Movie-Recommendation-System/
│
├── movie_reco_model.py      # Offline: preprocessing, vectorization, similarity matrix
├── movie_reco_app.py        # Online: Streamlit UI & recommendation logic
├── movies.pkl                # Processed movie metadata
├── top_similarity.pkl        # Top-200 similarity lookup table
├── tmdb_5000_movies.csv      # Raw TMDB movie data
├── tmdb_5000_credits.csv     # Raw TMDB cast/crew data
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Tools |
|---|---|
| **Language** | Python |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-Learn (CountVectorizer, Cosine Similarity) |
| **NLP** | NLTK (Porter Stemmer) |
| **Frontend** | Streamlit |
| **External Data** | TMDB API, TMDB 5000 Movie Dataset |
| **Networking** | Requests |

</div>

---

## 🚀 Quick Start

> 💡 Want to try it without installing anything? **[Launch the live app →](https://ai-movie-recommendation-system1.streamlit.app/)**

**1. Clone the repo**
```bash
git clone https://github.com/MuazzamAmanat/movie-recommendation-system.git
cd movie-recommendation-system
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Add your TMDB API key**

Create `.streamlit/secrets.toml`:
```toml
TMDB_API_KEY="YOUR_API_KEY"
```
> Get a free key at [themoviedb.org/settings/api](https://www.themoviedb.org/settings/api)

**4. Build the model**
```bash
python movie_reco_model.py
```
Generates `movies.pkl` and `top_similarity.pkl`.

**5. Launch the app**
```bash
streamlit run movie_reco_app.py
```

Open `http://localhost:8501` and start exploring. 🎉

---

## 🗺️ Roadmap

- [ ] Autocomplete search bar
- [ ] Genre tags on recommendation cards
- [ ] Ratings & release year display
- [ ] Trailer embeds
- [ ] Genre-based filtering
- [ ] "Why this movie?" recommendation explanations
- [ ] Mobile-responsive UI overhaul

---

## 🙏 Acknowledgements

- [**TMDB**](https://www.themoviedb.org/) — movie metadata and poster imagery
- [**Scikit-Learn**](https://scikit-learn.org/) — vectorization and similarity utilities
- [**Streamlit**](https://streamlit.io/) — the web app framework

---

## 📄 License

Built for learning and portfolio purposes. Feel free to fork, extend, and experiment.

<div align="center">

*If this project helped you, consider giving it a ⭐ on GitHub.*

</div>
