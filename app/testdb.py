from sqlalchemy import text
from database import SessionLocal

try:
    # Create a new session
    session = SessionLocal()
    
    # Execute a test query
    result = session.execute(text("SELECT 1")).fetchall()
    
    print("✅ Connection Successful!", result)
except Exception as e:
    print("❌ Connection Failed:", str(e))
finally:
    session.close()  