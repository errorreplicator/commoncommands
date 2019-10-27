import pandas a pd
import numpy as np

def ds_size(dataset):
    return (dataset.memory_usage().sum()) / (1024 ** 2)

def ds_statistics(df_names,df_lists) :
    datasets_df = pd.DataFrame(columns=['Dataset','Number of Rows','Number of Columns','Size (MB)'])
    rows = [df.shape[0] for df in df_lists]
    columns = [df.shape[1] for df in df_lists]
    size_MB = [ds_size(df) for df in df_lists]

    datasets_df['Dataset'] = df_names
    datasets_df['Number of Rows'] = rows
    datasets_df['Number of Columns'] = columns
    datasets_df['Size (MB)'] = size_MB
    datasets_df = datasets_df.set_index('Dataset')
    datasets_df = datasets_df.sort_values('Size (MB)')
    return datasets_df

def ds_optimization(dataframe,categorical = []):
    df = dataframe.copy()
    int_types = {np.int8 : (np.iinfo(np.int8).min,np.iinfo(np.int8).max),
                 np.int16: (np.iinfo(np.int16).min,np.iinfo(np.int16).max),
                 np.int32 : (np.iinfo(np.int32).min,np.iinfo(np.int32).max),
                 np.int64 : (np.iinfo(np.int64).min,np.iinfo(np.int64).max)
                }
    float_types = {np.float16: (np.finfo(np.float16).min,np.finfo(np.float16).max),
                   np.float32: (np.finfo(np.float32).min,np.finfo(np.float32).max),
                   np.float64: (np.finfo(np.float64).min,np.finfo(np.float64).max)
                  }
    for col in df.columns:
        col_type = df[col].dtypes
        col_min = df[col].min()
        col_max = df[col].max()
        if (str(col_type)[:3] == 'int') & (str(col) in categorical):
            df[col] = pd.Categorical(df[col])
        elif str(col_type)[:3] == 'int':
            for dtype,drange in int_types.items():
                if (col_min > drange[0]) & (col_max < drange[1]):
                    df[col] = df[col].astype(dtype)
                    break
        elif str(col_type)[:5] == 'float':
            for dtype,drange in float_types.items():
                if (col_min > drange[0]) & (col_max < drange[1]):
                    df[col] = df[col].astype(dtype)
                    break
    return df
