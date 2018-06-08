'''Formulae for variables from the TTrees. The variable dicts are in the format
needed by makeroodataset.make_roodataset, for converting TTrees to RooDataSets.'''

variables = {'Dst_mass' : {'formula' : 'lab0_DTF_vtx_M[0]',
                           'xmin' : 2000,
                           'xmax' : 2060,
                           'title' : 'D* mass', 
                           'unit' : 'MeV',
                           },
             'D0_mass' : {'formula' : 'lab0_DTF_vtx_D0_M[0]',
                          'xmin' : 1810,
                          'xmax' : 1910,
                          'title' : 'D^{0} mass',
                          'unit' : 'MeV',
                          }
             }

variables['deltam'] = {'formula' : variables['Dst_mass']['formula'] + ' - ' + variables['D0_mass']['formula'],
                       'xmin' : 140,
                       'xmax' : 170,
                       'title' : '#Deltam',
                       'unit' : 'MeV'}
