-- Database seed file
CREATE TABLE IF NOT EXISTS sample_seed (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO sample_seed (name) VALUES ('Initial Seed Data') ON CONFLICT DO NOTHING;
