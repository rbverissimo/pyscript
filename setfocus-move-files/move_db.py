import os;
import shutil;
import sys;
import rarfile;

SOURCE_DIR= r"C:\Users\User\Documents\Received Files"
BASE_BACKUP_DIR= r"C:\backup"

def move_file(file_name, target_dir):
    pass

if __name__ == '__main__':
    if(sys.argv) != 3:
       print("Como usar: python nome_script.py <nome_arquivo> <nome_diretorio_alvo>")
       print("Exemplo: python move_db.py arquivo.fb diretorio. Move o arquivo.fb de Received Files para o diretório em C:/backup/<diretorio>")
       print("É possível também extrair um arquivo dentro de um .rar de mesmo nome do arquivo alvo. python move_db arquivo.rar diretorio: extrairá qualquer arquivo de nome arquivo e colocará ele em C:/backup/<diretorio>")
       sys.exit(1)

    _file = sys.argv[1]
    _dest = sys.argv[2] 

    move_file(_file, _dest)


