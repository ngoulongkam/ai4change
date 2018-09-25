Machine Setup
===================

Install Brew:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

Install Python:
```
brew install python
```

Install Pip:
```
curl -O http://python-distribute.org/distribute_setup.py
python distribute_setup.py
curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
python get-pip.py
```

Installing and using virtualenv

virtualenv is a python tool used for managing installed dependencies. All dependencies are install to your own virtual environment and these requirements are output to a requirements.txt file.

```bash
# Install virtualenv
pip install virtualenv

# Create your own local virtualenv
virtualenv twitter_project

# Activate your virtualenv
source twitter_project/bin/activate
```

Once you have sourced your virtualenv you can install all requirements from the requirements.txt
```bash
pip install -r requirements.txt
```

If you install any new requirements then you can output these to the requirements.txt file
```bash
pip freeze > requirements.txt
```