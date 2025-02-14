from fastapi import APIRouter, Request, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/user_list/id')
async def get_user_list_id(db: Session = Depends(get_db)):
    try:
        return await service.get_user_list_id(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_list/')
async def post_user_list(raw_data: schemas.PostUserList, db: Session = Depends(get_db)):
    try:
        return await service.post_user_list(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_list/id/')
async def put_user_list_id(raw_data: schemas.PutUserListId, db: Session = Depends(get_db)):
    try:
        return await service.put_user_list_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_list/id')
async def delete_user_list_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user_list_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teams/')
async def get_teams(db: Session = Depends(get_db)):
    try:
        return await service.get_teams(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/teams/id')
async def get_teams_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_teams_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/teams/')
async def post_teams(raw_data: schemas.PostTeams, db: Session = Depends(get_db)):
    try:
        return await service.post_teams(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/teams/id/')
async def put_teams_id(raw_data: schemas.PutTeamsId, db: Session = Depends(get_db)):
    try:
        return await service.put_teams_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/teams/id')
async def delete_teams_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_teams_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/')
async def get_tasks(db: Session = Depends(get_db)):
    try:
        return await service.get_tasks(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/tasks/id')
async def get_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/tasks/')
async def post_tasks(raw_data: schemas.PostTasks, db: Session = Depends(get_db)):
    try:
        return await service.post_tasks(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/tasks/id/')
async def put_tasks_id(raw_data: schemas.PutTasksId, db: Session = Depends(get_db)):
    try:
        return await service.put_tasks_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/tasks/id')
async def delete_tasks_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_tasks_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_team_mapping/')
async def get_user_team_mapping(db: Session = Depends(get_db)):
    try:
        return await service.get_user_team_mapping(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/user_team_mapping/id')
async def get_user_team_mapping_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_user_team_mapping_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/user_team_mapping/')
async def post_user_team_mapping(raw_data: schemas.PostUserTeamMapping, db: Session = Depends(get_db)):
    try:
        return await service.post_user_team_mapping(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/user_team_mapping/id/')
async def put_user_team_mapping_id(raw_data: schemas.PutUserTeamMappingId, db: Session = Depends(get_db)):
    try:
        return await service.put_user_team_mapping_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/user_team_mapping/id')
async def delete_user_team_mapping_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_user_team_mapping_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/task_mapping/')
async def get_task_mapping(db: Session = Depends(get_db)):
    try:
        return await service.get_task_mapping(db)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/task_mapping/id')
async def get_task_mapping_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.get_task_mapping_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.post('/task_mapping/')
async def post_task_mapping(raw_data: schemas.PostTaskMapping, db: Session = Depends(get_db)):
    try:
        return await service.post_task_mapping(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.put('/task_mapping/id/')
async def put_task_mapping_id(raw_data: schemas.PutTaskMappingId, db: Session = Depends(get_db)):
    try:
        return await service.put_task_mapping_id(db, raw_data)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.delete('/task_mapping/id')
async def delete_task_mapping_id(id: int, db: Session = Depends(get_db)):
    try:
        return await service.delete_task_mapping_id(db, id)
    except Exception as e:
        raise HTTPException(500, str(e))

@router.get('/get-users')
async def get_get_users(page_number: int, page_size: int, db: Session = Depends(get_db)):
    try:
        return await service.get_get_users(db, page_number, page_size)
    except Exception as e:
        raise HTTPException(500, str(e))

