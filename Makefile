.PHONY: run-dev
run-dev:
	cd fom_bots && uvicorn main:app --reload --log-level='debug'

.PHONY: run
run:
	cd fom_bots && uvicorn main:app --host=0.0.0.0 --port=$${PORT:-33507} --workers=1
