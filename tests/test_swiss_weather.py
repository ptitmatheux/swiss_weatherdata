import swiss_weather.gbm as gbm

df = gbm.get_smn_stations_info(full_description=False)
print(df.head())

print('toto')