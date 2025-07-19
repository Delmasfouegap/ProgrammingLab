from pathlib import Path

class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    def __init__(self, my_files):
        self.name = my_files
        f = Path(my_files)
        if not f.is_file():
            raise  ExamException("Errore: impossibile aprire il file")
        
        if f.stat().st_size <= 0:
            raise ExamException("Errore: il file `e vuoto o non contiene dati validi")
        

    def get_data(self, country):
        my_list = []
        tab=[]
        with open(self.name, "r") as file:
            
            for test in file:
                test = test.strip().split(",")
                if len(test) < 3:
                    continue
                if test[0] != "dt":
                    tab.append(test[2].strip())
            #return (tab)
            if country not in tab:
                raise ExamException("Errore: il nome del paese ({})non `e presente nel file".format(country))
            
        with open(self.name, "r") as files:  
            #files.seek(0)
            for linea in files:
                linea = linea.strip().split(",")
                if len(linea) < 3:
                    continue

                if linea [2] == country:
                    my_list.append(linea)
            new_list = []
            for i in my_list:
                try:
                    i.pop(2)     
                    i[1] = float (i[1])
                    new_list.append(i)
                except: 
                    continue
            return  new_list



time_series_file = CSVTimeSeriesFile(r"C:\Users\delma\Downloads\GlobalLandTemperaturesByCountry (1).csv")
time_series_italy = time_series_file.get_data("Italy")  

print("\n")
#print(time_series_italy)




def compute_variations(time_series_1, time_series_2, first_year, last_year):
    my_dict = {}

    if not isinstance( first_year , int ) or not isinstance(last_year, int):
        raise ExamException("Errore: l’anno inserito non è un intero")

    for element in time_series_1:
        data = element[0].split("-")
        if len(data) < 1:
            continue
        anno = data[0]
        valore = element[1]
        if anno not in my_dict:
            my_dict[anno] = []
        my_dict[anno].append(valore)
    #return my_dict

    dictionary_media = {}
    for elemento in my_dict.keys():
        try:
            media = sum(my_dict[elemento]) / len(my_dict[elemento])
        except:
            continue
        dictionary_media[elemento] = round(media,4)
    #return(dictionary_media)
    if str(first_year) and str(last_year) not in dictionary_media.keys():
        raise ExamException("Errore: l'intervallo selezionato non contiene valori validi")

    my_dict2 = {}
    for element2 in time_series_2:
        data2 = element2[0].split("-")
        if len(data2) < 1:
            continue
        anno2 = data2[0]
        valore2 = element2[1]
        if anno2 not in my_dict2:
            my_dict2[anno2] = []
        my_dict2[anno2].append(valore2)

    #return my_dict
    dictionary_media2 = {}
    for elemento2 in my_dict2.keys():
        try:
            media2 = sum(my_dict2[elemento2]) / len(my_dict2[elemento2])
        except:
            continue
        dictionary_media2[elemento2] = round(media2,4)
    #return(dictionary_media2)
    if str(first_year) and str(last_year) not in dictionary_media2.keys():
        raise ExamException("Errore: l'intervallo selezionato non contiene valori validi")


    lista = []
    dim = last_year - first_year
    for i in range(dim+1):
        anno = first_year + i
        lista.append(str(anno))
    #return lista
    dictionary_finaly = {}
    for datas in lista:
        try:
            media_fi = dictionary_media2[datas] - dictionary_media[datas]
        except:
            continue
        dictionary_finaly[datas] = round(media_fi,3)
    return dictionary_finaly

    


time_series_file = CSVTimeSeriesFile(r"C:\Users\delma\Downloads\GlobalLandTemperaturesByCountry (1).csv")
time_series_1 = time_series_file.get_data("Italy") 

time_series_file = CSVTimeSeriesFile(r"C:\Users\delma\Downloads\GlobalLandTemperaturesByCountry (1).csv")
time_series_2 = time_series_file.get_data("Cameroon") 

result = compute_variations(time_series_1, time_series_2, 1995, 2000)
print("\n")
print(result)







#------------------------>    
# #         # Una funzione che calcola le medie annuale di una time series
# # def fun_intermedia(my_times_series):
# #     my_dict = {}
# #     for element in my_times_series:
# #         data = element[0].split("-")
# #         if len(data) < 1:
# #             continue
# #         anno = data[0]
# #         valore = element[1]
# #         if anno not in my_dict:
# #             my_dict[anno] = []
# #         my_dict[anno].append(valore)

# #     #return my_dict
# #     dictionary_media = {}
# #     for elemento in my_dict.keys():
# #         try:
# #             media = sum(my_dict[elemento]) / len(my_dict[elemento])
# #         except:
# #             continue
# #         dictionary_media[elemento] = round(media,4)
# #     print(dictionary_media)

#print(fun_intermedia(time_series_italy))
    