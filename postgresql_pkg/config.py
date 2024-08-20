# this lib able us to read '.ini' file structure {"more datail": "https://docs.python.org/3/library/configparser.html"}
from configparser import ConfigParser

def postgres_config(filename="database.ini", section="postgresql"):
    #creat a parser (analisador)
    parser = ConfigParser()
    parser.read(filename)
    data_base={}
 
    if parser.has_section(section):
        params = parser.items(section)
        # print("\nn params: ", params ,"\\n")
        for param in params:
            data_base[param[0]] = param[1]

    else:
        raise Exception(f"Section '{section}' is not found in the '{filename}' file.")
    
    return data_base
