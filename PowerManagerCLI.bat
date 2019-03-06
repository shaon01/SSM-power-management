@echo off
IF "%1"=="" (
echo NO ARGUMENT PROVIDED
)ELSE (
python3 PowerManagerCLI.py %1
echo in command line the argument is: %1
)