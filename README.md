# ptt-stock-crawler

## Introduction
- This is a simple web crawler for PTT stock board. It can crawl the latest posts in the stock board and save them to a local database. 
- The crawler will crawl the latest posts in the stock board every 10 minutes. If there are new posts, it will save them to the database.


## Installation and Usage
1. Clone the repository
```
git clone  https://github.com/VannaChiang/ptt-stock-crawler.git
```

2. Run the crawler using Docker
```
docker-compose up --build
```

3. Access http://localhost/docs to test the API