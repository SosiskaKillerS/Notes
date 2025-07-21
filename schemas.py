from typing import Optional
from pydantic import BaseModel, Field

class NoteCreateRequest(BaseModel):
    title: str = Field(..., max_length= 50)
    note_text: str = Field(..., max_length=250)


class NoteUpdateRequest(BaseModel):
    title: Optional[str]
    note_text: Optional[str]

