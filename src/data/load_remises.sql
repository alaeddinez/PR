select
   DISTINCT (CONCAT(CAST(NUM_TYPETT AS string),'-',CAST(NUM_ETT AS string),'-',
   CAST(NUM_CAI AS string),'-',CAST(NUM_TIC AS string),'-', 
   CAST(DAT_TIC AS string),'-',CAST(HEU_TIC AS string))) AS primary_key
from `dfdp-teradata6y.SalesLmfr.TF001_VTE_REMTICCAI`
where
1=1
AND  
extract(year from DAT_VTE) = var_year 
and
num_REM in (12 ,13)