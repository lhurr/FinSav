FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /code

COPY . /code
# COPY requirements.txt /code/

RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3002"]