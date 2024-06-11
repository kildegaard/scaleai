from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from firebase_admin import credentials, firestore, initialize_app
from passlib.hash import bcrypt
import jwt
import datetime

app = FastAPI()
security = HTTPBearer()

# Firebase Initialization
cred = credentials.Certificate("serviceAccountKey.json")
initialize_app(cred)
db = firestore.client()

# Secret key for JWT
SECRET_KEY = "your_secret_key"


def create_token(user_id: str):
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow(),
        "sub": user_id,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")


def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    return decode_token(token)


@app.post("/register")
async def register_user(username: str, password: str):
    user_ref = db.collection("users").document(username)
    user = user_ref.get()
    if user.exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists"
        )
    hashed_password = bcrypt.hash(password)
    user_ref.set({"password": hashed_password})
    return {"message": "User created successfully"}


@app.post("/login")
async def login_user(username: str, password: str):
    user_ref = db.collection("users").document(username)
    user = user_ref.get()
    if not user.exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    if not bcrypt.verify(password, user.to_dict()["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password"
        )
    return {"token": create_token(username)}


@app.post("/posts")
async def create_post(title: str, content: str, user: str = Depends(get_current_user)):
    post_ref = db.collection("posts").document()
    post_ref.set(
        {"title": title, "content": content, "user": user, "likes": [], "comments": []}
    )
    return {"message": "Post created successfully"}


@app.get("/posts")
async def get_posts():
    posts_ref = db.collection("posts")
    posts = posts_ref.stream()
    all_posts = []
    for post in posts:
        all_posts.append(post.to_dict())
    return all_posts


@app.put("/posts/{post_id}")
async def update_post(
    post_id: str, title: str, content: str, user: str = Depends(get_current_user)
):
    post_ref = db.collection("posts").document(post_id)
    post = post_ref.get()
    if not post.exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    if post.to_dict()["user"] != user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not the owner of this post",
        )
    post_ref.update({"title": title, "content": content})
    return {"message": "Post updated successfully"}


@app.delete("/posts/{post_id}")
async def delete_post(post_id: str, user: str = Depends(get_current_user)):
    post_ref = db.collection("posts").document(post_id)
    post = post_ref.get()
    if not post.exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    if post.to_dict()["user"] != user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You are not the owner of this post",
        )
    post_ref.delete()
    return {"message": "Post deleted successfully"}


@app.post("/posts/{post_id}/like")
async def like_post(post_id: str, user: str = Depends(get_current_user)):
    post_ref = db.collection("posts").document(post_id)
    post = post_ref.get()
    if not post.exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    if user in post.to_dict()["likes"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have already liked this post",
        )
    post_ref.update({"likes": post.to_dict()["likes"] + [user]})
    return {"message": "Post liked successfully"}


@app.post("/posts/{post_id}/dislike")
async def dislike_post(post_id: str, user: str = Depends(get_current_user)):
    post_ref = db.collection("posts").document(post_id)
    post = post_ref.get()
    if not post.exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    if user not in post.to_dict()["likes"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="You have not liked this post",
        )
    post_ref.update(
        {"likes": [like for like in post.to_dict()["likes"] if like != user]}
    )
    return {"message": "Post disliked successfully"}


@app.post("/posts/{post_id}/comment")
async def comment_post(
    post_id: str, comment: str, user: str = Depends(get_current_user)
):
    post_ref = db.collection("posts").document(post_id)
    post = post_ref.get()
    if not post.exists:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    post_ref.update(
        {"comments": post.to_dict()["comments"] + [{"user": user, "comment": comment}]}
    )
    return {"message": "Comment added successfully"}
