from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from config.db import close_mongo_connection  # Import the function to close MongoDB
from routes.customer_auth import customer_auth_router
from routes.owner_auth import owner_auth_router
from routes.products_crud import product_router
from routes.cart_crud import cart_router
from routes.orders_crud import order_router
from routes.category_crud import category_router

 
# Lifespan event handler to manage startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    yield  # App is running
    await close_mongo_connection()  # Close MongoDB on shutdown

# Initialize FastAPI app with lifespan
app = FastAPI(lifespan=lifespan)

# CORS Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific origins for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

# Register Routes
app.include_router(customer_auth_router, prefix="/customer-auth", tags=["Customer Authentication"])
app.include_router(owner_auth_router, prefix="/owner-auth", tags=["Owner Authentication"])
app.include_router(product_router, prefix="/products", tags=["Product Management"])
app.include_router(cart_router, prefix="/cart", tags=["Cart Management"])
app.include_router(order_router, prefix="/orders", tags=["Orders"])
app.include_router(category_router, prefix="/category")
 
@app.get("/", tags=["Root"])
def home():
    return {"message": "Welcome to the E-commerce API"}
