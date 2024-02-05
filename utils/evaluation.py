import pandas as pd


def evaluate(model=None, dataset=None, split='train', limit=None, metrics={}, debug=False):
    if model is None:
        raise "Must provide a model"
        
    if dataset is None:
        raise "Must provide a dataset"
        
    if split not in ['train', 'test']:
        raise "Split must either be 'train' or 'test'"
        
    ds = dataset['train'] if split == 'train' else dataset['test']
    
    if limit:
        ds = ds[0:limit]
    
    inputs = []
    predictions = []
    references = []
    metric_scores = {}
        
    for sample in ds:
        sample_inputs = sample['inputs']
        sample_outputs = sample['outputs']

        prediction = model(**sample_inputs)
        
        inputs.append(sample_inputs)
        references.append(sample_outputs)
        predictions.append(prediction)
        
    # compute metrics for every output field
    for field in references[0].keys():
        metric_scores[field] = {}

        for metric in metrics.keys():
            metric_fields = metrics[metric]["only"]
            metric_function = metrics[metric]["function"]
            
            if field in metric_fields:
                field_predictions = [prediction[field] for prediction in predictions]
                field_references = [reference[field] for reference in references]

                metric_scores[field][metric] = metric_function(predictions=field_predictions, references=field_references)
    
    if debug:
        pd.set_option('display.max_colwidth', 500)
        pd.set_option('display.max_rows', None)
        
        df_metrics = pd.DataFrame(metric_scores).T
        display(df_metrics)
        
        data = {}
        
        for key in predictions[0].keys():
            data["exact_match_" + key] = [prediction[key]==reference[key] for prediction, reference in zip(predictions,references)]
            
        for key in predictions[0].keys():
            data["prediction_" + key] = [prediction[key] for prediction in predictions]
            
        for key in references[0].keys():
            data["target_" + key] = [target[key] for target in references]

        for key in inputs[0].keys():
            data["input_" + key] = [input[key] for input in inputs]
            
        df = pd.DataFrame(data)
        display(df)


    return metric_scores