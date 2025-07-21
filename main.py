from fastapi import FastAPI, Depends, HTTPException
from database import get_db
from sqlalchemy.orm import Session
from models import Notes
from schemas import NoteCreateRequest, NoteUpdateRequest
import uvicorn

app = FastAPI()

@app.get("/notes")
def show_notes(db: Session = Depends(get_db)):
    all_notes = db.query(Notes).all()
    return all_notes
@app.get("/notes/{note_id}")
def test_1(note_id:int, db: Session = Depends(get_db)):
    note = db.query(Notes).filter(Notes.id==note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Not found")
    return note

@app.post("/notes")
def create_note(note_data: NoteCreateRequest, db: Session = Depends(get_db)):
    new_note = Notes(
        title = note_data.title,
        note_text = note_data.note_text
    )
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note

@app.patch("/notes/{note_id}")
def update_note(note_id: int, update_data: NoteUpdateRequest, db: Session = Depends(get_db)):
    note = db.query(Notes).filter(Notes.id==note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Not found")
    if update_data.title is not None:
        note.title = update_data.title
    if update_data.note_text is not None:
        note.note_text = update_data.note_text

    db.commit()
    db.refresh(note)

    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note = db.query(Notes).filter(Notes.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(note)
    db.commit()

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)