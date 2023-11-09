class SyntheticDataGenerator:
    def __init__(self):
        np = __import__('numpy')
        pd = __import__('pandas')
        rd = __import__('random')
        cp = __import__('copy')
        warnings = __import__('warnings')

        warnings.filterwarnings('ignore')
        pd.options.display.float_format = "{:,.2f}".format
        float_format = "{:.2f}".format
        np.set_printoptions(formatter={'float_kind':float_format})
        np.random.seed(1234)
    
    def generate_timeseries(self, start_date, end_date = None, num_steps = None, frequency = None):
        '''
        Generates the time series date or time column based on the parameter inputs.
        start_date: start date of time series
        end_date: end date of time series
        num_steps: number of steps of time series
        frequency: Date or Time along with frequency of the value. Eg: D or H
        '''
        pd = __import__('pandas')
        if start_date is None:
            print('provide start_date')
        if end_date is None and num_steps is None:
            print('provide end_date or num_steps')
        if frequency is None:
            frequency = 'D'
        else:
            frequency = frequency
        if (end_date is not None) and (num_steps is None):
            time_series = pd.date_range(start=start_date, end = end_date, freq=frequency)
        if (end_date is None) and (num_steps is not None):
            time_series = pd.date_range(start=start_date, periods=num_steps, freq=frequency)
        data = {'Date': time_series}
        return data
  
    def set_limit(self, x, limit_min, limit_max, ceil = 'N'):
        '''
        Set the limit for a column by providing minimum and maximum values
        limit_min: Minimum limit for a column
        limit_max: Maximum limit for a column
        ceil: Set 'Y' to ceil the data and 'N' to 
        '''
        np = __import__('numpy')
        if ceil == 'Y':
            result = np.ceil(np.interp(x, (x.min(), x.max()), (limit_min, limit_max)))
        else:
            result = np.interp(x, (x.min(), x.max()), (limit_min, limit_max))
        return result
    
    def convert_unit(self, x, unit):
        '''
        convert data from one unit to another.
        valid inputs are:
        inches to cm
        cm to inches
        cm to m
        mm to m
        m to cm
        m to mm
        pounds to kg
        kg to pounds
        Celcius to Fahrenheit
        Fahrenheit to Celcius
        Gallons to Liters
        Liters to Gallons
        Seconds to Minutes
        Minutes to Seconds
        Minutes to Hours
        Hours to Minutes
        mps to kph
        kph to mps
        sqft to sqm
        sqm to sqft
        joules to calories
        calories to joules
        acres to square meters
        square meters to acres
        square kilometers to square miles
        square miles to square kilometers
        cubic feet to cubic meters
        cubic meters to cubic feet
        cubic inches to liters
        cubic liters to inches
        '''
        if unit == 'inches to cm':
            return x * 2.54
        elif unit == 'cm to inches':
            return x / 2.54
        elif unit == 'cm to m':
            return x / 100
        elif unit == 'mm to m':
            return x / 1000
        elif unit == 'm to cm':
            return x * 100
        elif unit == 'm to mm':   
            return x * 1000
        elif unit == 'pounds to kg':
            return x / 2.205
        elif unit == 'kg to pounds':
            return x * 2.205
        elif unit == 'Celcius to Fahrenheit':
            return (x * 9/5) + 32
        elif unit == 'Fahrenheit to Celcius':
            return (x - 32) * 5/9
        elif unit == 'Gallons to Liters':
            return x * 3.785
        elif unit == 'Liters to Gallons':
            return x / 3.785
        elif unit == 'Seconds to Minutes':
            return x / 60
        elif unit == 'Minutes to Seconds':
            return x * 60
        elif unit == 'Minutes to Hours':
            return x / 60
        elif unit == 'Hours to Minutes':
            return x * 60
        elif unit == 'mps to kph':
            return x * 3.6
        elif unit == 'kph to mps':
            return x / 3.6
        elif unit == 'sqft to sqm':
            return x / 10.764
        elif unit == 'sqm to sqft':
            return x * 10.764
        elif unit == 'joules to calories':
            return x / 4184
        elif unit == 'calories to joules':
            return x * 4184
        elif unit == 'acres to square meters':
            return x * 4047
        elif unit == 'square meters to acres':
            return x / 4047
        elif unit == 'square kilometers to square miles':
            return x / 2.59
        elif unit == 'square miles to square kilometers':
            return x * 2.59
        elif unit == 'cubic feet to cubic meters':
            return x / 35.315
        elif unit == 'cubic meters to cubic feet':
            return x * 35.315
        elif unit == 'cubic inches to liters':
            return x / 61.024
        elif unit == 'cubic liters to inches':
            return x * 61.024
        
    def generate_data(self, data, num_features, name_features):
        '''
        Generate independent variables.
        data: Input data frame
        num_features: Number of features
        name_features: Name of features
        '''
        np = __import__('numpy')
        rd = __import__('random')
        
        func = ['np.sin', 'np.cos', 'np.tan', 'np.sinh', 'np.cosh', 'np.tanh']
        num_steps = len(data['Date'])
        for i, j in zip(range(1, num_features + 1), name_features):
            data[j] = np.random.rand(num_steps) + i * 0.5 * eval(rd.choice(list(func)))(np.linspace(0, 4 * np.pi, num_steps))
        return data,num_steps
    
    def generate_target(self, data, target_name = 'Y'):
        '''
        Generate the target variable.
        data: Input data frame
        '''
        np = __import__('numpy')
        cp = __import__('copy')
        rd = __import__('random')
        
        num_steps = len(data['Date'])
        data_copy = cp.deepcopy(data)
        del data_copy['Date']
        data[target_name] = np.abs((
        np.random.rand(1)[0] * rd.choice(list(data_copy.items()))[1] - np.random.rand(1)[0] * rd.choice(list(data_copy.items()))[1] + np.random.rand(1)[0] * rd.choice(list(data_copy.items()))[1] +
        np.random.rand(1)[0] * rd.choice(list(data_copy.items()))[1] - np.random.rand(1)[0] * rd.choice(list(data_copy.items()))[1] + np.random.rand(1)[0] * rd.choice(list(data_copy.items()))[1] +
        np.random.normal(0, 1, num_steps)))
        return data
    
    def generate_text_variable(self, data, variable, values):
        '''
        Generate text variable and append to data frame column.
        data: Input data frame
        variable: Input variable name
        values: The categorical text features needed in the input. Eg: ['male', 'female']
        '''
        np = __import__('numpy')
        data[variable] = np.random.choice(list(values), len(data['Date']))
        return data[variable]      

