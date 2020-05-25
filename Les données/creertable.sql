
CREATE TABLE compagnie (
                id_comp INTEGER NOT NULL,
                nom_comp VARCHAR,
                pays_comp VARCHAR,
                CONSTRAINT compagnie_pk PRIMARY KEY (id_comp)
);


CREATE TABLE aeroport (
                id_aero INTEGER NOT NULL,
                nom_aero VARCHAR,
                ville_aero VARCHAR,
                gmt_aero VARCHAR,
                pays_aero VARCHAR,
                CONSTRAINT aeroport_pk PRIMARY KEY (id_aero)
);


CREATE TABLE route (
                id_route INTEGER NOT NULL,
                id_aero_dep INTEGER NOT NULL,
                id_aero_arr INTEGER NOT NULL,
                id_comp INTEGER NOT NULL,
                CONSTRAINT route_pk PRIMARY KEY (id_route, id_aero_dep, id_aero_arr, id_comp)
);


ALTER TABLE route ADD CONSTRAINT compagnie_route_fk
FOREIGN KEY (id_comp)
REFERENCES compagnie (id_comp)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE route ADD CONSTRAINT aeroport_route_fk
FOREIGN KEY (id_aero_dep)
REFERENCES aeroport (id_aero)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;

ALTER TABLE route ADD CONSTRAINT aeroport_route_fk1
FOREIGN KEY (id_aero_arr)
REFERENCES aeroport (id_aero)
ON DELETE NO ACTION
ON UPDATE NO ACTION
NOT DEFERRABLE;