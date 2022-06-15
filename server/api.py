import time

class Api:
    def __init__(self):
        self.data = {}
    
    def contains_key(self, key):
        if key in self.data:
            return True
        return False

    def create_key_value(self, key, value):
        new_dict = {
            'latest_value': value,
            'history': [{
                'value': value,
                'timestamps': time.time()
            }]
        }
        self.data[key] = new_dict
        result = "Done"
        return result

    def update_key_value(self, key, value):
        self.data[key]['latest_value'] = value
        self.data[key]['history'].append({
            'value': value,
            'timestamps': time.time()
        })
        result = "Done"
        return result
    
    def get_value_by_key(self, key):
        result = None
        try:
            result = self.data[key]['latest_value']
        except:
            pass
        return result

    def get_history(self, key):
        result = None
        try:
            history = self.data[key]['history']
            result = history
        except:
            pass
        return result