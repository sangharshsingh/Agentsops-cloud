
from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        max_length=5000,
        description="Instruction for the AI agent"
    )

    agent_type: str = Field(
        default="research",
        description="Type of agent to execute the task"
    )
