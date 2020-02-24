SELECT DISTINCT 
CONCAT(CAST(NUM_TYPETT AS string),'-',CAST(NUM_ETT AS string),'-',CAST(NUM_CAI AS string),'-',CAST(NUM_TIC AS string),'-', CAST(DAT_TIC AS string),'-',CAST(HEU_TIC AS string)) as primary_key,
NUM_ART,
NUM_LIGTIC,
QTE_ART,
NUM_TYPTRN,
COD_TYPCV,
NUM_TYPREAPPRO	 as NUM_TYPREAPPR_MAG
from 
`dfdp-teradata6y.SalesLmfr.TF001_VTE_LIGTICCAI`
where 1=1 
AND extract(year from DAT_VTE) = var_year 
and NUM_BU = 1
and NUM_TYPTRN = var_typtrn and COD_TYPCV  = var_codtypv