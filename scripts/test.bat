echo off
call cd ..
echo Activating Conda Environment
call C:\Users\spittlemeister\anaconda3\Scripts\activate.bat TF
cls
echo Running Test Script...
python ./test/test.py -v

pause