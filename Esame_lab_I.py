

class ExamException(Exception):
    pass

##1-

import os
class CSVTimeSeriesFile:
    def __init__(self, my_files):
        self.name = my_files

        if not os.path.exists(my_files):
            raise ExamException("Errore: Questo file non esiste")
       
    
    def get_data(self, nome_città):

        with open(self.name) as test:    ##verifichiamo che il nome della città sia presente
            lista_città = []
            for lines in test:
                lines = lines.strip().split(",")
                lista_città.append(lines[3])
            if nome_città not in lista_città:
                raise ExamException("Errore: il nome della città non è presente nel file")
                    

        with open(self.name) as files:
            my_list = []
            for linea in files:
                linea = linea.strip().split(",")
                if linea[3] == nome_città:
                    del linea[6]
                    del linea[5]
                    del linea[4]
                    del linea[3]
                    del linea[2]
                    try:
                        linea[1] = float(linea[1])
                    except:
                        continue
                    my_list.append(linea)
            return my_list
        
            # # for i in my_list:    ##fa la stesa cosa con il codice giu
            # #     if i[1].strip() == '':
            # #         continue
            # #     else:
            # #         i[1] = float(i[1])
            # #         lista.append(i)
                    
            # # return lista

        

time_series_file = CSVTimeSeriesFile("C:/Users/delma/OneDrive/Bureau/GlobalLandTemperaturesByMajorCity.csv" )
time_series_italy = time_series_file.get_data("Rome")
print (time_series_italy)
print("\n")




##2-

def compute_slope(time_series, first_year, last_year):
    my_dict = {}
    my_dict_media_annuale = {}
    list_anni = []
    for i in range (last_year -first_year):
        list_anni.append(str(first_year + i))
    list_anni.append(str(last_year))
    #return list_anni
     
    if  len(list_anni) == 0 or last_year < first_year:
        raise ExamException("L'intervallo degli anni non è valido")

    for element in time_series:
        anni = element[0].strip().split("-")
        element[0] = anni[0]
    #return time_series
        if element[0] not in list_anni:
            continue
        if element[0] not in my_dict:
            my_dict[element[0]] = []              
        my_dict[element[0]].append(element[1])   
    #return my_dict
    for el in list( my_dict.keys()):
        if len( my_dict[el]) < 6:
            del (my_dict[el])
    #return my_dict   ## Qui abbiamo raggruppato le temperature per anno nel range specificato
    for dati in my_dict.keys():
        somma = sum (my_dict[dati])
        leng = len(my_dict[dati])
        media = somma / leng
        my_dict_media_annuale[dati] = media
    #return my_dict_media_annuale  ##Qui abbiamo calcolato la media annuale per ogni anno valido
    som = 0
    som_med = 0

    if len( my_dict_media_annuale) == 0:
        raise ExamException("Non si può calcolare la media annuali")
    
    for datti in my_dict_media_annuale.keys():
        datti = int(datti)
        som += datti
        media_anni = som / len( my_dict_media_annuale)
        media_anni = int(media_anni)
        datti = str(datti)
        som_med += my_dict_media_annuale[datti]
        media_temp = som_med / len (my_dict_media_annuale)
        media_temp = round(media_temp, 5)

    som_tot = 0
    x_tot = 0
    for delmas in my_dict_media_annuale.keys():
        som_tot += (int(delmas) - media_anni) * (my_dict_media_annuale[delmas] - media_temp)
        x_tot += (int(delmas) - media_anni) ** 2

        if x_tot == 0:
            raise ExamException("Non si può cacolare il coefficiente angole con 0 al denominatore ")
        
        m = som_tot / x_tot
       
    return m

    






result = compute_slope(time_series_italy, 2000 , 2005 )
print(result)