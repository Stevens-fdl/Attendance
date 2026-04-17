from services.subjectServices import SubjectEngine
from database.database import db_dependency
from fastapi import APIRouter
from database.scheme import SubjectCreateRequest

router = APIRouter()





@router.post("/subject")
async def create_subject(request: SubjectCreateRequest, db: db_dependency):
    """
    Create a new subject with the given subject name.
    """
    engine = SubjectEngine(db)
    return engine.create_subject(request.subject_name)



@router.get("/subjects")
async def get_subjects(db: db_dependency):
    engine = SubjectEngine(db)
    return engine.get_subjects()



@router.get("/subject/{subject_id}")
async def get_subject(subject_id, db: db_dependency):
    """
    Retrieve details for a specific subject by its ID.
    """
    engine = SubjectEngine(db)
    return engine.get_subject(subject_id)



@router.post("/subject/{subject_id}/full-attendance")
async def mark_full_attendance(subject_id, db: db_dependency):
    """
    Mark as full day present for the specified subject.
    """
    engine = SubjectEngine(db)
    return engine.mark_full_attendance(subject_id)




@router.post("/subject/{subject_id}/full-absence")
async def mark_full_absence(subject_id, db: db_dependency):
    """
    Mark as full day absent for the specified subject.
    """
    engine = SubjectEngine(db)
    return engine.mark_full_absence(subject_id)



@router.post("/subject/{subject_id}/half-attendance")
async def mark_half_attendance(subject_id, db: db_dependency):
    engine = SubjectEngine(db)
    return engine.mark_half_attendance(subject_id)