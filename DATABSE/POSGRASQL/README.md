# PostgreSQL Integration with Neon Using `uv` and SQLAlchemy

This guide explains how to set up and interact with a **PostgreSQL database** using **Neon**, manage your Python environment with `uv`, and connect via `SQLAlchemy`. We also use `python-dotenv` to manage environment variables securely.

---

## Prerequisites

Ensure the following are installed:

- Python 3.10+
- `uv` (dependency manager)
- A free account on [https://vercel.com](https://vercel.com)

---

## Step-by-Step Setup

### 1. Login to Vercel
Login to your [Vercel](https://vercel.com) account.

> **Purpose:** Required to access the Neon integration for database creation.

### 2. Open the Storage Tab
Navigate to the **Storage** section on the top navigation bar.

> **Purpose:** Neon databases are managed under this tab.

### 3. Create a Neon Database
Click the **Neon → Create** button.

> **Purpose:** Starts the database provisioning process.

### 4. Accept Terms
Click **Accept and Create** if prompted.

> **Purpose:** Accept Neon’s terms to proceed.

### 5. Choose Region
Select your preferred region (e.g., `US-East`, `Europe`).

> **Purpose:** Region affects latency and performance.

### 6. Select Free Plan
Choose the `Free` tier.

> **Purpose:** Ideal for development and testing.

### 7. Click Continue
Click the **Continue** button.

### 8. Name Your Database
Name your database (e.g., `my_app_db`).

### 9. Finalize Creation
Click **Create**.

### 10. Confirmation
You’ll see a message: **Database Created Successfully**. Click **Done**.

### 11. Get Connection String
From the `.env.local` file shown on Neon’s Vercel page, **copy the `DATABASE_URL_UNPOOLED`**.

> **Purpose:** This is the database connection string used by SQLAlchemy.

---

## Project Setup Using `uv`

### 12. Initialize Project with `uv`
In your project directory, run:

```sh
uv init
```

> **Purpose:** Initializes a virtual environment and `pyproject.toml`.

### 13. Create `.env` File
Create a `.env` file in your project root.

> **Purpose:** To store sensitive environment variables securely.

### 14. Paste Database URL
Paste the `DATABASE_URL_UNPOOLED` into `.env`:

```env
DATABASE_URL_UNPOOLED=your_copied_url_here
```

> 💡 _Never commit `.env` files to version control._

### 15. Install Required Dependencies
Install SQLAlchemy, PostgreSQL driver, and dotenv support:

```sh
uv add sqlalchemy
uv add psycopg2-binary
uv add python-dotenv
```

> **Purpose:** Required for DB communication, PostgreSQL support, and environment variable loading.

---

## 16. Sample Python Script to Verify DB Connection

Create a file `main.py` and paste the following code:

```python
import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the database URL
DATABASE_URL = os.getenv("DATABASE_URL_UNPOOLED")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

def main():
    with engine.connect() as connection:
        # Create users table if not exists
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            );
        """))
        connection.commit()

        # Insert sample data (optional)
        # connection.execute(text("""
        #     INSERT INTO users (name, email)
        #     VALUES ('Taha', 'taha@example.com'),
        #            ('Ahmed', 'ahmed@example.com');
        # """))
        # connection.commit()

        # Fetch data
        result = connection.execute(text("SELECT * FROM users;")).mappings()

        print("Users in database:")
        for row in result:
            print(dict(row))

if __name__ == "__main__":
    main()
```

> ✅ **Purpose:** Confirms the database connection and table creation logic.

---

### 17. Open Database in Neon
From the Vercel Storage page, click **Open in Neon**.

### 18. View Data in Table Tab
- Navigate to the **Tables** tab (bottom left).
- View schema and data entries directly.