import matplotlib.pyplot as plt
from tensorflow.keras import Model
from tensorflow.math import confusion_matrix
import numpy as np
import seaborn as sns
import pandas as pd

def plot_loss(history, filename='model_loss.png'):
    # clear the current firgure
    plt.clf()
    plt.cla()
    plt.close()

    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model Loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['train', 'test'], loc='upper right')
    plt.savefig(filename)

def plot_accuracy(history, filename='model_accuracy.png'):
    # clear the current firgure
    plt.clf()
    plt.cla()
    plt.close()
    
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model Accuracy')
    plt.ylabel('Loss')
    plt.xlabel('Accuracy')
    plt.legend(['train', 'test'], loc='upper left')
    plt.savefig(filename)

def plot_confusion(model, X_test, Y_test, labels, filename='confusion_matrix.png'):
    y_pred = model.predict(X_test)
    y_pred = np.argmax(y_pred,axis=1)
    con_mat = confusion_matrix(labels=Y_test, predictions=y_pred).numpy()

    # normalize rows
    sum_of_rows = con_mat.sum(axis=1)
    normalized_con_mat = con_mat / sum_of_rows[:, np.newaxis]

    # clear the current firgure
    plt.clf()
    plt.cla()
    plt.close()

    sns.heatmap(normalized_con_mat, annot=True, cmap=plt.cm.Blues, xticklabels=labels, yticklabels=labels, fmt='.2f')
    plt.tight_layout()
    plt.title('Confusion Matrix')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.savefig(filename)

def read_csv_log(filename='model_log.csv'):
    return pd.read_csv(filename, sep=',', engine='python')
