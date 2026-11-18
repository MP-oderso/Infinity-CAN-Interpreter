import Datenverarbeitung.dielen as pu

class Application:
    def __init__(self, name, version,description, developers, maintainer, tags):
        self.name = name
        self.version = version
        self.description = description
        self.developers = developers
        self.maintainer = maintainer
        self.tags = tags

def status(self):
    return( f"{self.name} {self.version}: {self.description} \n"
            f"Team: {', '.join(self.developers)} \n"
            f"Maintainer: {self.maintainer} \n"
            f"Tags: {', '.join(self.tags)} \n"
    )

if __name__ == "__main__":
    umwandler = pu.ParquetUmwandlung()     #standarmäßig wird die Filterung durchgeführt, kann aber durch filterung=False deaktiviert werden
   #umwandler = pu.ParquetUmwandlung(filterung=False)  #wenn man die Filterung deaktivieren möchte, kann man dies hier tun
    umwandler.alle_mat_zu_parquet()