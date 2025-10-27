from pydantic import BaseModel, List

class Lesson(BaseModel):
    id:int
    topic: str

class Modules(BaseModel):
    id:int
    title:str
    lessons: List[Lesson]

class Course(BaseModel):
    id:int
    title:str
    modules:List[Modules]