.PHONY: dev
dev:
	flask --app ti_draft_api/app run

>PHONY: test
test:
	pytest --strict-markers