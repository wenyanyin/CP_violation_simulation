'''Formulae for variables from the TTrees. The variable dicts are in the format
needed by makeroodataset.make_roodataset, for converting TTrees to RooDataSets.'''

variables = {'Dst_mass_DTF_vtx' : {'formula' : 'lab0_DTF_vtx_M[0]',
                                   'xmin' : 2000,
                                   'xmax' : 2200,
                                   'title' : 'D* mass', 
                                   'unit' : 'MeV',
                                   },
             'D0_mass_DTF_vtx' : {'formula' : 'lab0_DTF_vtx_D0_M[0]',
                                  'xmin' : 1700,
                                  'xmax' : 2010,
                                  'title' : 'D^{0} mass',
                                  'unit' : 'MeV',
                                  },
             'Dst_mass_DTF' : {'formula' : 'lab0_DTF_M',
                               'xmin' : 2000,
                               'xmax' : 2200,
                               'title' : 'D* mass', 
                               'unit' : 'MeV',
                               },
             'D0_mass_DTF' : {'formula' : 'lab0_DTF_D0_M',
                              'xmin' : 1700,
                              'xmax' : 2010,
                              'title' : 'D^{0} mass',
                              'unit' : 'MeV',
                              },
             'Dst_mass' : {'formula' : 'lab0_M',
                           'xmin' : 2000,
                           'xmax' : 2200,
                           'title' : 'D* mass', 
                           'unit' : 'MeV',
                           },
             'D0_mass' : {'formula' : 'lab1_M',
                          'xmin' : 1700,
                          'xmax' : 2010,
                          'title' : 'D^{0} mass',
                          'unit' : 'MeV',
                          },
             }

variables['deltam_DTF_vtx'] = {'formula' : variables['Dst_mass_DTF_vtx']['formula'] + ' - ' + variables['D0_mass_DTF_vtx']['formula'],
                               'xmin' : 140,
                               'xmax' : 170,
                               'title' : '#Deltam',
                               'unit' : 'MeV'}
variables['deltam_DTF'] = {'formula' : variables['Dst_mass_DTF']['formula'] + ' - ' + variables['D0_mass_DTF']['formula'],
                           'xmin' : 140,
                           'xmax' : 170,
                           'title' : '#Deltam',
                           'unit' : 'MeV'}
variables['deltam_no_DTF'] = {'formula' : variables['Dst_mass']['formula'] + ' - ' + variables['D0_mass']['formula'],
                              'xmin' : 140,
                              'xmax' : 170,
                              'title' : '#Deltam',
                              'unit' : 'MeV'}
variables['deltam'] = variables['deltam_DTF_vtx']
