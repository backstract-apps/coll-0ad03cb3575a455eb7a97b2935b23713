from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

# Create database connection URL
DATABASE_URL = URL.create(
    drivername='postgresql+psycopg2',
    username='postgres.hzdxvnoxwqilsmkguzms',
    password='G!8vL@9z#XqT2&pD',
    host='aws-0-ap-south-1.pooler.supabase.com',
    port=5432,
    database='postgres'
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
