from pydantic import BaseModel

class SubjectCreateRequest(BaseModel):
    subject_name: str