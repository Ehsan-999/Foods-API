from fastapi import FastAPI, status, Query, HTTPException
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel,conint, constr
import uuid
import json
import os

app = FastAPI()

foods = [
    {"id": "123", "title": "apple", "description": "fruit", "estimated_time": 5, "difficulty": "easy"}
]

class Foods(BaseModel):
    title: constr(min_length=1)
    category: str
    description: str
    estimated_time: conint(gt=0)
    difficulty: str

if os.path.exists("data/foods.json"):
    with open("data/foods.json", "r", encoding="utf-8") as f:
        foods = json.load(f)

@app.get("/foods", status_code=status.HTTP_200_OK)
async def get_foods(export: str = Query(None)):
    if export is not None:
        file_path = "data/foods.json"
        os.makedirs("data", exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(foods, f, ensure_ascii=False, indent=2)


        return FileResponse(
            path=file_path,
            filename="foods.json",
            media_type="application/json"
        )

    return foods


@app.post("/foods", status_code=status.HTTP_201_CREATED)
async def create_food(request_data: Foods):
    new_food = {
        "id": str(uuid.uuid4()),
        "title": request_data.title,
        "category": request_data.category,
        "description": request_data.description,
        "estimated_time": request_data.estimated_time,
        "difficulty": request_data.difficulty,
    }
    foods.append(new_food)
    return JSONResponse(content=new_food)


@app.get("/foods/{food_id}", status_code=status.HTTP_200_OK)
async def show_food(food_id: str):
    for food in foods:
        if food["id"] == food_id:
            return food
    raise HTTPException(status_code=404, detail="Food not found")


@app.put("/foods/{food_id}", status_code=status.HTTP_200_OK)
async def edit_food(food_id: str, request_data: Foods):
    for food in foods:
        if food["id"] == food_id:
            food["title"] = request_data.title
            food["category"] = request_data.category
            food["description"] = request_data.description
            food["estimated_time"] = request_data.estimated_time
            food["difficulty"] = request_data.difficulty
            return food

    raise HTTPException(status_code=404, detail="Food not found")



@app.delete("/foods/{food_id}", status_code=status.HTTP_200_OK)
async def delete_food(food_id: str):
    global foods
    new_foods = [food for food in foods if food["id"] != food_id]

    if len(new_foods) == len(foods):
        raise HTTPException(status_code=404, detail="Food not found")

    foods = new_foods
    return {"detail": "Deleted successfully"}
