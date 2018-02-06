#!/bin/bash
echo "STARTING TESTS"
echo "-----------------------PERCENTAGES TEST-----------------------"
python Servidor/porcentajes_test.py
echo "-----------------------AGREED_EMOTION TEST-----------------------"
python Servidor/consensuada_test.py
echo "-----------------------MAIN_EMOTION TEST-----------------------"
python Servidor/mayoritaria_test.py
