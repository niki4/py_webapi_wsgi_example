# py_webapi_wsgi_example
Simple example of the wsgi-compatible API written on pure Python

It uses uWSGI built-in server to run the script. 
Of course both the server and the script are for demonstration only and not 
intended to use in production.

# Setting up and running
Once you've cloned the repo from GitHub, 
make sure you've created a virtual environment for experiments.

Open shell in cloned folder on local drive, then run commands:
```
sudo pip3 install virtualenv

python3 -m virtualenv ./venv

source venv/bin/activate
```
Now you can install some dependencies:
```
sudo pip3 install uwsgi
```
Finally, you're ready to go. Just run the script, which start the uWSGI server with the API app loaded:
```
./run_uwsgi.sh
```
Open the browser and make sure the following endpoints returns the result (for better understanding how it works, play with them with your browser Developer Tools activated (F12 btn) and by reading source code in project .py file):
```
http://localhost:8080/products/1/

http://localhost:8080/products/

http://localhost:8080/cart/non-exist

http://localhost:8080/cart/

http://localhost:8080/
```