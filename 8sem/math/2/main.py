import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

RANDOM_STATE = 17
N = 5000
N_FEATURES = 100
N_CLASSES = 2


def createData(n_samples=100, n_features=100, n_classes=2):
    X, y = make_classification(n_samples=n_samples, n_features=n_features, n_classes=n_classes, random_state=RANDOM_STATE, n_informative=n_features, n_redundant=0, n_clusters_per_class=1)
    return X, y

def show_graphic(X, y, lrm):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))

    Z = lrm.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.8)

    plt.scatter(X[:, 0], X[:, 1], c=y, marker='o', edgecolors='k')

    plt.xlabel('Признак 1')
    plt.ylabel('Признак 2')

    plt.title('Логистическая регрессия')
    plt.show()


def logistic_regression(X, y):
    lrm = LogisticRegression(solver='newton-cg')

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.3,
        random_state=RANDOM_STATE
    )

    lrm.fit(X_train, y_train)

    y_pred = lrm.predict(X_test)
    conf_matrix = confusion_matrix(y_test, y_pred)
    errors = np.sum(conf_matrix) - np.trace(conf_matrix)
    accuracy = accuracy_score(y_test, y_pred)

    print("Кол-во ошибок:", errors)
    print("Доля ошибок:", errors/N)
    print("Точность модели:", accuracy)

    if (N_FEATURES == 2):
        show_graphic(X, y, lrm)
    


if __name__=="__main__":
    X, y = createData(n_samples=N, n_features=N_FEATURES, n_classes=N_CLASSES)
    print('Количество данных:', N)
    print('Количество признаков:', N_FEATURES)
    logistic_regression(X, y)




