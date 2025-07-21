# backend/app.py

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from models import Base, Patient, Appointment
from schemas import PatientCreate, PatientRead, AppointmentCreate, AppointmentRead
from database import engine, get_db

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Allow CORS for frontend if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/patients/", response_model=PatientRead)
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Patient(name=patient.name, age=patient.age)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient


@app.get("/patients/", response_model=List[PatientRead])
def read_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()


@app.post("/patients/{patient_id}/appointments/", response_model=AppointmentRead)
def create_appointment_for_patient(
    patient_id: int, appointment: AppointmentCreate, db: Session = Depends(get_db)
):
    db_appointment = Appointment(patient_id=patient_id, appointment_time=appointment.appointment_time)
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


@app.get("/appointments/", response_model=List[AppointmentRead])
def read_appointments(db: Session = Depends(get_db)):
    return db.query(Appointment).all()
