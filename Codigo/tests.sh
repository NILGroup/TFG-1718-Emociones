#!/bin/bash
echo "STARTING TESTS"
echo "-----------------------PERCENTAGES TEST-----------------------"
python porcentajes_test.py
echo "-----------------------AGREED_EMOTION TEST-----------------------"
python consensuada_test.py
echo "-----------------------MAIN_EMOTION TEST-----------------------"
python mayoritaria_test.py