git stash
git pull
git stash pop

docker compose -f production.yml build
docker compose -f production.yml up -d
docker compose -f production.yml run --rm django python manage.py migrate
