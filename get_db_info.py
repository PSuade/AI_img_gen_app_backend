from configparser import ConfigParser

def get_db_params():
    parser=ConfigParser()
    parser.read(['database.ini'])

    db_params={}
    if parser.has_section('postgresql'):
         key_val_tuple = parser.items('postgresql') 
         for item in key_val_tuple:
             db_params[item[0]]=item[1]

    return db_params
