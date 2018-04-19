# bibliotecas para manipulacao de dados e de sistema
import csv
import json
import unidecode
import sys

# leitura e saida de arquivos .csv
csv_path = r'C:\Dev\Python\meuremedio-extracao\xls_conformidade_2018_03_14 - formatada.csv'
txt = r'medicamentos.txt'


# leitura do arquivo .csv
def reader_csv(path):
    with open(path, 'r') as csv_file:
        count = 0
        reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)

        for row in reader:
            if count > 0:  # exclusao de cabecalho da planilha
                yield row
            count += 1


# escrita do arquivo .txt
def write_txt(data):
    with open(txt, 'a', newline='') as txt_file:
        txt_file.write(data)


# quantidade de linhas .csv
def count_csv(path):
    with open(path, 'r') as csv_file:
        return sum(1 for row in csv_file)


# escrita dos dados em .json
def write_json(data):
    with open(txt, 'a', newline='') as txt_file:
        # atributos selecionados do arquivo .csv
        atributos = {'principioAtivo': data[0], 'laboratorioCnpj': data[1], 'laboratorioNome': data[2],
                     'laboratorioRegistro': format_value(data[4]), 'nome': data[6], 'apresentacao': data[7],
                     'classeTerapeutica': data[8], 'tipo': data[9], 'precoFabrica': format_number(data[10]),
                     'precoConsumidor0': format_number(data[19]), 'precoConsumidor12': format_number(data[20]),
                     'precoConsumidor17': format_number(data[21]), 'precoConsumidor20': format_number(data[27]), 
                     'restricaoHospitalar': data[28], 'tarja': data[34]}

        json.dump(atributos, txt_file)


# formatar numeros com notacao cientifica
def format_value(data):
    try:
        return int(float(data))
    except:
        return ''


# formatar casas decimais
def format_number(data):
    return data.replace('.', ',')


# formatar dados em unidecode
def set_unicode(data):
    for index, row in enumerate(data):
        data[index] = unidecode.unidecode(row)


# formatar dados em letra maiuscula
def set_uppercase(data):
    for index, row in enumerate(data):
        data[index] = row.upper()


# limpeza e insercao de dados
try:
    row_count_csv = count_csv(csv_path)
    row_count = 0
    write_txt('[')
    for row in reader_csv(csv_path):  # leitura no arquivo .csv
        set_unicode(row)
        set_uppercase(row)
        write_json(row)
        row_count += 1
        if row_count_csv != row_count:
            write_txt(',')
    write_txt(']')
except:
    print("Ooops!", sys.exc_info())  # informacao de erro
