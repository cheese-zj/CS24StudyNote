#!/bin/bash

cd preparations

echo "Delete the Stock database"
python3 Drop_database.py

echo "Re-create database"
python3 create_database.py

echo "Re-create tables"
python3 create_tables.py