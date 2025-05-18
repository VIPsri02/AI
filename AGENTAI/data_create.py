from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from datetime import datetime
import os
import random

# Ensure the directory exists
db_folder = "AGENTAI"
db_file = "your_database.db"
os.makedirs(db_folder, exist_ok=True)

# Database setup
db_path = os.path.join(db_folder, db_file)
engine = create_engine(f'sqlite:///{db_path}')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Table Definitions
class Shipment(Base):
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True)
    shipment_number = Column(String, unique=True)
    origin = Column(String)
    destination = Column(String)
    weight = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    awbs = relationship("AWB", back_populates="shipment")

class AWB(Base):
    __tablename__ = 'awbs'
    id = Column(Integer, primary_key=True)
    awb_number = Column(String, unique=True)
    shipment_id = Column(Integer, ForeignKey('shipments.id'))
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    shipment = relationship("Shipment", back_populates="awbs")

# Create tables
Base.metadata.create_all(engine)
print(f"Database created at: {db_path}")
