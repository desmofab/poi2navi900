####################################
#DEVELOPER: desmofab
#NAME: POI2NAVI900
#DESCRIPTION: CONVERT POI FILES INTO NAVI900 FORMAT
#VERSION: 1.0
#RELEASE: STABLE
#UPDATE: 05/05/2017
####################################

import os
import csv
from decimal import Decimal


#Files name
file_csv = "POI.csv"
file_poi = "Privato_1.poi"

#Mi posiziono nella cartella POI
os.chdir('C:/Users/desmo/Desktop/myPOIs/')

#Unisco tutti i files POI CSV
os.system('copy /b *.csv %s /y' % file_csv)


#Apro il file unificato per la conversione
pois_csv = csv.reader(open(file_csv, newline='', encoding='utf-8'), delimiter=',', quoting=csv.QUOTE_NONE)


#Apro il nuovo file che conterrà la conversione
poi_poi = csv.writer(open(file_poi, 'w', newline = '', encoding='utf-8'), delimiter = ',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)


#Ciclo le righe
for poi in pois_csv:
	poi_poi.writerow([ Decimal(poi[0]), Decimal(poi[1]), poi[2] ])







# with open(file_poi, 'w', newline='', encoding='utf-8') as f:
# 	writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
# 	writer.writerows(pois_csv)


# exit()
