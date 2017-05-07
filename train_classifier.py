from Trainer import Trainer
from datetime import datetime

def main():
    started = datetime.now()
    
    trainer = Trainer()

    trainer.train_MNB_classifier()
    finished = datetime.now()
    
    print 'Started MNB at: ',started
    print 'Finished MNB at: ',finished
    print 'Time taken: ',(finished-started)

main()
