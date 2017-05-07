import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from datetime import datetime
import time

class Trainer(object):
    
    def __init__(self):
        td = np.load('bin_data/training_fv.npy').item()
        self.samples = td['samples']
        self.labels = td['labels']
        
    
    def train_MNB_classifier(self):
        classifier = MultinomialNB()
        classifier.fit(self.samples,self.labels)
       	#time.sleep(25) 
        np.save('bin_data/mnb-classifier',classifier)

    def train_SVM_classifier(self):
        classifier = svm.SVC()
        classifier.fit(self.samples,self.labels)
       	#time.sleep(25) 
        np.save('bin_data/svm-classifier',classifier)



