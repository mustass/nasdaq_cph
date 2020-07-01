import get_NASDAQCPH_tikers as gs 
import match_cvrs as mc
import get_Financial_data as stonks
import calc_stuff as calc
import Financial_data_class as fdc

Finance =fdc.financialMeasures()

#print(Finance.log_returns)w        
#print(Finance.to_monthly(Finance.returns,'avg'))
print(Finance.create_grand_table())
