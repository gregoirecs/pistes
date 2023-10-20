"""The ETL module.

Look at the instructions after the statement if __name__ == "__main__":

* First, we extract the data from the input CSV files into a collection of Pandas dataframes.
  Each dataframe corresponds to a table in the target relational database.
* Then, we transform the data in the dataframes.
* Finally, we load the data into the database.

"""

import pandas as pd
import sqlite3
import os
import db
import utils

from datetime import datetime

def get_right_date(input_date):
    if pd.isnull(input_date):
        return None 
    try:
        input_date = datetime.strptime(input_date, "%Y-%m-%d")
    except ValueError:
        return None
    return input_date.strftime("%d/%m/%Y")

def extract():
    """Implementation of the extraction submodule.

    Returns
    -------
    dictionary
        The collection of dataframes containing the data of the input CSV files.
        You should have as many dataframes as tables in your relational database.
        Each dataframe corresponds to a table in the relational database.
        The dictionary contains a set of key-value pairs where
            * the value is a dataframe. 
            * the key is the name of the table corresponding to the dataframe  (e.g., "Student", "EmailAddress"...)
            
    """

    # This is the dictonary containing the collection of dataframes.
    # Each item of this dictionary is a key-value pair; the key is the name of a database table;
    # the value is a Pandas dataframe with the content of the table.
    dataframes = {}
    input1=pd.read_csv("./data/student_registrations.csv", delimiter=';')
    input2=pd.read_csv("./data/student_memberships.csv", delimiter=';')
    student_df=input1[["stud_number","first_name","last_name","gender"]]
    student_df = pd.concat([student_df, input2[["stud_number","first_name","last_name","gender"]]], ignore_index=True)
    email_df=input1[["email","stud_number"]]
    email_df = pd.concat([email_df, input2[["email","stud_number"]]], ignore_index=True)
    pistus_df=input1[["year","registration_fee"]]
    register_df=input1[["registration_date","payment_date","stud_number","year"]]
    member_df=input2[["stud_role","asso_name","stud_number"]]
    asso_df=input2[["asso_name","asso_desc"]]
   # print("Extracting the data from the input CSV files..."

    ################## TODO: COMPLETE THE CODE OF THIS FUNCTION  #####################
    dataframes={"Student":student_df,"EmailAddress":email_df,"PistusEdition":pistus_df,"Register_for":register_df,"Member_of":member_df,"Association":asso_df}
    
    ##################################################################################

    # Return the dataframe collection.
    return dataframes
    
#dataframes=extract()

def transform(dataframes):
    """Implementation of the transformation submodule.

    Parameters
    ----------
    dataframes : dictionary
        This is the dictionary returned by the function load()
    
    Returns 
    -------
    The input dictionary (after the transformations).
    """

    ################## TODO: COMPLETE THE CODE OF THIS FUNCTION  #####################
    dataframes["Student"]=dataframes["Student"].drop_duplicates()
    dataframes["EmailAddress"]=dataframes["EmailAddress"].drop_duplicates()
    dataframes["Association"]=dataframes["Association"].drop_duplicates()
    dataframes["PistusEdition"]=dataframes["PistusEdition"].drop_duplicates()
    
    find_replace={"M":"M","H":"M","garçon":"M","F":"F","W":"F","fille":"F"}
    columns_to_replace = {"gender": find_replace}
    dataframes["Student"]=dataframes["Student"].replace(columns_to_replace)
    
    dataframes["Register_for"]["registration_date"] = dataframes["Register_for"]["registration_date"].map(get_right_date)
    dataframes["Register_for"]["payment_date"] = dataframes["Register_for"]["payment_date"].map(get_right_date)
    ##################################################################################

    # Returns the dataframe collection after the transformations.
    return dataframes

def load(dataframes):
    """Implementation of the load submodule.

    Parameters:
    ----------
    dataframes : dictionary
        The dictionary returned by the function extract()
    """
    # Loads the application configuration.
    app_config = utils.load_config()

    # Gets the path to the database file.
    database_file = app_config["db"]

    # You might bump into some errors while debugging your code which 
    # This might result in a database that is partially filled with some data.
    # Each time you rerun the ETL module, you want the database to be in the same state as when
    # you first created. 
    # The simpler solution here is to remove the database and recreate the tables back again.
    if os.path.exists(database_file):
        # If the database file already exists, we remove it.
        # In order to test the existence of a file, and to remove it, we use functions that are 
        # available in a Python module called "os".
        os.remove(database_file)
    
    # We open a connection to the database.
    try:
        conn = sqlite3.connect(database_file)

    # We get the cursor to query the database.
        cursor = conn.cursor()

    # We create the tables in the database, by using the function create_database that you implemented in the module
    # db.
        db.create_database(conn, cursor)

        print("Loading the data into the database...")
    
    ################## TODO: COMPLETE THE CODE OF THIS FUNCTION  #####################
        dataframes["Student"].to_sql("student", conn, if_exists="append", index=False)
        dataframes["EmailAddress"].to_sql("Email", conn, if_exists="append", index=False)
        dataframes["Association"].to_sql("Association", conn, if_exists="append", index=False)
        dataframes["PistusEdition"].to_sql("PistusEdition", conn, if_exists="append", index=False)
        dataframes["Register_for"].to_sql("register_for", conn, if_exists="append", index=False)
        dataframes["Member_of"].to_sql("member_of", conn, if_exists="append", index=False)
        
    ##################################################################################
        conn.commit()
        cursor.close()
        conn.close()
        return "Done!"
    except Exception as e:
        return "An error occurred while loading data into the Pistus database:"+str(e)

dataframes = extract()
# Entry point of the ETL module.
if __name__ == "__main__":
    load(transform(dataframes))
##print(dataframes["PistusEdition"])
   
    