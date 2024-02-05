from datasets import load_dataset


def load_email_spam_dataset():
    full_dataset = load_dataset("TrainingDataPro/email-spam-classification")

    # Split the dataset into train and validation sets
    dataset = full_dataset['train'].train_test_split(test_size=0.2)

    # Now, dataset is a dictionary with two keys: 'train' and 'test'
    # 'train' corresponds to the training set
    # 'test' corresponds to the test set
    
    train = dataset['train']
    test = dataset['test']
    
    train_clean = []
    test_clean = []
    
    for sample in train:
        cleaned_sample = {
            "inputs": {
                "subject": sample['title'],
                "body": sample['text']
            },
            "outputs": {
                "is_spam": sample['type'] == 'spam'
            }
        }
        train_clean.append(cleaned_sample)
        
    for sample in test:
        cleaned_sample = {
            "inputs": {
                "subject": sample['title'],
                "body": sample['text']
            },
            "outputs": {
                "is_spam": sample['type'] == 'spam'
            }
        }
        test_clean.append(cleaned_sample)
        
    return {
        "train": train_clean,
        "test": test_clean
    }