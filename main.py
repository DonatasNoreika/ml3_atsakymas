import pickle
import sklearn

with open('fish_predictor.pkl', 'rb') as f:
    predictor = pickle.load(f)

weight = float(input("Weight (ex.: 242):"))
length1 = float(input("Length1 (ex.: 24):"))
length2 = float(input("Length2 (ex.: 25):"))
length3 = float(input("Length3 (ex.: 30):"))
height = float(input("Height (ex.: 12):"))
width = float(input("Width (ex.: 5):"))

res = predictor.predict([[weight, length1, length2, length3, height, width]])
print(res[0])
