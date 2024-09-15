REGISTRY := "ghcr.io/mp-bad"

up:
	docker compose -f docker-compose.dev.yaml up -d

down:
	docker compose -f docker-compose.dev.yaml down

build:
	docker compose -f ./Dockerfile.dev . -t ${REGISTRY}/backend:dev

build-prod:
	docker build --platform=linux/amd64 -f ./Dockerfile . -t ${REGISTRY}/backend:prod

pup:
	podman compose -f docker-compose.dev.yaml up -d

pdown:
	podman compose -f docker-compose.dev.yaml down

pbuild:
	podman build -f ./Dockerfile.dev . -t ${REGISTRY}/backend:dev

pbuild-prod:
	podman build --platform=linux/amd64 -f ./Dockerfile . -t ${REGISTRY}/backend:prod
