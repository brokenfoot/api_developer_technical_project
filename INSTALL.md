# Requirements
- Built with python 3.6.6
- Python packages: falcon, pandas, and gunicorn

# Install
To install and run in a virtual environment:
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
gunicorn app:app
```