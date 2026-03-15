### **Setup & Run Instructions**

1. **Create virtual environment**

   ```bash
   py -m venv venv
   ```

2. **Activate the virtual environment**

   ```bash
   venv\Scripts\activate
   ```

3. **Create a `.env` file**
   - Copy `.env.example` to `.env` and configure your environment:

   ```bash
   copy .env.example .env
   ```

   - Edit `.env` with your settings:

   **Development:**

   ```env
   ENV=development
   DEV_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
   PROD_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
   ```

   **Production:**

   ```env
   ENV=production
   DEV_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
   PROD_ORIGINS=https://yourdomain.com,https://www.yourdomain.com
   ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the server**

   ```bash
   uvicorn main:app --port 3002
   ```
