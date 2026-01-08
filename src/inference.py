import joblib

MODEL_PATH = "model/depression_pipeline1.joblib"

def load_model():
    return joblib.load(MODEL_PATH)

def predict(model, text: str):
    return model.predict([text])[0]

def predict_confidence(model, text: str):
    clf = model.named_steps["model"]
    if hasattr(clf, "predict_proba"):
        return clf.predict_proba([text])[0][1]
    return None
