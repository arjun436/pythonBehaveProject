@echo off
set folder="allurereports"
IF EXIST "%folder%" (
    cd /d %folder%
    for /F "delims=" %%i in ('dir /b') do (rmdir "%%i" /s/q || del "%%i" /s/q)
)

cd..
pytest -s -v -n 3 --alluredir="./allurereports"
allure serve ./allurereports

EXIT /B