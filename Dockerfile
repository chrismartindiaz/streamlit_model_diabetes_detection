FROM python:3.8
RUN pip install pandas scikit-learn==1.2.2 streamlit
COPY src/* /app/
COPY model/diabetes_model.pkl /app/
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]