from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class UserList(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: datetime.time


class ReadUserList(BaseModel):
    id: int
    name: str
    email: str
    password: str
    created_at: datetime.time
    class Config:
        from_attributes = True


class Teams(BaseModel):
    id: int
    name: str
    created_at: datetime.time


class ReadTeams(BaseModel):
    id: int
    name: str
    created_at: datetime.time
    class Config:
        from_attributes = True


class Tasks(BaseModel):
    id: int
    title: str
    visibility: bool
    priority: str
    created_at: datetime.time
    description: str


class ReadTasks(BaseModel):
    id: int
    title: str
    visibility: bool
    priority: str
    created_at: datetime.time
    description: str
    class Config:
        from_attributes = True


class UserTeamMapping(BaseModel):
    id: int
    team_id: int
    user_id: int
    created_at: datetime.time


class ReadUserTeamMapping(BaseModel):
    id: int
    team_id: int
    user_id: int
    created_at: datetime.time
    class Config:
        from_attributes = True


class TaskMapping(BaseModel):
    id: int
    task_id: int
    user_id: int
    team_id: int
    created_at: datetime.time


class ReadTaskMapping(BaseModel):
    id: int
    task_id: int
    user_id: int
    team_id: int
    created_at: datetime.time
    class Config:
        from_attributes = True




class PostUserList(BaseModel):
    id: int
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class PutUserListId(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class PostTeams(BaseModel):
    id: str
    name: str
    created_at: str

    class Config:
        from_attributes = True



class PutTeamsId(BaseModel):
    id: str
    name: str
    created_at: str

    class Config:
        from_attributes = True



class PostTasks(BaseModel):
    id: str
    title: str
    visibility: str
    priority: str
    created_at: str
    description: str

    class Config:
        from_attributes = True



class PutTasksId(BaseModel):
    id: str
    title: str
    visibility: str
    priority: str
    created_at: str
    description: str

    class Config:
        from_attributes = True



class PostUserTeamMapping(BaseModel):
    id: str
    team_id: str
    user_id: str
    created_at: str

    class Config:
        from_attributes = True



class PutUserTeamMappingId(BaseModel):
    id: str
    team_id: str
    user_id: str
    created_at: str

    class Config:
        from_attributes = True



class PostTaskMapping(BaseModel):
    id: str
    task_id: str
    user_id: str
    team_id: str
    created_at: str

    class Config:
        from_attributes = True



class PutTaskMappingId(BaseModel):
    id: str
    task_id: str
    user_id: str
    team_id: str
    created_at: str

    class Config:
        from_attributes = True

