import psycopg2
import plant.settings as Settings


def LoadDataInDjango(
    ProjectNamePath = "plant/",
    FilePath = "SQLScripts/",
    FileName = "InitialData",
    DBNameInSettings = "default"):
    """
        Loads initial data from SQL file in django tables
    """

    print("Loading initial data in database...")

    # get DB data from settings
    print(Settings.DATABASES)
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
        print(f"Connection opened to '{DBData['NAME']}' database")
    
    except(Exception, psycopg2.DatabaseError) as Error:
        # error
        print(f"ERROR: Cannot connect to '{DBData['NAME']}' database, error detail:\n{Error}")
        return
   
    # get script from file
    SQLScript = ""
    try:
        with open(ProjectNamePath + FilePath + FileName + ".sql", "r", encoding = "utf-8") as MyFile:
            SQLScript = "".join(MyFile.readlines())
        
        print(f"Script retrieved from '{ProjectNamePath + FilePath + FileName + '.sql'}' file")
    
    except FileNotFoundError as Error:
        # error
        print(f"ERROR: accessing '{ProjectNamePath + FilePath + FileName + '.sql'}' file, error detail:\n{Error}")
        return
    
    # execute script instructions
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

                print(f"Executing\n{SQLInstruction}\nOK")

            except(Exception, psycopg2.DatabaseError) as Error:
                # error
                print(f"ERROR: executing\n{SQLInstruction}\nError detail:\n{Error}")
                return

            finally:
                # close resources
                if MyCursor is not None:
                    MyCursor.close()

    # close resources
    if MyConnection is not None:
        MyConnection.close()

    print("Initial data successfully loaded in database.")


if __name__ == "__main__":
    LoadDataInDjango()
