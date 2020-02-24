import pandas as pd
from data import LoadTickets, LoadRemise
from data import storage_blob
import os

# TODO : charger le fichier caro via Storage (corriger le code ci dessous)
#os.environ['GOOGLE_APPLICATION_CREDENTIALS'] ='/home/alaeddinez/big-data-dev-lmfr-c09b71d85de2.json'
# data = storage_blob(bucket='temp_a',
#                     blob='list_ref_caro.csv').select_bucket(sep=";")

# charger les ficher de caro (uploaded via git)
data = pd.read_csv("gs://temp_a/list_ref_caro.csv", sep =";" )


# charger les lignes de tickets (exemple BV)
lig_tickets = LoadTickets('ticket_line',  year='2020',
                          typtrn='1', codtypv='1').dataframe

lig_remise = LoadRemise('remise', year='2020').dataframe.primary_key


