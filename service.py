from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import *
from fastapi import Request, UploadFile, HTTPException
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_user_list_id(db: Session):

    user_list_one = db.query(models.UserList).all()
    user_list_one = [new_data.to_dict() for new_data in user_list_one] if user_list_one else user_list_one

    res = {
        'user_list_one': user_list_one,
    }
    return res

async def post_user_list(db: Session, raw_data: schemas.PostUserList):
    id:int = raw_data.id
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    import random

    try:
        integer = random.randint(1, 10000000)
    except Exception as e:
        raise HTTPException(500, str(e))



    
    from datetime import datetime

    try:
        # Get the current timestamp
        timestamp_curr:datetime = datetime.now();
    except Exception as e:
        raise HTTPException(500, str(e))



    record_to_be_added = {'id': id, 'name': name, 'email': email, 'password': password, 'created_at': timestamp_curr}
    new_user_list = models.UserList(**record_to_be_added)
    db.add(new_user_list)
    db.commit()
    db.refresh(new_user_list)
    user_list_inserted_record = new_user_list.to_dict()

    res = {
        'user_list_inserted_record': user_list_inserted_record,
    }
    return res

async def put_user_list_id(db: Session, raw_data: schemas.PutUserListId):
    name:str = raw_data.name
    email:str = raw_data.email
    password:str = raw_data.password


    user_list_edited_record = db.query(models.UserList).filter(models.UserList.id == id).first()
    for key, value in {'id': id, 'name': name, 'email': email, 'password': password, 'created_at': created_at}.items():
          setattr(user_list_edited_record, key, value)
    db.commit()
    db.refresh(user_list_edited_record)
    user_list_edited_record = user_list_edited_record.to_dict() 

    res = {
        'user_list_edited_record': user_list_edited_record,
    }
    return res

async def delete_user_list_id(db: Session, id: int):

    user_list_deleted = None
    record_to_delete = db.query(models.UserList).filter(models.UserList.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_list_deleted = record_to_delete.to_dict() 

    res = {
        'user_list_deleted': user_list_deleted,
    }
    return res

async def get_teams(db: Session):

    teams_all = db.query(models.Teams).all()
    teams_all = [new_data.to_dict() for new_data in teams_all] if teams_all else teams_all

    res = {
        'teams_all': teams_all,
    }
    return res

async def get_teams_id(db: Session, id: int):

    teams_one = db.query(models.Teams).filter(models.Teams.id == id).first() 
    teams_one = teams_one.to_dict() if teams_one else teams_one

    res = {
        'teams_one': teams_one,
    }
    return res

async def post_teams(db: Session, raw_data: schemas.PostTeams):
    id:str = raw_data.id
    name:str = raw_data.name
    created_at:str = raw_data.created_at


    record_to_be_added = {'id': id, 'name': name, 'created_at': created_at}
    new_teams = models.Teams(**record_to_be_added)
    db.add(new_teams)
    db.commit()
    db.refresh(new_teams)
    teams_inserted_record = new_teams.to_dict()

    res = {
        'teams_inserted_record': teams_inserted_record,
    }
    return res

async def put_teams_id(db: Session, raw_data: schemas.PutTeamsId):
    id:str = raw_data.id
    name:str = raw_data.name
    created_at:str = raw_data.created_at


    teams_edited_record = db.query(models.Teams).filter(models.Teams.id == id).first()
    for key, value in {'id': id, 'name': name, 'created_at': created_at}.items():
          setattr(teams_edited_record, key, value)
    db.commit()
    db.refresh(teams_edited_record)
    teams_edited_record = teams_edited_record.to_dict() 

    res = {
        'teams_edited_record': teams_edited_record,
    }
    return res

async def delete_teams_id(db: Session, id: int):

    teams_deleted = None
    record_to_delete = db.query(models.Teams).filter(models.Teams.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        teams_deleted = record_to_delete.to_dict() 

    res = {
        'teams_deleted': teams_deleted,
    }
    return res

async def get_tasks(db: Session):

    tasks_all = db.query(models.Tasks).all()
    tasks_all = [new_data.to_dict() for new_data in tasks_all] if tasks_all else tasks_all

    res = {
        'tasks_all': tasks_all,
    }
    return res

async def get_tasks_id(db: Session, id: int):

    tasks_one = db.query(models.Tasks).filter(models.Tasks.id == id).first() 
    tasks_one = tasks_one.to_dict() if tasks_one else tasks_one

    res = {
        'tasks_one': tasks_one,
    }
    return res

async def post_tasks(db: Session, raw_data: schemas.PostTasks):
    id:str = raw_data.id
    title:str = raw_data.title
    visibility:str = raw_data.visibility
    priority:str = raw_data.priority
    created_at:str = raw_data.created_at
    description:str = raw_data.description


    record_to_be_added = {'id': id, 'title': title, 'visibility': visibility, 'priority': priority, 'created_at': created_at, 'description': description}
    new_tasks = models.Tasks(**record_to_be_added)
    db.add(new_tasks)
    db.commit()
    db.refresh(new_tasks)
    tasks_inserted_record = new_tasks.to_dict()

    res = {
        'tasks_inserted_record': tasks_inserted_record,
    }
    return res

async def put_tasks_id(db: Session, raw_data: schemas.PutTasksId):
    id:str = raw_data.id
    title:str = raw_data.title
    visibility:str = raw_data.visibility
    priority:str = raw_data.priority
    created_at:str = raw_data.created_at
    description:str = raw_data.description


    tasks_edited_record = db.query(models.Tasks).filter(models.Tasks.id == id).first()
    for key, value in {'id': id, 'title': title, 'visibility': visibility, 'priority': priority, 'created_at': created_at, 'description': description}.items():
          setattr(tasks_edited_record, key, value)
    db.commit()
    db.refresh(tasks_edited_record)
    tasks_edited_record = tasks_edited_record.to_dict() 

    res = {
        'tasks_edited_record': tasks_edited_record,
    }
    return res

async def delete_tasks_id(db: Session, id: int):

    tasks_deleted = None
    record_to_delete = db.query(models.Tasks).filter(models.Tasks.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        tasks_deleted = record_to_delete.to_dict() 

    res = {
        'tasks_deleted': tasks_deleted,
    }
    return res

async def get_user_team_mapping(db: Session):

    user_team_mapping_all = db.query(models.UserTeamMapping).all()
    user_team_mapping_all = [new_data.to_dict() for new_data in user_team_mapping_all] if user_team_mapping_all else user_team_mapping_all

    res = {
        'user_team_mapping_all': user_team_mapping_all,
    }
    return res

async def get_user_team_mapping_id(db: Session, id: int):

    user_team_mapping_one = db.query(models.UserTeamMapping).filter(models.UserTeamMapping.id == id).first() 
    user_team_mapping_one = user_team_mapping_one.to_dict() if user_team_mapping_one else user_team_mapping_one

    res = {
        'user_team_mapping_one': user_team_mapping_one,
    }
    return res

async def post_user_team_mapping(db: Session, raw_data: schemas.PostUserTeamMapping):
    id:str = raw_data.id
    team_id:str = raw_data.team_id
    user_id:str = raw_data.user_id
    created_at:str = raw_data.created_at


    record_to_be_added = {'id': id, 'team_id': team_id, 'user_id': user_id, 'created_at': created_at}
    new_user_team_mapping = models.UserTeamMapping(**record_to_be_added)
    db.add(new_user_team_mapping)
    db.commit()
    db.refresh(new_user_team_mapping)
    user_team_mapping_inserted_record = new_user_team_mapping.to_dict()

    res = {
        'user_team_mapping_inserted_record': user_team_mapping_inserted_record,
    }
    return res

async def put_user_team_mapping_id(db: Session, raw_data: schemas.PutUserTeamMappingId):
    id:str = raw_data.id
    team_id:str = raw_data.team_id
    user_id:str = raw_data.user_id
    created_at:str = raw_data.created_at


    user_team_mapping_edited_record = db.query(models.UserTeamMapping).filter(models.UserTeamMapping.id == id).first()
    for key, value in {'id': id, 'team_id': team_id, 'user_id': user_id, 'created_at': created_at}.items():
          setattr(user_team_mapping_edited_record, key, value)
    db.commit()
    db.refresh(user_team_mapping_edited_record)
    user_team_mapping_edited_record = user_team_mapping_edited_record.to_dict() 

    res = {
        'user_team_mapping_edited_record': user_team_mapping_edited_record,
    }
    return res

async def delete_user_team_mapping_id(db: Session, id: int):

    user_team_mapping_deleted = None
    record_to_delete = db.query(models.UserTeamMapping).filter(models.UserTeamMapping.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        user_team_mapping_deleted = record_to_delete.to_dict() 

    res = {
        'user_team_mapping_deleted': user_team_mapping_deleted,
    }
    return res

async def get_task_mapping(db: Session):

    task_mapping_all = db.query(models.TaskMapping).all()
    task_mapping_all = [new_data.to_dict() for new_data in task_mapping_all] if task_mapping_all else task_mapping_all

    res = {
        'task_mapping_all': task_mapping_all,
    }
    return res

async def get_task_mapping_id(db: Session, id: int):

    task_mapping_one = db.query(models.TaskMapping).filter(models.TaskMapping.id == id).first() 
    task_mapping_one = task_mapping_one.to_dict() if task_mapping_one else task_mapping_one

    res = {
        'task_mapping_one': task_mapping_one,
    }
    return res

async def post_task_mapping(db: Session, raw_data: schemas.PostTaskMapping):
    id:str = raw_data.id
    task_id:str = raw_data.task_id
    user_id:str = raw_data.user_id
    team_id:str = raw_data.team_id
    created_at:str = raw_data.created_at


    record_to_be_added = {'id': id, 'task_id': task_id, 'user_id': user_id, 'team_id': team_id, 'created_at': created_at}
    new_task_mapping = models.TaskMapping(**record_to_be_added)
    db.add(new_task_mapping)
    db.commit()
    db.refresh(new_task_mapping)
    task_mapping_inserted_record = new_task_mapping.to_dict()

    res = {
        'task_mapping_inserted_record': task_mapping_inserted_record,
    }
    return res

async def put_task_mapping_id(db: Session, raw_data: schemas.PutTaskMappingId):
    id:str = raw_data.id
    task_id:str = raw_data.task_id
    user_id:str = raw_data.user_id
    team_id:str = raw_data.team_id
    created_at:str = raw_data.created_at


    task_mapping_edited_record = db.query(models.TaskMapping).filter(models.TaskMapping.id == id).first()
    for key, value in {'id': id, 'task_id': task_id, 'user_id': user_id, 'team_id': team_id, 'created_at': created_at}.items():
          setattr(task_mapping_edited_record, key, value)
    db.commit()
    db.refresh(task_mapping_edited_record)
    task_mapping_edited_record = task_mapping_edited_record.to_dict() 

    res = {
        'task_mapping_edited_record': task_mapping_edited_record,
    }
    return res

async def delete_task_mapping_id(db: Session, id: int):

    task_mapping_deleted = None
    record_to_delete = db.query(models.TaskMapping).filter(models.TaskMapping.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        task_mapping_deleted = record_to_delete.to_dict() 

    res = {
        'task_mapping_deleted': task_mapping_deleted,
    }
    return res

async def get_get_users(db: Session, page_number: int, page_size: int):
    res = {
    }
    return res

