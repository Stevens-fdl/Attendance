from database.database import db_dependency
from fastapi import HTTPException, status
from database import models 
from datetime import datetime



class SubjectEngine:
    def __init__(self, db: db_dependency):
        self.db = db



    def create_subject(self, subject_name):
        subject = models.Subject(name=subject_name)
        self.db.add(subject)
        self.db.commit()
        self.db.refresh(subject)
        
        return {
                "id": subject.id,
                "name": subject.name,
                "session_num": subject.session_num,
                "absence_num": subject.absence_num,
                "attendance_num": subject.attendance_num,
                "last_attendance_date": subject.last_attendance_date,
                "percentage": subject.percentage
            }



    def get_subjects(self):
        subjects = self.db.query(models.Subject).all()
        if not subjects:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "No subject, Create one")
        
        result = []
        for subject in subjects:
            result.append({
                "id": subject.id,
                "name": subject.name,
                "session_num": subject.session_num / 2,
                "absence_num": subject.absence_num,
                "attendance_num": subject.attendance_num,
                "last_attendance_date": subject.last_attendance_date,
                "percentage": subject.percentage
            })

        return result



    def get_subject(self, subject_id):
        subject = self.db.query(models.Subject).filter(models.Subject.id == subject_id).first()

        if not subject:
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Subject Not Found!")
        
        return subject



    def mark_full_attendance(self, subject_id):
        subject = self.get_subject(subject_id)
        
        subject.session_num = subject.session_num + 2
        subject.attendance_num = subject.attendance_num + 2
        subject.last_attendance_date = datetime.now()

        percentage = self.calculate_percentage(subject.attendance_num, subject.session_num) 
        subject.percentage = percentage
        self.db.commit()

        return percentage



    def mark_full_absence(self, subject_id):
        subject = self.get_subject(subject_id)
        
        subject.session_num = subject.session_num + 2
        subject.absence_num = subject.absence_num + 2
        subject.last_attendance_date = datetime.now()
        
        percentage = self.calculate_percentage(subject.attendance_num, subject.session_num) 
        subject.percentage = percentage
        self.db.commit()

        return percentage
    


    def mark_half_attendance(self, subject_id):
        subject = self.get_subject(subject_id)
        
        subject.session_num = subject.session_num + 2
        subject.attendance_num = subject.attendance_num + 1
        subject.absence_num = subject.absence_num + 1

        percentage = self.calculate_percentage(subject.attendance_num, subject.session_num) 
        subject.percentage = percentage
        self.db.commit()

        return percentage



    def reset_attendance(self, subject_id):
        subject = self.get_subject(subject_id)
        
        subject.session_num = 0
        subject.attendance_num = 0
        subject.absence_num = 0
        subject.percentage = 0

        self.db.commit()

        return {
                "id": subject.id,
                "name": subject.name,
                "session_num": subject.session_num,
                "absence_num": subject.absence_num,
                "attendance_num": subject.attendance_num,
                "last_attendance_date": subject.last_attendance_date,
                "percentage": subject.percentage
            }


    def calculate_percentage(self, num, session_num):
        return (num * 100) / session_num