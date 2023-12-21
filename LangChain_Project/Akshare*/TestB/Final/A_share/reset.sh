cd preparation
pwd
echo "Drop database Stock_mul:"
python3 drop_database.py
echo " "

echo "Create database Stock_mul:"
python3 create_database.py
echo " "

echo "Create table(s):"
python3 create_tables.py