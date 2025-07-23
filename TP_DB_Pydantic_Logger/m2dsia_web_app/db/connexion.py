from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# Exemple : utilisateur=root, motdepasse=secret, base=tpdb, host=localhost, port=3306
DATABASE_URL = "mysql+pymysql://root:secret@localhost:3306/tpdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()