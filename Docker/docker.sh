# Create New DB image
docker compose -f compose.db.yml up -d
# Create Dev BA_AUTH image
docker build -t anuchitorigin/ba_auth .
