# Save the current directory and the script's directory, since build must be run from the project root
$curloc = $pwd
$scriptloc = $PSScriptRoot

# Back up the old PYTHONPATH so it can be restored later
$oldPythonpath=$Env:PYTHONPATH

# Build the program
Set-Location $scriptloc/..
$Env:PYTHONPATH = ""
flake8 --max-line-length=160 --ignore W605,W503,W504 --builtins ossdbtoolsservice,View ossdbtoolsservice
flake8 --max-line-length=160 --ignore W605,W503,W504 --builtins ossdbtoolsservice,View tests
flake8 --max-line-length=160 --ignore W605,W503,W504 --builtins ossdbtoolsservice,View mysqlsmo

# Restore the old PYTHONPATH and move back to the original directory
Set-Location $curloc
$Env:PYTHONPATH = $oldPythonpath
