# To create virtual environment
python3 -m venv venv
# To activate virtual environment
source ./venv/bin/activate
# To upgrade pip
pip install --upgrade pip
# To install some pips
pip install pylint
pip install jedi
pip install pyjwt
pip install flask
# For more information: https://github.com/PyMySQL/mysqlclient#install
# # Assume you are activating Python 3 venv
# $ brew install mysql-client
# $ echo 'export PATH="/usr/local/opt/mysql-client/bin:$PATH"' >> ~/.bash_profile
# $ export PATH="/usr/local/opt/mysql-client/bin:$PATH"
# $ pip install mysqlclient
pip install flask_mysqldb
pip install pydantic
pip install python-dotenv
# To export dependencies to file
pip freeze > requirements.txt
