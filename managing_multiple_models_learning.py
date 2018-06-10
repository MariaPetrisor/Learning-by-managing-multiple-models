#!/usr/bin/python2.7

'''
    File name: managing_multiple_models_learning.py 
    Author: Maria Petrisor
    Date created: 28/05/2018
    Python Version: 2.7
'''


class Characteristics:
    def __init__(self, characteristics_list, reaction):
        self.characteristics_list = characteristics_list
        self.reaction = reaction

    def get_characteristics_list(self):
        return self.characteristics_list

    def get_reaction(self):
        return self.reaction


class Model:
    def __init__(self):
        self.general_model = []
        self.specific_model = []

    def get_general_model(self):
        return self.general_model

    def get_specific_model(self):
        return self.specific_model  

    def generalization(self, characteristics_list):
        if self.general_model == []:
            for entry in characteristics_list:
                self.general_model.append("?")
        else:
            new_specific_model = []
            for idx, entry in enumerate(characteristics_list):
                if entry == self.specific_model[idx]:
                    new_specific_model.append(entry)
                else:
                    new_specific_model.append("?")
            if new_specific_model:
                self.specific_model = new_specific_model

    def specialization(self, characteristics_list):
        if self.specific_model == []:
            for entry in characteristics_list:
                self.specific_model.append(entry)
        else:
            new_general_model = []
            for idx, entry in enumerate(characteristics_list):
                if entry != self.specific_model[idx] and self.specific_model[idx] != "?":
                    new_specialization = []
                    
                    for i in self.general_model:
                        if type(i) != list:
                            new_specialization.append(i)
                        else:
                            for ii in self.general_model[0]:
                                new_specialization.append(ii)
                            break
                    
                    new_specialization[idx] = self.specific_model[idx]
                    new_general_model.append(new_specialization)

            if new_general_model:
                if len(new_general_model) == 1:
                    flat_list = [item for sublist in new_general_model for item in sublist]
                    self.general_model = flat_list
                else:
                    self.general_model = new_general_model

    def modify_version_space(self, characteristic):
        
        if self.general_model == [] and self.specific_model == []:
            self.generalization(characteristic.get_characteristics_list())
            self.specialization(characteristic.get_characteristics_list())
        else:
            if characteristic.get_reaction() is True:
                self.generalization(characteristic.get_characteristics_list())
            else:
                self.specialization(characteristic.get_characteristics_list())

        if self.general_model == self.specific_model and self.general_model != [] and self.specific_model != []:
            print "The general model and the specific model have converged. The obtained model: "
            print self.general_model

if __name__ == "__main__":

    ch1 = Characteristics(["Sam's", "breakfast", "Friday", "cheap"], True)
    ch2 = Characteristics(["Lobdell", "lunch", "Friday", "expensive"], False)
    ch3 = Characteristics(["Sam's", "lunch", "Saturday", "cheap"], True)
    ch4 = Characteristics(["Sarah's", "breakfast", "Sunday", "cheap"], False)
    ch5 = Characteristics(["Sam's", "breakfast", "Sunday", "expensive"], False)

    model = Model()

    print "Iteration 1"
    print ch1.get_characteristics_list()
    model.modify_version_space(ch1)
    print "General model: "
    print model.get_general_model()
    print "Specific model: "
    print model.get_specific_model()
    print ""

    print "Iteration 2"
    print ch1.get_characteristics_list()
    model.modify_version_space(ch2)
    print "General model: "
    print model.get_general_model()
    print "Specific model: "
    print model.get_specific_model()
    print ""

    print "Iteration 3"
    print ch1.get_characteristics_list()
    model.modify_version_space(ch3)
    print "General model: "
    print model.get_general_model()
    print "Specific model: "
    print model.get_specific_model()
    print ""

    print "Iteration 4"
    print ch1.get_characteristics_list()
    model.modify_version_space(ch4)
    print "General model: "
    print model.get_general_model()
    print "Specific model: "
    print model.get_specific_model()
    print ""

    print "Iteration 5"
    print ch1.get_characteristics_list()
    model.modify_version_space(ch5)
    print "General model: "
    print model.get_general_model()
    print "Specific model: "
    print model.get_specific_model()
    print ""
