CREATE TABLE IF NOT EXISTS agency (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc')
);


CREATE TABLE IF NOT EXISTS alert (
    id SERIAL PRIMARY KEY,
    agency_id INTEGER REFERENCES agency (id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    x_coordinate FLOAT NOT NULL,
    y_coordinate FLOAT NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc')
);

CREATE TABLE IF NOT EXISTS contact (
    id SERIAL PRIMARY KEY,
    info TEXT,
    filter_type VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS pin (
    id SERIAL PRIMARY KEY,
    agency_id INTEGER REFERENCES agency (id),
    title VARCHAR(255) NOT NULL,
    description TEXT,
    filter_type VARCHAR(50) NOT NULL,
    x_coordinate FLOAT NOT NULL,
    y_coordinate FLOAT NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (NOW() AT TIME ZONE 'utc')
);

CREATE INDEX IF NOT EXISTS agency_title_idx ON agency USING GIN (title gin_trgm_ops);
CREATE INDEX IF NOT EXISTS alert_title_idx ON alert USING GIN (title gin_trgm_ops);
CREATE INDEX IF NOT EXISTS alert_title_idx ON alert USING GIN (title gin_trgm_ops);