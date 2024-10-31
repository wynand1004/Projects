# Romania Map
class node:
	def __init__(self, name, distance_to_bucharest):
		self.name = name
		self.distance_to_bucharest = distance_to_bucharest
		self.edges = None
		self.weights = {}
		self.parent = None

arad = node("Arad", 366)
bucharest = node("Bucharest", 0)
craiova = node("Craiova", 160)
dobreta = node("Dobreta", 242)
eforie = node("Eforie", 161)
fagaras = node("Fagaras", 178)
giurgiu = node("Giurgiu", 77)
hirsova = node("Hirsova", 151)
iasi = node("Iasi", 226)
lugoj = node("Lugoj", 244)
mehadia = node("Mehadia", 241)
neamt = node("Neamt", 234)
oradea = node("Oradea", 380)
pitesti = node("Pitesti", 98)
rimnicu_vilcea = node("Rimnicu", 193)
sibiu = node("Sibiu", 253)
timisoara = node("Timisoara", 329)
urziceni = node("Urziceni", 80)
vaslui = node("Vaslui", 199)
zerind = node("Zerind", 374)

arad.edges = [sibiu, timisoara, zerind]
arad.weights[sibiu] = 140
arad.weights[timisoara] = 118
arad.weights[zerind] = 75

bucharest.edges = [fagaras, giurgiu, pitesti, urziceni]
bucharest.weights[fagaras] = 211
bucharest.weights[giurgiu] = 90
bucharest.weights[pitesti] = 101
bucharest.weights[urziceni] = 85

craiova.edges = [dobreta, pitesti, rimnicu_vilcea]
craiova.weights[dobreta] = 120
craiova.weights[pitesti] = 138
craiova.weights[rimnicu_vilcea] = 146 

dobreta.edges = [craiova, mehadia]
dobreta.weights[craiova] = 120
dobreta.weights[mehadia] = 75

eforie.edges = [hirsova]
eforie.weights[hirsova] = 86

fagaras.edges = [bucharest, sibiu]
fagaras.weights[bucharest] = 211
fagaras.weights[sibiu] = 99

giurgiu.edges = [bucharest]
giurgiu.weights[bucharest] = 90 

hirsova.edges = [eforie, urziceni]
hirsova.weights[eforie] = 86
hirsova.weights[urziceni] =  98

iasi.edges = [neamt, vaslui]
iasi.weights[neamt] = 87 
iasi.weights[vaslui] = 92

lugoj.edges = [mehadia, timisoara]
lugoj.weights[mehadia] = 70
lugoj.weights[timisoara] = 111

mehadia.edges = [dobreta, lugoj]
mehadia.weights[dobreta] = 75
mehadia.weights[lugoj] = 70

neamt.edges = [iasi]
neamt.weights[iasi] = 87

oradea.edges = [sibiu, zerind]
oradea.weights[sibiu] = 151
oradea.weights[zerind] = 71

pitesti.edges = [bucharest, craiova, rimnicu_vilcea]
pitesti.weights[bucharest] = 101
pitesti.weights[craiova] = 138
pitesti.weights[rimnicu_vilcea] = 97 

rimnicu_vilcea.edges = [craiova, pitesti, sibiu]
rimnicu_vilcea.weights[craiova] = 146
rimnicu_vilcea.weights[pitesti] = 97
rimnicu_vilcea.weights[sibiu] = 80

sibiu.edges = [arad, fagaras, oradea, rimnicu_vilcea]
sibiu.weights[arad] = 140
sibiu.weights[fagaras] = 99
sibiu.weights[oradea] = 151
sibiu.weights[rimnicu_vilcea] = 80

timisoara.edges = [arad, lugoj]
timisoara.weights[arad] = 118
timisoara.weights[lugoj] = 111

urziceni.edges = [bucharest, hirsova, vaslui]
urziceni.weights[bucharest] = 85
urziceni.weights[hirsova] = 98
urziceni.weights[vaslui] = 142

vaslui.edges = [iasi, urziceni]
vaslui.weights[iasi] = 92
vaslui.weights[urziceni] = 142 

zerind.edges = [arad, oradea]
zerind.weights[arad] = 75 
zerind.weights[oradea] = 71
