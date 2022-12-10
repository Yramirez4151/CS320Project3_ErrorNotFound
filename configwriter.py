import configparser
import os.path

Config_path = os.path.dirname(__file__)
config = configparser.ConfigParser()	

def readConfig(file_name = 'Config/conf.ini', section = 'default'):
    filename = os.path.join(Config_path,file_name)
    config.read(filename)

    db = {}
    if config.has_section(section):
        params = config.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

