from Tester import Tester
from datetime import datetime

def main():
    started1 = datetime.now()
    
    tdpath1 = 'bin_data/testing_fv.npy'
    cpath1 = 'bin_data/svm-classifier.npy'
    
    tester = Tester(tdpath1,cpath1)
    tester.test_classifier()
    
    finished1 = datetime.now()
    
    print 'Started SimSVMTest at: ',started1
    print 'Finished SimSVMTest at: ',finished1
    print 'Time taken: ',(finished1-started1)  

main()
