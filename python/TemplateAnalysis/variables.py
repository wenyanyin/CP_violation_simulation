'''Formulae for variables from the TTrees. The variable dicts are in the format
needed by makeroodataset.make_roodataset, for converting TTrees to RooDataSets.'''

variables = {'mass' : {'formula' : 'Xc_M',
                       'xmin' : 2300,
                       'xmax' : 2400,
                       'title' : 'Mass', 
                       'unit' : 'MeV', # optional
                       'discrete' : False, #optional, default False.
                       },
             }
