copy:
    cp dist/* /var/www/html

server:
    uvicorn wheel_of_learning_backend.server:app
