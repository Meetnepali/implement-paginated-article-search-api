from fastapi import APIRouter, HTTPException, status, Depends
from profiles.models import UserProfile, UserProfileCreate, UserProfileUpdate
from profiles.exceptions import UserProfileNotFound, DuplicateUsernameException
from typing import List

router = APIRouter(prefix="/profiles", tags=["profiles"])

# In-memory store
_profiles_db = {}

@router.post("/", response_model=UserProfile, status_code=status.HTTP_201_CREATED)
def create_profile(profile: UserProfileCreate):
    if profile.username in _profiles_db:
        raise DuplicateUsernameException(profile.username)
    _profiles_db[profile.username] = profile.dict()
    return _profiles_db[profile.username]

@router.get("/{username}", response_model=UserProfile)
def get_profile(username: str):
    user = _profiles_db.get(username)
    if not user:
        raise UserProfileNotFound(username)
    return user

@router.put("/{username}", response_model=UserProfile)
def update_profile(username: str, profile_update: UserProfileUpdate):
    user = _profiles_db.get(username)
    if not user:
        raise UserProfileNotFound(username)
    # Only update specified fields
    data = user.copy()
    update_data = profile_update.dict(exclude_unset=True)
    data.update(update_data)
    # Validate full update
    try:
        new_profile = UserProfile(**data)
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
    _profiles_db[username] = new_profile.dict()
    return _profiles_db[username]

@router.delete("/{username}", status_code=status.HTTP_204_NO_CONTENT)
def delete_profile(username: str):
    if username not in _profiles_db:
        raise UserProfileNotFound(username)
    del _profiles_db[username]
    return

@router.get("/", response_model=List[UserProfile])
def list_profiles():
    return list(_profiles_db.values())