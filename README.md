# plc_web_ui
User interface website for PLC with Modbus protocol.

Run command:
```
python manage.py runserver
```
# Installation
Install Python and Django and PyModbus.

Open command line in project main folder and type:
```
python manage.py makemigrations ui
```
And then:
```
python manage.py migrate
```
To add admin user type:
```
python manage.py createsuperuser
```
