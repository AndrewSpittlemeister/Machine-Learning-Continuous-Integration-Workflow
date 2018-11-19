echo off
call cd ..
echo Activating Conda Environment
call C:\Users\spittlemeister\anaconda3\Scripts\activate.bat TF
cls
echo Running Training Script...
python ./src/train/train.py -x_trn ./datasets/TrainingData/x_train.npy -y_trn ./datasets/TrainingData/y_train.npy

pause