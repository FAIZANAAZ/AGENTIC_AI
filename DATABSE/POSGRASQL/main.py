# Import kar rahe hain zaroori libraries
import os
from sqlalchemy import create_engine, text
# SQLAlchemy sy craete_engine import krwa rahe hain
# create_engin sy hm database ko connet krwa ty hen 


from dotenv import load_dotenv
# ye load krwata he env ki file ko


data_list=[]#yha data base sy data lakr stor krengy

# .env file load kar rahe hain
load_dotenv()

# DATABASE_URL ko environment se read kar rahe hain
DATABASE_URL = os.getenv("DATABASE_URL_UNPOOLED")
# ye read krta he 

# SQLAlchemy engine create kar rahe hain
engine = create_engine(DATABASE_URL)


# Core logic function
def main():
    with engine.connect() as conn:
        # Table/Schema create kar rahe hain agar exist nahi karti
        conn.execute(text("""
           CREATE TABLE IF NOT EXISTS my_table(
               
              id SERIAL PRIMARY KEY,
              name VARCHAR(50) NOT NULL,
              age INT,
              email TEXT UNIQUE NOT NULL
              
           );
        """))
        conn.commit()
        # phly yha tk ka code likh kr or func call krkky main.py wala jakr dekhengy table bna ya nhi phir agy ka code krengy 
#         # hm yha text likhety hen query likhty time 

        # Optional: Sample data insert karne ke liye (commented by default)
        # conn.execute(text("""
        #     INSERT INTO my_table (name,age, email)
        #     VALUES ('faiza',4,'taha@example.com'),
        #            ('Ahmed',5,'ahmed@example.com');
        # """))
        # conn.commit()

#         # Data fetch kar rahe hain neon database sy
        result = conn.execute(text("SELECT * FROM my_table;")).mappings()
        
        print("Users in database:")#ye bs ak heading he 
        for row in result:
            # users to ak nhi he zada hen data to zada he isi liye hm isko loop me rakhengy 
            data_list.append(dict(row))
            
        print(data_list,"😎 done boos")  # Row ko dictionary mein convert karke print kar rahe hain taky terminal medekh sky 

# # Script ko run karne ke liye
if __name__ == "__main__":
    main()