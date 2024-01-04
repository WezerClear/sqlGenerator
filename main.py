class Generators:
    def __init__(self, request=""):
        self.__request = request

    def displayRequest(self):
        print(self.__request)

    def readDataTypes(self, infos):
        liste = []
        choice = -1
        with open("datatype.txt", "r") as fichier:
            save = False
            for line in fichier:
                if save:
                    liste.append(line)
                for car in line:
                    if car == infos:
                        save = not save
        fichier.close()
        liste.pop()
        for count, data_type in enumerate(liste):
            print(f"{count} : {data_type}")
        while choice < 0 or choice > len(liste):
            choice = int(input("Choose a type: "))
        return liste[choice]

    def CREATE(self, addColumn=True):
        self.__request += "CREATE "
        tableName = input("Enter the table name: ")
        # vérifier que la table existe
        self.__request += tableName
        self.__request += "\n ( \n"
        while addColumn:
            columnName = input("Column name: ")
            self.__request += columnName
            typeChoice = "aze"
            while typeChoice not in ("1", "0", "2"):
                typeChoice = input(" 0 : string\n 1 : number\n 2 : Date\n")
            choice = self.readDataTypes(typeChoice)
            if False:
                pass
            else:
                addColumn = False
        self.__request += "\n );"
        self.displayRequest()
        return

    def SELECT(self):
        print("select is launch")
        return

    def INSERT(self):
        print("insert is launch")
        return

    def UPDATE(self):
        print("update is launch")
        return

    def menu(self, choice="A", var=-1):  # first menu
        while choice not in ("1", "0"):
            choice = input(
                "SQL GENERATOR\n 0: request on Table, \n 1: Table management \n"
            )

        if int(choice):
            listTable = [self.CREATE]
            while var < 0 or var > len(listTable):
                var = int(
                    input(
                        "TABLE MANAGEMENT\n 0: CREATE Table,\n 1: DELETE lign/column,\n 2: DESTROY Table,\n 3: ALTER Table,\n 4: back \n"
                    )
                )
            listTable[var]()

        else:
            listRequest = [self.SELECT, self.INSERT, self.UPDATE, self.menu]
            while var < 0 or var > len(listRequest):
                var = int(
                    input(
                        "REQUEST ON TABLE\n 0: SELECT lign/column,\n 1: INSERT lign/column,\n 2: UPDATE lign/column,\n 3: back \n"
                    )
                )
            listRequest[var]()


myGenerator = Generators()
myGenerator.menu()
