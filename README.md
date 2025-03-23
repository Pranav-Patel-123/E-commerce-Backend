# 🛒 E-commerce Backend  

This is the **backend service** for an **E-commerce platform**, built using **FastAPI**. It provides APIs for user authentication, category management, cart handling, and order processing. The backend is designed to work seamlessly with the **Next.js frontend**.  

## 🚀 Features  

✅ **User Authentication** – Register, login, and manage user sessions using JWT.  
✅ **Category Management** – Create, update, delete, and retrieve product categories.  
✅ **Cart System** – Add, remove, and update cart items for users.  
✅ **Order Processing** – Manage customer orders (Pending development).  
✅ **MongoDB Cloud Integration** – Store and retrieve data efficiently.  
✅ **RESTful API** – Designed with a clean and scalable API structure.  

## 🛠️ Tech Stack  

- **Backend Framework:** FastAPI (Python)  
- **Database:** MongoDB Cloud  
- **Authentication:** JWT (JSON Web Tokens)  
- **Payment Gateway:** (Pending implementation)  

## 📂 Project Structure  

```plaintext
/src
 ├── api/           # API routes and endpoints
 ├── models/        # Database models and schemas
 ├── services/      # Business logic and database operations
 ├── config/        # Configuration and environment settings
 ├── middlewares/   # Authentication and security middlewares
 ├── utils/         # Helper functions
 ├── tests/         # Unit and integration tests
 ├── main.py        # Entry point of the FastAPI application
```

## 🏗️ Installation & Setup  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/Pranav-Patel-123/E-commerce-Backend.git
cd E-commerce-Backend
```

### 2️⃣ Create a Virtual Environment  

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies  

```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables  

Create a `.env` file in the root directory and configure it:  

```plaintext
MONGO_DB_URI=<Your MongoDB Connection String>
JWT_SECRET=<Your Secret Key>
```
    
### 5️⃣ Run the Development Server  

```bash
uvicorn main:app --reload
```
API will be available at: **[http://localhost:8000](http://localhost:8000)**  

## ⚡ API Endpoints  

| Method | Endpoint | Description |
|--------|---------|-------------|
| `POST` | `/auth/register` | Register a new user |
| `POST` | `/auth/login` | Authenticate and get JWT token |
| `GET` | `/categories/` | Get all product categories |
| `POST` | `/categories/` | Create a new category |
| `GET` | `/cart/` | View user cart |
| `POST` | `/cart/` | Add item to cart |
| `DELETE` | `/cart/{item_id}` | Remove item from cart |

## 🤝 Contributing  

This project is **open for contributions**! 🎉  

- If you have ideas, improvements, or want to **add new features**, feel free to contribute.  
- The **order management** and **payment integration** are still pending, so contributors are welcome to help complete them.  

### Steps to Contribute  

1. **Fork** the repository  
2. **Create** a new branch (`git checkout -b feature-branch`)  
3. **Commit** your changes (`git commit -m "Added new feature"`)  
4. **Push** to your branch (`git push origin feature-branch`)  
5. **Create a Pull Request**  

## 📜 License  

This project is licensed under the **MIT License**.  

---

Feel free to contribute and help improve the project! 🚀  
