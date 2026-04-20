from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
    RocCurveDisplay,
)


def evaluate_model(
    model,
    X_train,
    X_test,
    y_train,
    y_test,
    model_name: str,
    output_dir: Path,
    roc_filename: str,
):
    """Train a model, evaluate it, and save ROC curve."""
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    print("\n==============================")
    print(f"{model_name.upper()} RESULTS")
    print("==============================")
    print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print(f"ROC AUC:  {roc_auc_score(y_test, y_prob):.4f}")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    RocCurveDisplay.from_predictions(y_test, y_prob)
    plt.title(f"ROC Curve - {model_name}")
    plt.tight_layout()
    plt.savefig(output_dir / roc_filename)
    plt.close()

    return y_pred, y_prob


def save_feature_importance(rf_model, output_dir: Path, top_n: int = 15) -> None:
    """Extract and save feature importance from the random forest model."""
    preprocessor_fitted = rf_model.named_steps["preprocessor"]
    classifier_fitted = rf_model.named_steps["classifier"]

    feature_names = preprocessor_fitted.get_feature_names_out()
    importances = classifier_fitted.feature_importances_

    importance_df = pd.DataFrame(
        {
            "Feature": feature_names,
            "Importance": importances,
        }
    ).sort_values(by="Importance", ascending=False)

    print(f"\n--- Top {top_n} Feature Importances ---")
    print(importance_df.head(top_n))

    importance_df.to_csv(output_dir / "feature_importance.csv", index=False)

    top_features = importance_df.head(top_n).sort_values(by="Importance")

    plt.figure(figsize=(10, 6))
    plt.barh(top_features["Feature"], top_features["Importance"])
    plt.title(f"Top {top_n} Feature Importances - Random Forest")
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.tight_layout()
    plt.savefig(output_dir / "feature_importance_top15.png")
    plt.close()