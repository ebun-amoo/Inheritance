
import os

class PersistedList:
    def __init__(self, filename):
        self.filename = filename
        self.internal_list = []
        
        if os.path.exists(filename):
            with open(self.filename, 'r') as f:
                file_contents = f.read()
                if file_contents:
                    self.internal_list = file_contents.split('\n')
            
    def persist(self):
        with open(self.filename, 'w') as f:
            new_file_contents = '\n'.join(self.internal_list)
            f.write(new_file_contents)
        
    def append(self, incoming_string):
        self.internal_list.append(incoming_string)
        self.persist()
        
    def insert(self, position, incoming_string):
        self.internal_list.insert(position, incoming_string)
        self.persist()
    
    def get_last_item(self):
        length = len(self.internal_list)
        return self.internal_list[length - 1]
    
    def get_item_at(self, position):
        return self.internal_list[position]
    
    def set_item_at(self, position, incoming_string):
        self.internal_list[position] = incoming_string
        self.persist()

# please add your code here
class PersistedListWithReset(PersistedList):
    def reset(self):
        self.internal_list = []

some_list = PersistedListWithReset("greeting.txt")
some_list.append('Hello')
some_list.append('Hi')

some_list.reset()
