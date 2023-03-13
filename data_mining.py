# the data will read from csv files
import csv

class dataset():
    def __init__(self,file_path):
        self.data=[]
        
        file = open(file_path,'r')
        self.headers=file.readline().strip().split(',')
        for i in file:
            self.data.append(i.strip().split(','))

    def dictionary_encoding(self,header_name,encoder):
        location=self.headers.index(header_name)
        for i in self.data:
            i[location]=encoder[i[location]]
        
    def function_encoding(self,header_name,fn):
        location=self.headers.index(header_name)
        for i in self.data:
            i[location]= fn(i[location])

    




        
