from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta

app = FastAPI(title="Subaru API")

# ---------- Данные машин ----------
cars = [
    {"id": 1, "name": "Subaru WRX", "engine": "2.0 Turbo", "type": "Sedan"},
    {"id": 2, "name": "Subaru Forester", "engine": "2.5", "type": "SUV"},
    {"id": 3, "name": "Subaru Outback", "engine": "2.5", "type": "Crossover"},
    {"id": 4, "name": "Subaru BRZ", "engine": "2.0", "type": "Coupe"},
]

# ---------- Простая «база» пользователей ----------
users_db = {}

# ---------- Настройки безопасности ----------
SECRET_KEY = "supersecretkey123"  # токен
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ---------- Хэлперы ----------
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None or username not in users_db:
            raise HTTPException(status_code=401, detail="Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# ---------- Основные endpoint ----------

@app.get("/")
def home():
    return {"message": "Subaru API работает"}

@app.get("/cars")
def get_cars():
    return {"cars": cars}

@app.get("/cars/{car_id}")
def get_car(car_id: int):
    for car in cars:
        if car["id"] == car_id:
            return car
    return {"error": "Car not found"}

# ---------- Регистрация ----------
@app.post("/register")
def register(username: str, password: str):
    if username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = get_password_hash(password)
    users_db[username] = {"username": username, "password": hashed_password}
    return {"message": f"User {username} registered successfully"}

# ---------- Логин ----------
@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(
        data={"sub": user["username"]}, 
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

# ---------- Пример защищённого endpoint ----------
@app.get("/profile")
def read_profile(current_user: str = Depends(get_current_user)):
    return {"user": current_user}