# coding: utf-8

# Add initial data in a PostgreSQL database in a Django project

import psycopg2
import plant.settings as Settings


def LoadDataInDjango(
    ProjectNamePath = "",
    FilePath = "SQLScripts/",
    FileName = "InitialData",
    DBNameInSettings = "default"):
    """
        Loads initial data from SQL file in django tables
    """

    print("\nLoading initial data in database.")
    print("Note that all existing data will be deleted from concerned tables.")

    # get DB data from settings
    for SetName, SetValue in Settings.DATABASES.items():
        print(f"\nDatabase settings name : {SetName}")
        for Name, Value in SetValue.items():
            print(f"    {Name} : {Value}")
    DBData = Settings.DATABASES[DBNameInSettings]

    # connect to DB
    MyConnection = None
    try:
        MyConnection = psycopg2.connect(
            host=DBData["HOST"] if DBData["HOST"].strip() != "" else "localhost",
            port=DBData["PORT"] if str(DBData["PORT"]).strip() != "" else "5432",
            database=DBData["NAME"],
            user=DBData["USER"],
            password=DBData["PASSWORD"])
        print(f"\nConnection opened to '{DBData['NAME']}' database")
    
    except(Exception, psycopg2.DatabaseError) as Error:
        # error
        print(f"\nERROR: Cannot connect to '{DBData['NAME']}' database, error detail:\n{Error}\n")
        return
   
    # get script from file
    SQLScript = ""
    try:
        with open(ProjectNamePath + FilePath + FileName + ".sql", "r", encoding = "utf-8") as MyFile:
            SQLScript = "".join(MyFile.readlines())
        
        print(f"\nScript retrieved from '{ProjectNamePath + FilePath + FileName + '.sql'}' file")
    
    except FileNotFoundError as Error:
        # error
        print(f"\nERROR: accessing '{ProjectNamePath + FilePath + FileName + '.sql'}' file, error detail:\n{Error}\n")
        return

    # get table names from SQL script
    TableNames = []
    for SQLInstruction in SQLScript.split(";"):
        if SQLInstruction.strip().strip("\n").upper().startswith("INSERT INTO"):
            TableName = SQLInstruction.strip().strip("\n").replace("INSERT INTO ", "").split(" ")[0]
            TableNames.append(TableName)

    # delete existing data 
    print(f"\nDeleting existing data...")
    # reverse table names order so that integrity constraints will be respected while deleting
    TableNames.reverse()
    for TableName in TableNames:
        MyCursor = None
        SQLInstruction = f"DELETE FROM {TableName};"
        try:
            # create cursor to browse db objects
            MyCursor = MyConnection.cursor()
            # execute query
            MyCursor.execute(SQLInstruction)
            # commit to DB
            MyConnection.commit()

            print(f"Executing\n{SQLInstruction}\nOK")

        except(Exception, psycopg2.DatabaseError) as Error:
            # error
            print(f"\nERROR: executing\n{SQLInstruction}\nError detail:\n{Error}\n")
            return

        finally:
            # close resources
            if MyCursor is not None:
                MyCursor.close()
    # put back table names in script order
    TableNames.reverse()
    
    # execute script instructions
    print(f"\nAdding initial data...")
    TableNameIndex = 0
    for SQLInstruction in SQLScript.split(";"):
        SQLInstruction = SQLInstruction.strip("\n")

        if SQLInstruction:
            MyCursor = None
            try:
                # create cursor to browse db objects
                MyCursor = MyConnection.cursor()
                # execute query
                MyCursor.execute(SQLInstruction)
                # commit to DB
                MyConnection.commit()

                print(f"\nExecuting\n{SQLInstruction}\nOK")

                # get last inserted id for current table
                LastID = 1
                NewInstruction = f"SELECT id FROM {TableNames[TableNameIndex]} ORDER BY id DESC LIMIT 1;"
                MyCursor.execute(NewInstruction)
                LastID = MyCursor.fetchone()[0]

                # force primary key auto increment value to last value + 1 for current table
                NewInstruction = f"ALTER SEQUENCE {TableNames[TableNameIndex]}_id_seq RESTART WITH {LastID + 1} INCREMENT BY 1;"
                MyCursor.execute(NewInstruction)
                MyConnection.commit()
                print(f"Auto-increment start for table {TableNames[TableNameIndex]} set to {LastID + 1}")
                TableNameIndex += 1

            except(Exception, psycopg2.DatabaseError) as Error:
                # error
                print(f"\nERROR: executing\n{SQLInstruction}\nError detail:\n{Error}\n")
                return

            finally:
                # close resources
                if MyCursor is not None:
                    MyCursor.close()

    # close resources
    if MyConnection is not None:
        MyConnection.close()

    print("\nInitial data successfully loaded in database.\n")


if __name__ == "__main__":
    LoadDataInDjango()
