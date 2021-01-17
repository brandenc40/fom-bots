CREATE TABLE IF NOT EXISTS limits (
  id varchar(45) NOT NULL,
  period varchar(450) NOT NULL,
  calls integer NOT NULL DEFAULT '0',
  PRIMARY KEY (id)
);

CREATE INDEX IF NOT EXISTS period_idx ON limits USING btree(period);
