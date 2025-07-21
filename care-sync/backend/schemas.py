# backend/schemas.py

from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class AppointmentBase(BaseModel):
    appointment_time: Optional[datetime] = None


class AppointmentCreate(AppointmentBase):
    pass


class AppointmentRead(AppointmentBase):
    id: int
    patient_id: int

    class Config:
        orm_mode = True


class PatientBase(BaseModel):
    name: str
    age: int


class PatientCreate(PatientBase):
    pass


class PatientRead(PatientBase):
    id: int
    appointments: List[AppointmentRead] = []

    class Config:
        orm_mode = True
