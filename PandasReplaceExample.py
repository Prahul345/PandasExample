import numpy as np
import pandas as pd

country_code = np.random.choice(['AE','BH','DZ','EG','IQ','JO','OM','QA','SA','TN','LB','KE','NG','ZA','PK'],size=1000)
#print("********",type(country_cd))

data=pd.DataFrame(country_code)
#print(data)

data['B'] = data[0].replace(['AE','BH','DZ','EG','IQ','JO','OM','QA','SA','TN','LB','KE','NG','ZA','PK'], ['United Arab Emirates', 'Bahrain','Algeria','Egypt','Iraq','Jordan','Oman','Qatar','Saudi Arabia','Tunisia','Lebanon','Kenya','Nigeria','South Africa','Pakistan'])
#print(data['B'])
print(data)