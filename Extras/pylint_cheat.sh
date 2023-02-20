#!/bin/bash

# Set the directory for output and check if it exists. Create if no
main="$PWD" # The root directory of the project
dir="${PWD}/pylint_result" # The directory to house all pylinting reports
if [ ! -d "$dir" ]; then
    mkdir $dir
fi

# $1 = name of file
# $2 = path to python file
pylinter(){
    python_file="$main/$2"
    pylint_report="$dir/$1_pylint.txt"
    echo "Adding pylint result for $1 - $pylint_report"
    if [ ! -f "$pylint_report" ]; then
        touch $pylint_report
    fi
    pylint $python_file > $pylint_report
    echo "Finished creating pylint result for $1"
    echo ""
}

# Pylinting files
pylinter "lab6" "lab6.py"
# pylinter "lab1_model" "models/lab1_model.py"
# pylinter "lab2_password" "models/lab2_password_model.py"
pylinter "lab2_percentage" "models/lab2_percentage_model.py"