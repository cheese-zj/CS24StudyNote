cd preparations
pwd
echo "Drop database Stock:"
python3 drop_database.py
echo " "

echo "Create database Stock:"
python3 create_database.py
echo " "

echo "Create table(s):"
python3 create_tables.py