#cookie cutter ml_startup file

0.) create git repo
1.) git init, commit, create remote repo and push
2.) dvc init and add raw data file
3.) create gdrive/s3/blob/gcs storage 
4.) create remote dvc repo and push


5.) create component pipeline with utils
6.) create dvc pipeline
7.) track performance with mlflow

debug mode - use 5-10% of data
compoenent must have training and predict mode
-training mode save data
-predict mode returns data for next stage

######################################
What are the data to be tracked?

1. assembled_data should be tracked
    -add assembled_data to remote dvc repo
2. best_artifact should be tracked