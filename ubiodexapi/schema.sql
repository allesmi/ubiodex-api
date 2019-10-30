CREATE TABLE "kingdom"(
	kingdom_id SERIAL PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE "phylum"(
	phylum_id SERIAL PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE "class"(
	class_id SERIAL PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE "order"(
	order_id SERIAL PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE "family"(
	family_id SERIAL PRIMARY KEY,
	name VARCHAR(100)
);

CREATE TABLE species(
	species_id SERIAL PRIMARY KEY,
	-- Taxonomy ranks
	kingdom_id INTEGER,
	phylum_id INTEGER,
	class_id INTEGER,
	order_id INTEGER,
	family_id INTEGER,
	-- Names
	genus VARCHAR(100),
	subgenus VARCHAR(100),
	specific_epithet VARCHAR(100),
	infraspecific_epithet VARCHAR(100),
	scientific_name VARCHAR(300),
	-- Constraints
	FOREIGN KEY (kingdom_id) REFERENCES "kingdom" (kingdom_id),
	FOREIGN KEY (phylum_id) REFERENCES "phylum" (phylum_id),
	FOREIGN KEY (class_id) REFERENCES "class" (class_id),
	FOREIGN KEY (order_id) REFERENCES "order" (order_id),
	FOREIGN KEY (family_id) REFERENCES "family" (family_id)
);