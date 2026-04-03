# Airflow ETLers

이 디렉터리는 EKIS와 분리된 Airflow 홈입니다.

## 구성

- Airflow 이미지: `apache/airflow` 기반
- 별도 Postgres 컨테이너는 없음
- 메타 DB: `ekis`의 기존 `pg-db` 컨테이너
- 메타 스키마: `ekis_web.airflow_meta`
- 웹 포트: `http://localhost:9999`
- 실행기: `LocalExecutor`

## 주요 파일

- [`docker-compose.yml`](/Users/etlers/airflow-etlers/docker-compose.yml)
- [`Dockerfile`](/Users/etlers/airflow-etlers/Dockerfile)
- [`config/simple_auth_manager_passwords.json`](/Users/etlers/airflow-etlers/config/simple_auth_manager_passwords.json)
- [`dags/test_hello_dag.py`](/Users/etlers/airflow-etlers/dags/test_hello_dag.py)
- [`dags/`](/Users/etlers/airflow-etlers/dags)
- [`plugins/`](/Users/etlers/airflow-etlers/plugins)
- [`logs/`](/Users/etlers/airflow-etlers/logs)

## 접속 정보

- URL: `http://localhost:9999`
- 뷰어 계정: `guest / 1234`

## 실행 순서

초기화:

```bash
docker compose up airflow-init
```

본 실행:

```bash
docker compose up -d
```

중지:

```bash
docker compose down
```

## 테스트 DAG

`dags/` 아래의 DAG 파일들이 자동으로 로드됩니다. 현재는 테스트용 DAG를 하나 추가해두면 UI에서 바로 확인할 수 있습니다.

## 메모

- 이 Airflow는 `ekis` 프로젝트와 별도입니다.
- `ekis/airflow`가 아니라 이 폴더를 기준으로 작업해야 합니다.
- 로컬 `postgres` 컨테이너는 사용하지 않고, `ekis`의 `pg-db`를 공유합니다.
- Airflow 메타데이터만 `airflow_meta` 스키마로 분리합니다.
