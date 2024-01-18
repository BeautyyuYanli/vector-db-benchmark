# Run in the root of the project
# export GH_TOKEN=xxx
poetry install --no-interaction --no-root
LATEST_STABLE_VERSION=$(gh release list --repo tensorchord/pgvecto.rs --exclude-drafts --exclude-pre-releases --limit 1 | awk '{print $3}')
docker remove -f pgvecto-rs-demo || true
docker run --rm --name pgvecto-rs-demo -p 5432:5432 -e POSTGRES_USER=root -e POSTGRES_PASSWORD=123456 -d tensorchord/pgvecto-rs:pg15-${LATEST_STABLE_VERSION}
poetry run python run.py --engines "*pgvecto_rs*"

python3 scripts/handle_price.py
python3 scripts/process_result_files.py

mv benchmark.json visualization/public/benchmark.json
cd visualization
git pull origin main
git add .
git commit -m "update benchmark.json $(date -Iminutes)"
git push origin HEAD:main
cd ..
