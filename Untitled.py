
# coding: utf-8

# In[1]:



from full_database_feature_extraction import save_features_to_csv_file
import DataImputation

list_missing_data_percentage = [0, 5, 10, 20, 30, 60, 90]
num_iterations = 25
imputation_strategy =  DataImputation.KNN_Imputation
#imputation_strategy =  None

for missing_data_percentage in list_missing_data_percentage:
    save_features_to_csv_file(missing_data_percentage,  num_iterations, imputation_strategy)

