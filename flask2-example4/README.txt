    ##################
    #######VENV#######
    ##################
    '''virtual environment'''
python3.9 -m venv venv/cpython39
source venv/cpython39/bin/activate
pip3 install -r requirements.txt


        ##################
        ###config.toml#### 
        ##################
    '''configuration file'''
DEBUG = true
SECRET_KEY = "development key"


        ##################
        ###STARTING APP###
        ##################
flask run --reload 