FROM python:3.10
ENV PYTHONUNBUFFERED=1
COPY . .
RUN pip install openai django requests whitenoise
WORKDIR '/LoginSignUp'
CMD ["python", "manage.py", "runserver", "0:8080"]