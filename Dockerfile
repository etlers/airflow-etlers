FROM apache/airflow:3.0.2

# 패키지를 이미지 빌드 시 미리 설치 (컨테이너 시작마다 pip install 방지)
RUN pip install --no-cache-dir \
    apache-airflow-providers-docker \
    apache-airflow-providers-fab \
    docker \
    httpx==0.28.1
