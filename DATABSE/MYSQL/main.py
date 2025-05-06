from sqlalchemy import create_engine, text

# MySQL Connection Details
USER = 'root'     # Username hmny set nhi kiya tha isiliy wo root likhengy 
PASSWORD = 'faiza13579'       # Password
HOST = 'localhost'          # Local Server
DB_NAME = 'school'          # Target Database




# Establish SQLAlchemy Engine
engine = create_engine(f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")
# ye hmny name ko sahi sy add krwaty hen system me yhahm wesy direct bhi data base name likh skty hen ya phir hm variable me rakhlety hen

# Table Creation
with engine.connect() as connection:
    # yha hmny connct krwaya he   database 
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(25) NOT NULL,
            age INT
        );"""))
        # is trha hm query likhty hen 
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
        
# Insert a Sample Record
with engine.connect() as connection:
    connection.execute(text("""
        INSERT INTO students (name, age)
        VALUES ('Zeeshan', 30),
        ('Ali', 25),
        ('Hamza', 20);
    """))
    connection.commit()  # 🧠 Don't forget to commit the transaction
    
    # update
    # Update student record (example: change 'Ali' age to 28)
with engine.connect() as connection:
    connection.execute(text("""
        UPDATE students
        SET age = 28
        WHERE name = 'Ali';
    """))
    connection.commit()

    # delete
    # Delete student record (example: delete 'Hamza')
with engine.connect() as connection:
    connection.execute(text("""
        DELETE FROM students
        WHERE name = 'Hamza';
    """))
    connection.commit()

     