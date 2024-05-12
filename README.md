
# Vendor Managment system
The Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics.

# Modules Split

### Vendor
- All the vendor based models and details will be in this module, which includes:
  - Vendor profile
  - vendor performance
  - and seperate model for vendor performance history


### Purchase order
- All the purchase based models and details will be in this module, which includes:
  - purchase order against a vendor



## Setting up project

create folder 
```
mkdir folder_name
```

inside the folder clone this
```shell
git clone https://github.com/shilpasasidharan97/Vendor-managment.git
```

create a virtualenvironment and activate that :
```shell
virtualenv venv
source venv/Source/activate (for windows)
source venv/bin/activate (ubuntu)
```

change directory to vendorvendor_management_system/ :
```shell
cd vendorvendor_management_system/
```

Install requirment :
```shell
pip install -r requirements.txt
```

database change :
```shell
python manage.py runserver
```
