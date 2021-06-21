from app.app import app
import pickle
from app.libs.pricing import get_price

if __name__ == "__main__":
    model = pickle.load(open("app/models/in_model.pkl", "rb"))
    colname = pickle.load(open("app/models/colname.pkl", "rb"))
    app.run()