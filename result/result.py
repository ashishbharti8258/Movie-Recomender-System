import pickle
import pandas as pd

# ==============================
# Loading the Saved Pickle Files
# ==============================

vectorizer = pickle.load(
    open(r"C:\Users\ashis\Courses\Projects\Movie-Recomender-System\tfidf_vectorizer.pkl", "rb")
)

similarity = pickle.load(
    open(r"C:\Users\ashis\Courses\Projects\Movie-Recomender-System\similarity_matrix.pkl", "rb")
)

content_data = pickle.load(
    open(r"C:\Users\ashis\Courses\Projects\Movie-Recomender-System\content_data.pkl", "rb")
)

idx = pickle.load(
    open(r"C:\Users\ashis\Courses\Projects\Movie-Recomender-System\idx.pkl", "rb")
)

print("All files loaded successfully!")

# ==============================
# Recommendation Function
# ==============================

def recommend_movies(movie, top_n=5):

    # normalize input
    movie = movie.strip().lower()

    # create lowercase mapping of idx
    idx_lower = {k.lower(): v for k, v in idx.items()}

    # check existence
    if movie not in idx_lower:
        return "Movie not found in dataset"

    movie_index = idx_lower[movie]
    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:top_n+1]

    data = []

    for i, score in movie_list:
        data.append({
            "Movie": content_data.iloc[i].title,
            "Similarity": round(float(score), 3)
        })

    return pd.DataFrame(data)
# ==============================
# Test Recommendation System
# ==============================

movie_name = input(
    "Enter a movie name for recommendations: "
)

result = recommend_movies(movie_name)

# ==============================
# Display Final Output Table
# ==============================

if result is not None:

    print("\nRecommendation Table:\n")
    print(result)

    # ==============================
    # Save Results
    # ==============================

    result.to_csv(
        "recommended_movies.csv",
        index=False
    )

    print("\nResults saved as recommended_movies.csv")