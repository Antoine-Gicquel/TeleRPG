class Entity(object):
    def __init__(self):
        pass
    
    def runScenario(self):
        pass
    
    def createEntity(entityname):
        # TODO refactor
        if entityname == "YvesPoilane":
            return YvesPoilane()
        elif entityname == "MyriamDavidovici":
            return MyriamDavidovici()
        elif entityname == "RenaudGamet":
            return RenaudGabet()
        
        return None

exec(open("lib/entities/YvesPoilane.py").read())
exec(open("lib/entities/MyriamDavidovici.py").read())
exec(open("lib/entities/RenaudGabet.py").read())