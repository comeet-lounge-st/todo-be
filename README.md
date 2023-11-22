## 설치
```bash
python3.11 -m pip install --upgrade pip
pip install -r requirements.txt
alembic upgrade head
```


## 실행

### Shell

```bash
python run.py
```

### Docker

```bash
docker build -t todo-be .
docker run -d --name todo-be -p 8000:8000 -v $PWD/db.sqlite3:/app/db.sqlite3 todo-be
```

## 프로젝트 구조

```
.
├── app                         # Application
│   ├── api                     # API를 구현하는 경로
│   │   └── routes              # 어플리케이션 단위로 엔드포인트를 설정하는 경로 / APIRouter를 사용 / Spring의 Controller 동일
│   ├── domain                  #
│   │   ├── entities            # pydantic의 BaseModel에 기반한 DTO, VO 등의 경로
│   │   ├── repositories        # Interface 형태의 Repository에 대한 경로
│   │   └── services            # Interface 형태의 Service에 대한 경로
│   ├── infrastructure          #
│   │   ├── db                  #
│   │   │   ├── models.py       # SqlAlchemy를 통해 DB와 연결할 DAO를 저장하는 파일
│   │   │   ├── repositories.py # Repository의 구현체에 대한 파일
│   │   │   └── session.py      # DB 커넥션을 저장하는 파일
│   │   ├── repositories        # Interface 형태의 Repository에 대한 경로
│   │   └── services            # Service의 구현체에 대한 경로
│   └── main.py                 # app의 instance를 만들고 설정하는 파일
├── config                      # 설정파일의 경로
├── migrations                  # alembic 기반의 마이그레이션 관련 경로
├── tests                       # 테스트와 관련된 경로
├── .env.sample                 # 환경변수 예제
├── .gitignore                  # git 제외 목록 파일
├── alembic.ini                 # 마이그레이션 설정 파일
├── CHANGELOG.md                # 변경 히스토리 파일
├── Dockerfile                  # 도커 파일
├── README.md                   # 사용설명서
├── requirements.txt            # 파이썬 패키지 목록 파일
└── run.py                      # 앱 실행 python 파일
```

## Migration

```
alembic revision --autogenerate -m "create todo table"
```
