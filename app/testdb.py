<-
This is a test file to test my connection for the credentials which I am passing using amazon and fastapi
->

# # from database import SessionLocal
# from sqlalchemy import create_engine, text  # Import create_engine and text
# from database import SessionLocal


# db = SessionLocal()

# try:
#     # result = db.execute(text("SELECT 1").fetchall())
#     # print("✅ Connection Successful!", result)
#     result = db.execute(text("SELECT 1"))  # Execute the query
#     rows = result.fetchall()  # Fetch the rows from the ResultProxy
#     print("✅ Connection Successful!", rows)
# except Exception as e:
#     print("❌ Connection Failed:", str(e))
# finally:  # Use a finally block to ensure db.close() is always called
#     db.close()

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session  # Import Session explicitly
from database import SessionLocal

# ... (your database URL and engine setup)

# db = SessionLocal()  # No longer create the session directly here

try:
    # Use a context manager to get a session and connection
    with SessionLocal() as session:  # Use SessionLocal as a context manager
        result = session.execute(text("SELECT 1"))  # Use the session to execute
        rows = result.fetchall()
        print("✅ Connection Successful!", rows)
except Exception as e:
    print("❌ Connection Failed:", str(e))