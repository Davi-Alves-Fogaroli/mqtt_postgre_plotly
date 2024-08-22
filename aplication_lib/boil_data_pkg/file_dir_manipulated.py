import os, shutil
import time
import json

def create_file(dictionary):
    #implement '.env' (hide important variables/informations)
    absolute_path="C:/Users/davi.alves/analytic_eye_tests/paho_postgre_plotly/aplication_lib/boil_data_pkg"
                    
    #Create a directory
    os.mkdir("dinamyc_files")
    #Change to the new directory
    os.chdir("dinamyc_files")

    #Create dile and writr to it
    with open("created_file.json", "w") as file:
        file.write(json.dumps(dictionary))
        file.close()
        #implementar nomenclatura dinamica
        resposta = input("Caso va gerar uma nova pasta com codigo digite 'S', para nao ter problemas as pastas dinamicas: ")

        if resposta.upper() == 'S':
            os.remove("created_file.json")
            time.sleep(2)
            print(f"{absolute_path}")
            os.chdir(f"{absolute_path}")
            os.rmdir("dinamyc_files") # empty-dir
            # shutil.rmtre("nonempty-dir")

    return 