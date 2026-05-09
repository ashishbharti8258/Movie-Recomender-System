# Movie Recommendation System

A Content-Based Movie Recommendation System built using **Python**, **Natural Language Processing (NLP)**, and **Machine Learning** techniques. This project recommends movies similar to a given movie based on genres, overview, keywords, tagline, production companies, countries, and spoken languages.

---

# Project Overview

This project uses the **TMDB 5000 Movies Dataset** to build a recommendation engine that suggests similar movies using:

* TF-IDF Vectorization
* Cosine Similarity
* NLP preprocessing techniques
* Text feature engineering

The system analyzes movie metadata and computes similarity scores between movies to generate recommendations.

---

# Features

* Content-based movie recommendation
* NLP text preprocessing
* TF-IDF feature extraction
* Cosine similarity calculation
* Top-N movie recommendations
* Model serialization using Pickle
* Clean and modular implementation

---

# Technologies Used

## Programming Language

* Python

## Libraries

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-learn
* NLTK
* Pickle
* AST
* Regex

---

## Dataset Used

### TMDB 5000 Movies Dataset

This project uses the **TMDB 5000 Movies Dataset**, downloaded from Kaggle.  
The dataset contains metadata for approximately **5000 movies** collected from **The Movie Database (TMDb)**.

The dataset primarily contains:

- Hollywood movies
- English-language films
- International movies from different countries

It mainly focuses on Hollywood cinema and includes popular movies from genres such as:

- Action
- Adventure
- Science Fiction
- Comedy
- Drama
- Thriller
- Fantasy


  Main columns used:
1. Genres
2. Title
3. Overview
4. Keywords
5. Tagline
6. Production Companies
7. Production Countries
8. Spoken Languages

---

# Project Workflow

## 1. Data Loading

The dataset is loaded using Pandas.

```python
pd.read_csv("tmdb_5000_movies.csv")
```

---

## 2. Feature Selection

Important text-based columns are selected:

* genres
* overview
* keywords
* tagline
* production_companies
* production_countries
* spoken_languages

---

## 3. Data Preprocessing

### Handling Missing Values

Missing values in overview and tagline columns are replaced.

### Text Extraction

JSON-like text fields are converted into readable text using `ast.literal_eval()`.

### Text Cleaning

The following preprocessing steps are applied:

* Lowercasing
* Removing punctuation
* Removing numbers
* Removing extra spaces
* Word stemming using Porter Stemmer

---

## 4. Feature Engineering

All text features are combined into a single column called `tags`.

---

## 5. TF-IDF Vectorization

Text data is converted into numerical vectors using:

---

## 6. Similarity Calculation

Cosine similarity is used to calculate similarity between movies.

---

## 7. Recommendation Function

The system recommends top five similar movies based on cosine similarity scores.

---

## 8. Model Saving

The trained vectorizer and similarity matrix are saved using Pickle.

Saved files:

* tfidf_vectorizer.pkl
* similarity_matrix.pkl
* content_data.pkl
* idx.pkl

---

#  Recommendation Example

Input Movie:

```python
"pirates of the caribbean: at world's end"
```

Output:

| Movie                                                  |Similarity |
| -------------------------------------------------------| ---------- |
| pirates of the caribbean: dead man's chest             | 0.274      |
| pirates of the caribbean: on stranger tides            | 0.239      |
| Pirates of the Caribbean: The Curse of the Black Pearl | 0.212      |

---

# Project Structure

```bash
Movie-Recommender-System/
│
├── dataset/
│   └── tmdb_5000_movies.csv
│
├── RecomenderSytem.ipynb
│
├── tfidf_vectorizer.pkl
├── similarity_matrix.pkl
├── content_data.pkl
├── idx.pkl
│
└── README.md
```


# Learning Outcomes

Through this project, the following concepts were implemented:

* Natural Language Processing
* Feature Engineering
* TF-IDF Vectorization
* Cosine Similarity
* Recommendation Systems
* Data Cleaning and Preprocessing
* Machine Learning Workflow

---


