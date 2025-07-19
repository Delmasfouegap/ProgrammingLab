
#           PRIMO ESAME:--

class ExamEception(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, my_files):
        self.name = my_files
        try:
           f= open(my_files, "r")
           f.close()
        except:
            raise ExamEception("ERRORE, impossibile aprire il file ! ")

    def get_data(self):
        my_list = []
        with open(self.name, "r") as files:
            for linea in files:
                element = linea.strip().split(",")
                if element[0] != "date":
                    my_list.append(element)
        return(my_list)
    

time_series_file = CSVTimeSeriesFile(r"C:\Users\delma\Downloads\data (2).csv")
time_series = time_series_file.get_data()
print("\n")
#print(time_series)



def compute_variations(My_time_serie, first_year, last_year, N):
    my_dict_by_anno = {}
    for element in My_time_serie:
        data = element[0].strip().split("-")
        anno = int(data[0])
        try:
            valore = float(element[1])
        except:
            continue
        if anno not in my_dict_by_anno:
            my_dict_by_anno[anno] = []
        my_dict_by_anno[anno].append(valore)
    #return my_dict_by_anno
    my_dict_media = {}
    for elemento in my_dict_by_anno.keys():
        media = sum(my_dict_by_anno[elemento]) / len(my_dict_by_anno[elemento])
        media = round(media, 3)
        my_dict_media[elemento] = media
    #return my_dict_media
    my_dict_media_intervalli = {}
    anni =[]
    table = []
    for i in range(last_year-first_year+1):
        anni.append(first_year+i)
    #return anni
    if N >= (last_year - first_year):
        raise ExamEception("ERROR: N (che vale {}) deve essere minore di last_year - first_year (che vale {})".format(N, last_year - first_year))
    
    array = [i for i in my_dict_by_anno.keys()]

    if first_year not in my_dict_by_anno.keys() or last_year not in my_dict_by_anno.keys():
        raise ExamEception("ERROR: gli estremi dell'intervallo devono essere tra {} e {}.".format( min(my_dict_by_anno), max(my_dict_by_anno)) )

    for m in anni:
        meno = m - N
        for l in range(N):
            table.append(meno+l)
        #return table
        somma = 0
        for de in table:
            try:
                somma += my_dict_media[de] 
                media_mobile = somma / len(table)
            except:
                continue
            media_mobile = round(media_mobile,3)
            my_dict_media_intervalli[m] = media_mobile
    #return my_dict_media_intervalli
    dictionary = {}
    for delmas in my_dict_media_intervalli.keys():
        try:
            var =  my_dict_media[delmas] - my_dict_media_intervalli[delmas]
            dictionary[delmas] = round(var,3)
        except:
            continue
    #return dictionary
    dictionary_finaly = {}
    for yo in dictionary.keys():
        yoo = str(yo)
        dictionary_finaly[yoo] = dictionary [yo]
    return dictionary_finaly
        
   

#    main:
result = compute_variations(time_series, 1953, 1959, 3)

print(result)
 
