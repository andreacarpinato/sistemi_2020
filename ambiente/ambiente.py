import matplotlib.pyplot as mat 
import csv
anno = []
temperatura =[]
with open('dati.csv') as csvfile :
    csvreader=csv.reader(csvfile,delimiter=',')
    line_count=0
    for row in csvreader:
        if line_count > 4:
            print(f'\t{row[0]},{row[1]}')
            anno.append(int(row[0]))
            temperatura.append(float(row[1]))
        line_count +=1
print("fine")
mat.figure()  #crea la figura,la finstra vuota
mat.bar(anno,temperatura) # crea il grafico(x,y)
mat.show() #mostra grafico



