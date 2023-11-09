#!/usr/bin/env python
# coding: utf-8

# In[22]:


from syntheticdatagenerator import SyntheticDataGenerator
sd = SyntheticDataGenerator()
data = sd.generate_timeseries('2000-01-01',end_date = '2023-10-20', frequency = 'D')
num_features = 9
name_features = ['Activity', 'HeartRate', 'Oxygen', 'Stress', 'ActivityTime', 'BodyTemperature', 'Calories', 'BloodSugarFasting', 'BloodSugarAfterFood']
activity = ['Walking', 'Running', 'Aerobics', 'Yoga', 'Strenth Trainig', 'Cycling']
sd.generate_data(data, num_features, name_features)
sd.generate_target(data, target_name = 'HealthIndicator')
data['Activity'] = sd.generate_text_variable(data, 'Activity', activity)
data['HeartRate'] = sd.set_limit(data['HeartRate'], 60, 120, ceil = 'Y')
data['Oxygen'] = sd.set_limit(data['Oxygen'], 90, 100, ceil = 'Y')
data['Stress'] = sd.set_limit(data['Stress'], 1, 99, ceil = 'Y')
data['ActivityTime'] = sd.set_limit(data['ActivityTime'], 1, 120, ceil = 'Y')
data['BodyTemperature'] = sd.set_limit(data['BodyTemperature'], 33.3, 37.0, ceil = 'N')
data['BodyTemperature'] = sd.convert_unit(data['BodyTemperature'], 'Celcius to Fahrenheit')
data['Calories'] = sd.set_limit(data['Calories'], 50, 500, ceil = 'Y')
data['BloodSugarFasting'] = sd.set_limit(data['BloodSugarFasting'], 80, 150, ceil = 'Y')
data['BloodSugarAfterFood'] = sd.set_limit(data['BloodSugarAfterFood'], 150, 300, ceil = 'Y')
data['HealthIndicator'] = sd.set_limit(data['HealthIndicator'], 50, 100, ceil = 'Y')

import pandas as pd
df = pd.DataFrame(data)

print(df.head())

