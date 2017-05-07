from Trainer import Trainer
from datetime import datetime

def main():
    started1 = datetime.now()
    trainer = Trainer()
    trainer.train_SVM_classifier()    
    finished1 = datetime.now()

    print 'Started SimSVM at: ',started1
    print 'Finished SimSVM at: ',finished1
    print 'Time taken: ',(finished1-started1)

main()
