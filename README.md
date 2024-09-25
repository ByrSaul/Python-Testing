```sh
git clone
cd PYTHON-TESTING

.\venv\Scripts\activate #windows
source env/bin/activate #linux or mac

pip3 install -r requirements.txt

#With coverage
coverage run --source src -m unittest 
coverage report
coverage html

#With unittest
python -m discover unittest tests

#with doctest
pyton -m doctest src/calculator.py 

```
