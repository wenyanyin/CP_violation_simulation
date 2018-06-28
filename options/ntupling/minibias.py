from Configurables import DaVinci, FilterDesktop, DecayTreeTuple
from PhysSelPython.Wrappers import Selection, SelectionSequence, TupleSelection
import StandardParticles

alg = FilterDesktop('pions')
alg.Code = 'ALL'
sel = Selection('pions_sel',
                Algorithm = alg,
                RequiredSelections = [StandardParticles.StdAllNoPIDsPions])

tuplesel = TupleSelection('pions_tuple_sel',
                          Decay = '[pi+]cc',
                          RequiredSelection = sel)

selseq = SelectionSequence('pions_seq',
                           TopSelection = tuplesel)
DaVinci().UserAlgorithms.append(selseq.sequence())
DaVinci().TupleFile = 'DVTuples.root'
