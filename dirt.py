import pandas as pd

data = {'wydatki': ['kaczka','jabca','piwko'], 
        'kwoty': [480.3,20,4789.4]}

df = pd.DataFrame(data, columns=['wydatki','kwoty'])

print(df)