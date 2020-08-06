# Simple-News-Board-API
### Описание запуска проекта
1. Установите docker, docker-compose
2. Скачайте данный репозиторий
3. Откройте терминал в директории проекта для сборки образа и запуска контейнера(для ubuntu перед командой docker-compose писать sudo):
```
docker-compose up -d --build
```
### API Documentation
API URL
```
api/v1/news_board/
```
| Method       |Authorization |URL           | Body  |Description |
| ------------- |:-------------:|------:| -----:|-----:|
| POST      |-| register/ | username, password, password_confirm | Register new user|
| POST     |+| post/create/      |   title, link |Create new post|
| GET |-| post/detail/{post_id}/     |    - |Watch post detail|
| PUT |+| post/detail/{post_id}/     |    title, link |Update post|
| DELETE |+| post/detail/{post_id}/     |    - |Delete post|
| GET |-| posts/    |    - |Shows list of posts|
| POST |+| post/upvote/{post_id}/    |   - |Upvote post|
| POST     |+| post/comment/      |   content |Create new comment| 
| GET |-| post/{post_id}/comments/    |    - |Shows comments for post({post_id}) |  
| GET |-| post/comment/detail/{comment_id}/   |    - |Watch comment detail|
| PUT |+| post/comment/detail/{comment_id}/   |    content |Update comment|
| DELETE |+| post/comment/detail/{comment_id}/   |    - |Delete comment|

