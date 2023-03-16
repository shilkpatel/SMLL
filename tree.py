import math


class tree():
    def __init__(self,subset,X,y):
        self.subset = subset# subset of a dataset, 
        self.children=[]#array of children as non-binary tree
        self.X=X#array of indexs to show which elements are used for x
        self.y=y# int of index of y
        self.num_splits=100# can be determined in a better way



    def standard_deviation(array):#assume numerical data in array
        average=sum(array)/len(array)
        variance=0
        for i in array:
            variance+=(i-average)**2
        variance/=len(array)
        std = math.sqrt(variance)
        return std



class numtree(tree):
    def __init__(self,subset,X,y):
        super().__init__(subset,X,y)
        self.condition=None

    def building(self):
        sub_std=tree.standard_deviation([i[self.y] for i in self.subset])
        
        # for each atribute in x you calculate the reduced standard deviation and which ever is greater
        # you split the data on it but this only works when the data is categorical
        # but if you sort the data on the attribute x you then have n-1 splits to test
        # for which standard_deviation reduction works on

        # this is difficult to do efficiently so I could employ a heuristic and have n number of splits
        best_attribute=-1
        best_split=None
        max_standard_reduction = 0
        for i in self.X:# for each attribute
            range_of_set = self.max_in_attribute(i) - self.min_in_attribute(i)
            steps = range_of_set/self.num_splits
            minimum = self.min_in_attribute(i)
            for i in range(1,self.num_splits-1):# for each splitting codition
                splitting_condition =minimum+(steps*i)
                left,right=self.split_on_condition(splitting_condition,i)
                standard_reduction = sub_std - (tree.standard_deviation(left)+tree.standard_deviation(right))
                if standard_reduction>max_standard_reduction:
                    max_standard_reduction=standard_reduction
                    best_attribute=i
                    best_split=splitting_condition
                    max_standard_reduction = standard_reduction



    def split_on_condition(self,condition, index):
        left=[]
        right=[]
        for i in self.subset:
            if i[index]<condition:
                left.append(i)
            else:
                right.append(i)
        return left,right
        
    def max_in_attribute(self,index):

        max_value=0
        max_record=[]
        for i in self.subset:
            if i[index]>max_value:
                max_record=i.copy()
                max_value=i[index]
        return max_record

    def min_in_attribute(self,index):
        min_value = 100000000
        min_record = []
        for i in self.subset:
            if i[index]<min_value:
                min_value=i[index]
                min_record= i.copy()
        return min_record
        


class grouptree(tree):
    def __init__(self, subset, X, y):
        super().__init__(subset, X, y)
        self.condition = None


