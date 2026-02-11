# ---------- FRONTEND BUILD STAGE ----------
FROM node:20 AS frontend

WORKDIR /app

# Copy package files
COPY package*.json ./
RUN npm install

# Copy all project files
COPY . .

# Build Vue
RUN npm run build


# ---------- BACKEND STAGE ----------
FROM python:3.13

WORKDIR /app

# Install backend dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY . .

# Copy built Vue dist into Flask static folder
COPY --from=frontend /app/dist ./static

# Expose port (required for Koyeb)
EXPOSE 8000

# Run app using dynamic port
CMD ["sh", "-c", "gunicorn app:app --bind 0.0.0.0:$PORT"]
