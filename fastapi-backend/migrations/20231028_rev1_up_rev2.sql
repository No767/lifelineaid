-- This is only used for testing purposes

CREATE TABLE IF NOT EXISTS devtest (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc')
);

CREATE INDEX IF NOT EXISTS devtest_name_idx ON devtest USING GIN (name gin_trgm_ops);

