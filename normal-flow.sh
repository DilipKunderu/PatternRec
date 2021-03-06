echo 'Processing training data...'
python process_training_data.py dataset/train/train-data-1

echo 'Now extracting features from training data...'
python extract_features.py

echo 'Now building feature vectors from training data...'
python vectorize_training_data.py

echo 'Now preprocessing test data...'
python process_testing_data.py

echo 'Now building feature vectors from test data...'
python vectorize_testing_data.py

echo 'Now training MNB classifier...'
python train_classifier.py

echo 'Now testing MNB classifier...'
python test_classifier.py

echo 'Now training SVM classifier...'
python train_classifier_SimSVM.py

echo 'Now testing SVM classifier...'
python test_classifier_SimSVM.py
