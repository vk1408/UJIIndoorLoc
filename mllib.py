import pandas as pd
# build correlation matrix
def get_correlation(df, threshold):
    '''
    args: dataframe, threshold
    returns dataframe of correlating features
    for given threshold
    '''
    correlation_matrix = df.corr()
    list_corr = []
    for row in correlation_matrix.index:
        for col in list(correlation_matrix.columns):
            if abs(correlation_matrix.loc[row,col]) > threshold and col<row:
                list_corr.append((row,col,correlation_matrix.loc[row,col]))
    return pd.DataFrame(list_corr, columns=['f1','f2','corr'])

# check  metric of the model
from sklearn.metrics import accuracy_score, confusion_matrix, recall_score

def model_check(y_true, y_pred, model, output ='accuracy'): 
    '''
    returns selected metric
    '''
    if output== 'accuracy':
        acc_sc = accuracy_score(y_true, y_pred)
        return acc_sc
    elif output== 'recall':
        recall_sc= recall_score(y_true, y_pred)
        return recall_sc
    elif output == 'cmatrix':
        conf_matrix = pd.DataFrame(confusion_matrix(y_true, y_pred))
        conf_matrix.set_index(model.classes_, inplace=True)
        conf_matrix.columns = model.classes_
        return conf_matrix

# conver unix time
from datetime import datetime
def get_time(val,form='%Y-%m-%d %H:%M:%S'):
    '''
    converts integer unix time to given format
    '''
    try:
        return datetime.utcfromtimestamp(val).strftime(form)
    except:
        return val