import pickle
import cProfile
import pstats
import io 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

def train_model():
    iris = load_iris()
    clf = RandomForestClassifier()
    clf.fit(iris.data, iris.target)
    with open('modle/my_model.pkl',"wb") as f:
        pickle.dump(clf, f)
if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()
    train_model()
    profiler.disable()
    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumtime')
    ps.print_stats()
    with open("model/profile.txt", "w") as f:
        f.write(s.getValue())
