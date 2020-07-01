flooding_columns = ['Flood_RP100_2041_2070_RCP45Mean',

 'Flood_RP100_2041_2070_RCP85Mean',

 'Flood_RP100_2071_2100_RCP45Mean',

 'Flood_RP100_2071_2100_RCP85Mean',

 'Flood_RP100_2071_2100_RCP85_90Perc',

 'Flood_RP100_Presentday',

 'Flood_RP20_2041_2070_RCP45Mean',

 'Flood_RP20_2041_2070_RCP85Mean',

 'Flood_RP20_2071_2100_RCP45Mean',

 'Flood_RP20_2071_2100_RCP85Mean',

 'Flood_RP20_2071_2100_RCP85_90Perc',

 'Flood_RP20_Presentday',

 'Flood_RP50_2041_2070_RCP45Mean',

 'Flood_RP50_2041_2070_RCP85Mean',

 'Flood_RP50_2071_2100_RCP45Mean',

 'Flood_RP50_2071_2100_RCP85Mean',

 'Flood_RP50_2071_2100_RCP85_90Perc',

 'Flood_RP50_Presentday']

measures=['min', 'max', 'mean', 'median']

new_dict = { i : measures for i in flooding_columns }
print(new_dict)