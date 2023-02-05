copy:
    cp dist/* /var/www/html

server:
    uvicorn --host 0.0.0.0 wheel_of_learning_backend.server:app

parcel:
    npx parcel wheel-of-learning-frontend/index.html

site: server parcel
    echo Ready
