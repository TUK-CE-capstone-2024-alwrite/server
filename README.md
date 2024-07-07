# 📺 노트 필기 어플리케이션 Alwrite

<br>

## 프로젝트 소개

- 다양한 필기 기능을 가지고 있는 노트 어플리케이션으로
- 기존 노트 어플리케이션에서 OCR를 활용한 텍스트 변환 기능과 녹음 요약 기능을 추가한 다용도 플랫폼입니다.
- 해당 레포지토리는 백엔드에 해당하는 레포지토리입니다.
<br>

## 팀원 구성

<div align="center">

| **오하민** | **김민지** |
| :------: | :------: |
| [<img width="140px" src="https://avatars.githubusercontent.com/u/113972482?v=4" height=150 width=150> <br/> @ohamin26](https://github.com/ohamin26) | [<img width="140px" src="https://avatars.githubusercontent.com/u/102501739?v=4" height=150 width=150> <br/> @min9-525](https://github.com/min9-525) |

</div>

<br>

## 1. 개발 환경

- Language && Framework : python, flask, firebase
- 버전 및 이슈관리 : Github, Github Issues
- 서비스 배포 환경 : GCP, Docker, Docker-compose, nginx, gunicorn, github-actions
  <br>

## 2. 채택한 개발 기술과 브랜치 전략

### python, flask

- 프로젝트에서 사용되는 OCR 기능이 python 기반으로 동작하기 때문에 파이썬을 선택하였습니다.
- 서버 규모가 크지 않기 때문에 python 라이브러리 중 필요한 부분만 개발 가능한 라이브러리인 flask를 선택하였습니다.
  
### firebase

- 관리해야할 데이터가 비교적 적고, firebase의 storage를 활용하기 위해 선택하였습니다.

### GCP

- 다른 클라우드 플랫폼과 비교했을 때 성능 대비 비용이 가장 저렴한 GCP를 선택하였습니다.

### Docker, Docker-compose, nginx, gunicorn, github-actions

- 클라이언트와 원할한 통신을 위해 HTTPS 통신을 지원하는 nginx을 선택하였습니다.
- nginx와 flask를 간편히 관리하기 위해 Dokcer를 도입, Docker-compose를 통해 하나로 묶어 관리하였습니다.
- python wsgi중 관리가 원할한 gunicorn를 채택하였습니다.
- 배포 자동화를 위해 github-actions를 도입했습니다.

### 브랜치 전략

- Git-flow를 채택하였으며, main, dev, feat로 구분하여 진행하였습니다.
  - **main** 배포용으로 최종적으로 적용할 기능만을 합쳤습니다.
  - **dev** 모든 기능을 합치고 개발과 테스트 단계에 사용하는 브랜치 입니다.
  - **Feat** 개발을 효율적으로 진행하기 위해 기능 단위로 브랜치을 생성하여 dev 브랜치에 합치는 방식으로 진행하였습니다.

<br>

## 3. 프로젝트 구조

```
├── README.md
├── .dockerignore
├── .gitignore
├── .gitmodules
├── pacage-lock.json
├── docker-compose.yml
│
├── .github/workflows
│    └── main.yml│
│
├── .nginx
│    ├── Dockerfile
│    ├── default.conf
│    └── nginx.conf
│
└── src
     ├── EasyOCR
     ├── secret_info(submodules)
     ├── speach_file
     ├── dao
     ├── database
     ├── services
     ├── controllers
     ├── Dockerfile
     ├── __init__.py
     ├── requirements.txt
     └── routes.py
```

<br>

## 4. 개발 기간 및 작업 관리

### 개발 기간

- 전체 개발 기간 : 2024.03.01 ~

<br>

### 작업 관리

- Gihub를 통해 관리하였습니다.

## 5. 트러블 슈팅
