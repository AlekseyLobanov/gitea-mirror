from pydantic import BaseModel, Field, HttpUrl
import datetime


class Config(BaseModel):
    repository_format: str
    ssh_key_path: str
    endpoint: HttpUrl
    token: str
    out_dir: str


class GiteaUser(BaseModel):
    user_id: int = Field(alias="id")
    login: str
    email: str


class GiteaRepository(BaseModel):
    ssh_url: str
    name: str
    repo_id: int = Field(alias="id")
    updated_at: datetime.datetime
    owner: GiteaUser
