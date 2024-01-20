FROM python:3.12.1

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose port
EXPOSE 8000


# Start server
CMD python manage.py runserver