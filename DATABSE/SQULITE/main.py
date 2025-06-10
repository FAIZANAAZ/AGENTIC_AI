from sqlalchemy import create_engine, text


# Database file name
DB_FILE = "my_squlite.db"
# ye hm name de rhy hen data base ka ye bn kr bhi ayga ak file ki trha  lekin jb tb hm file ko run kreengy wahi main.py ko data  base connect kry ke bad  query likhny k bad

# Create an SQLite engine connected to the real database
engine = create_engine(f"sqlite:///{DB_FILE}")
# ab hm connect krwa rhy hen data base ke sath

# Create the database and table using raw SQL
with engine.connect() as connection:
    # hmny connect krwaay or auto krdiya with ke sath
    # with ke sath isi liye likhty hen wo khod hi open krta he or khod hi close krta he
    connection.execute(text(
        # execute matlb wo apny ander query likhny deta he 
        
        #row sql 
        """
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(25) NOT NULL,
            age INTEGER
        );
        """
        # isky ander hm jo likhry hen osko wo smajhta he jesy 
        # yha likha he ke ( CREATE TABLE IF NOT EXISTS students) yani agr students table nhi he to create krdo
        # id integer yani id jo hogi wo aygi sbsy phly column me jismy id integer hogi 
        # (primary key) ka matlb he ke key uniq hogi or khali nahi hogi 
        # (auto increment) ka matlb he ke outomate increase hoty jao 
        # (name varchar(25) not null) yani name jo hoga wo 25 character ka hoga OSY ZADA NHI HONA CHIYE or wo khali nahi ho sakta
        # (age integer) yani age jo hogi wo integer hogi
        # , lga laga kr hm seprate krengy 
        # ; lagana lazmi he wrna wo chlayga hi nhi isi sy wo and hoga
        # variable ka name lowercase me hen or jo chizn hmy squilite ki traf sy milti hen wo uppercase me hen
        
    ))
    
    # create add *************************
    # with engine.connect() as connection:
    #     connection.execute(text(
    #         """
    #         INSERT INTO students
    #         (name, age)
    #         VALUES
    #         ('Taha', 20),
    #         ('Ali', 22),
    #         ('Sara', 19);
            
    #         """
    #         # is trha hm jitny chahy otna insert kr skty hen 
    #     ))
    #     connection.commit()
    
    # isko commint rkha he wrna wo bar bar add krta jayga
    
    
    # hm inser krwa rhy hen data base me data ko student ke table me jo oper bnaya he name wahi ayga bhly change ho jay 
    # phir variable name phir kha VALUES phir oski value dedi hmny osky ander id hm nhi dengy kioky osko hmny autoincreament pr lagay howa he id wo khod generate krlega 
    
    # run uv run main.py file 
    # run .\sqlite3.exe my_squlite.db (wo name jo hmne diya tha DATA BASE KA ) 
    # run .tables
    # run SELECT * FROM students; (studet yani wo name jo hmny table ka diya tha name ; lgana lazmi he ) 
    #  .headers on
    # run .mode box 
    # in dono sy wo ak table ki chakal lelega box jesy 
    # run .exit (ye exit ho jaye ga yani database sy bahir a jaygy )
    
    # agr hm semi colomn nhi lgaty ya koi ghalti ho jay jisy terminal me koch bhi kro enter to ..> ayga to osy hm bahir nikalny ke liye (;)lga kr enter krygy
    
    
    # run SELECT * FROM students WHERE id = 1; (ye id 1 ka student ka data dikhayga he )
    
    
    # delete data ***************
    with engine.connect() as connection:
        connection.execute(text(
            """
            DELETE FROM students WHERE id = 2;
            """
        ))
        connection.commit()
        
        # YHA HMNY DELETE KRWA DIA HE STUDENT KO ID 2 KA
        # jb bhi koi changging krty hen hmy connection.commit() krna lazmi he 
    
    #UPDATE data ***************
    with engine.connect() as connection:
        connection.execute(text(
            """
            UPDATE students
            SET name = 'Alex'
            WHERE id = 3;
            """
        ))
        connection.commit()
    
#   ye hmny updatte krdiya code name id 3 ka