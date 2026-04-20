from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

"""Build a logistic regression pipeline."""
def build_logistic_model(preprocessor) -> Pipeline:
    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("classifier", LogisticRegression(max_iter=1000, random_state=42)),
        ]
    )

"""Build a random forest pipeline."""
def build_random_forest_model(preprocessor) -> Pipeline:
    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "classifier",
                RandomForestClassifier(
                    n_estimators=200,
                    max_depth=6,
                    min_samples_split=5,
                    min_samples_leaf=2,
                    random_state=42,
                ),
            ),
        ]
    )