import pennylane as qml 
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import (accuracy_score,f1_score,confusion_matrix,precision_score,roc_curve,roc_auc_score)
from sklearn.linear_model import LogisticRegression
import torch
import torch.nn as nn
from sklearn.preprocessing import StandardScaler,MinMaxScaler
from sklearn.decomposition import PCA 
import time 
import copy 
import os 
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.svm import SVC

    dev=qml.device("default.qubit",wires=n_qubits)

    @qml.qnode(dev)
    def feature_state(x):
        # Applies embedding and entanglement twice  for more complex encoding due to the twice entanglement
        qml.IQPEmbedding(x,wires=range(n_qubits),n_repeats=2)

        return qml.state()

    def returnstates(X,bandwidth):

        return np.stack([feature_state(x*bandwidth) 
                         for x in X])
    y_train=data["y"]["train"]
    best=None

    for bandwidth in (0.25,0.5,0.75,1):
        train_states=returnstates(data["q"]["train"],bandwidth)

        test_states=returnstates(data["q"]["test"],bandwidth)

        # Create kernel matrix using square overlap method , we map train states to train states while training and test states similarity to train states while testing
        k_train=np.abs((train_states@train_states.conj().T))**2

        k_test=np.abs((test_states@train_states.conj().T))**2

        search=GridSearchCV(SVC(kernel="precomputed",class_weight="balanced"),{"C":[0.1,1,10,100,1000]},cv=5,scoring="roc_auc")

        search.fit(k_train,y_train)
        
        if best is None or search.best_score_>best["cv_auc"]:
            best={"cv_auc":search.best_score_,
                  "model":search.best_estimator_,
                  "k_test":k_test,
                  "bandwidth":bandwidth,
                  "C":search.best_params_["C"]}
        print(f"""Selected bandwidth:{best['bandwidth']}
            Selected C:{best['C']}
            Achieved AUC score{best['cv_auc']}""")

        return best["model"].decision_function(best["k_test"])
