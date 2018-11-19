echo off
call cd ..
echo Activating Conda Environment
call C:\Users\spittlemeister\anaconda3\Scripts\activate.bat TF
cls
echo Running Evaluation Script...
python ./src/evaluate/eval.py -x_tst ./datasets/TestData/x_test.npy -y_tst ./datasets/TestData/y_test.npy

pause