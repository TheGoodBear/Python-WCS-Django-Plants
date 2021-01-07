INSERT INTO knowledge_category (id,name,parent_id) VALUES
	 (1,'Hépatique (Marchantiophyte)',1),
	 (2,'Mousse (Bryophyte)',1),
	 (3,'Plante vasculaire (Trachéophyte)',1),
	 (4,'Plante à embryons (Embryophyte)',NULL),
	 (5,'Algue',NULL),
	 (6,'Plante à ovules (Spermatophyte)',5),
	 (7,'Plante à fleurs (Angiosperme)',6),
	 (8,'Conifère (pinophyte)',6);
INSERT INTO knowledge_color (id,name) VALUES
	 (1,'Bleu'),
	 (2,'Jaune'),
	 (3,'Blanc'),
	 (4,'Rouge'),
	 (5,'Vert'),
	 (6,'Orange'),
	 (7,'Rose');
INSERT INTO knowledge_vegetal (id,name,image,"comments",category_id,wiki) VALUES
	 (1,'Passiflore','Passiflora_caerulea_makro_close-up.jpg','Passiflora est un genre de plantes, les passiflores, de plus de 530 espèces de la famille des Passifloraceae.
Ce sont des plantes grimpantes aux fleurs spectaculaires, mais leur abondance n''est garantie que dans les régions au climat doux.',7,'https://www.wikiwand.com/fr/Passiflore'),
	 (2,'Coquelicot','fleur-rouge-coquelicot-1200x900.jpg','',7,'https://www.wikiwand.com/fr/Coquelicot'),
	 (3,'Cèdre atlas','cedre-bleu-de-l-atlas.jpg','',8,'https://www.wikiwand.com/fr/Cedrus_atlantica'),
	 (4,'Mousse commune','polytrichum-commune-600x450.jpg','',4,'https://www.wikiwand.com/fr/Bryophyta'),
	 (5,'Lys','lilies.jpg','Plusieurs couleurs possibles.',7,'https://www.wikiwand.com/fr/Lys'),
	 (6,'Magnolia','magnolia-arbre.jpg','',1,'https://www.wikiwand.com/fr/Magnolia'),
	 (7,'Sapin','5edf8c390479b_19_coupe_sapin_de_noel_de_l_lys_e_montsauche-00_01_26_02-4527673.jpg','',8,''),
	 (8,'Rose','Lions_Rose_1.jpg','',7,'');
INSERT INTO knowledge_vegetal_color (id,vegetal_id,color_id) VALUES
	 (1,1,1),
	 (2,1,3),
	 (3,2,4),
	 (4,3,1),
	 (5,4,5),
	 (6,5,4),
	 (7,5,6),
	 (8,6,3),
	 (9,6,7),
	 (10,7,5),
	 (11,8,3),
	 (12,8,6);