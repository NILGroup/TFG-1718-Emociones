#!/bin/bash
echo "STARTING TESTS"
echo "-----------------------PERCENTAGES TEST-----------------------"
python Codigo/porcentajes_test.py
echo "-----------------------AGREED_EMOTION TEST-----------------------"
python Codigo/consensuada_test.py
echo "-----------------------MAIN_EMOTION TEST-----------------------"
python Codigo/mayoritaria_test.py
