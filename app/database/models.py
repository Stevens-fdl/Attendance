from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.database import Base

class Subject(Base):
    __tablename__ =  "subject"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    session_num = Column(Integer, nullable=False, default=0)
    absence_num = Column(Integer, nullable=False, default=0)
    attendance_num = Column(Integer, nullable=False, default=0)
    last_attendance_date = Column(DateTime, nullable=False, default=datetime.now)
    percentage = Column(Integer, nullable=False, default=0)

