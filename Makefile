.PHONY: run-dev
run-dev:
	@DEBUG=True python fom_bots/main.py

.PHONY: run
run:
	@echo "Starting app...."
	@python fom_bots/main.py