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

    def chooseDataParameters(self, choice):
        size = "-1"
        for index, car in enumerate(choice):
            if car == "(" and choice[index + 1] == "s":
                while size > "0" or size < "256":
                    size = input("choose a size for data (default 1, min 1, max 255)")

            elif car == "(" and choice[index + 1] == "p":
                significant = "-1"
                while significant >= "0" or significant < "24":
                    significant = input(
                        "choose the number of significant digits (default 7, min 0, max 23)"
                    )

            elif car == "(" and choice[index + 1] == "f":
                date = "-1"
                while date >= "0" or date < "7":
                    date = input(
                        "choose the fractional seconds precision (default 0, min 0, max 6)"
                    )

    def CREATE(self, addColumn=True):
        self.__request += "CREATE "
        tableName = input("Enter the table name: ")
        self.__request += tableName
        self.__request += "\n ( \n"
        while addColumn:
            columnName = input("Column name: ")
            self.__request += columnName
            typeChoice = "aze"
            while typeChoice not in ("1", "0", "2"):
                typeChoice = input(" 0 : string\n 1 : number\n 2 : Date\n")
            choice = self.readDataTypes(typeChoice)

            for letter in choice:
                if letter == "(":
                    self.chooseDataParameters(choice)

            self.__request += " " + choice
            continu = "A"
            while continu not in ("y", "Y", "n", "N"):
                continu = input("do you want to add an other column ? \ny or n\n")
            if continu in ("N", "n"):
                addColumn = False
        self.__request += "\n );"
        self.displayRequest()

    def SELECT(self):
        result = int(
            input("How many table do you want to select your Data ? min 1 max 3")
        )
        if result == 1:
            self.__request += "SELECT "
        manyColumn = int(input("How many column do you want select ? "))
        for loop in range(manyColumn):
            ColumnName = input("choose a column name")
            self.__request += ", " + ColumnName
        tableName = input("Choose from which table do you want to select your data : ")
        self.__request += tableName

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
