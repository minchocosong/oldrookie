# 도커로 코드 테스트 하는 방법
1. DockerHub에 가입한다. https://hub.docker.com/
2. 로컬 컴퓨터에 도커를 설치한다. https://docs.docker.com/
3. 터미널에서 최초로 docker 실행을 할 경우 docker login 을 한다.

---

## python code 테스트하는 방법
베이스 이미지는 dockerhub의 python3으로 지정한다. <br/>
테스트 코드가 작성된 현재 로컬 디렉토리($PWD)를 컨테이너 내에 /usr/src/myapp로 볼륨마운트를 하고, 컨테이너의 워킹 디렉도리를 /usr/src/myapp로 지정한다. <br/>
아래 예제에서 사용된 docker run 옵션은 아래와 같다. <br/>
| 옵션  | 설명                          |
| :--- | ---------------------------: |
| v   | 볼륨 마운트                      |
| w   | 컨테이너 내 Working Directory 지정 |

<br/>

> ### 1. python 디렉토리 이동
```
cd python
```

> ### 2. docker로 실행 
docker run --rm -v "$PWD":{마운트할컨테이너내부path} -w {컨테이너내부워킹디렉토리} python:3 python {파일명}
``` 
docker run --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python test_01.py
```

> ### 3. VSCode Docker Debug 환경 구성
https://code.visualstudio.com/docs/remote/containers

<br/>


## javascript code 테스트하는 방법

> ### 1. javascript 디렉토리 이동
```
cd javascript
```

> ### 2. docker로 실행
```
docker run --rm -v $(pwd):/app -w /app node:9 node test_01.js

```
