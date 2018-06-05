from Configurables import EventNodeKiller
eventNodeKiller = EventNodeKiller('Stripkiller')
eventNodeKiller.Nodes = [ '/Event/AllStreams', '/Event/Strip' ]
DaVinci().appendToMainSequence( [ eventNodeKiller ] )   # Kill old stripping banks first
