# Tendencias e Innovación en Tecnología Agrícola
# Autor: servio@palacios.com
# Fecha: 2022.09.06
# Editado: 2022.09.06
import csv

with open('20220905_participants.csv', newline='') as csv_file:
    data_source_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
    for row in data_source_reader:
        #print(', '.join(row))
        print(row)
