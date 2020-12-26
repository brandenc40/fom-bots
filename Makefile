.PHONY: run-dev
run-dev:
	cd fom_bots && uvicorn main:app --reload --log-level='debug'

.PHONY: run
run:
	cd fom_bots && uvicorn main:app --host=0.0.0.0 --port=33507 --log-level='info'