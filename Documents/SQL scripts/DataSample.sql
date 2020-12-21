INSERT INTO public.knowledge_category ("name",parent_id) VALUES
	 ('Hépatique (Marchantiophyte)',1),
	 ('Mousse (Bryophyte)',1),
	 ('Plante vasculaire (Trachéophyte)',1),
	 ('Plante à embryons (Embryophyte)',NULL),
	 ('Algue',NULL),
	 ('Plante à ovules (Spermatophyte)',5),
	 ('Plante à fleurs (Angiosperme)',6),
	 ('Conifère (pinophyte)',6);
INSERT INTO public.knowledge_color ("name") VALUES
	 ('Bleu'),
	 ('Jaune'),
	 ('Blanc'),
	 ('Rouge'),
	 ('Vert'),
	 ('Orange'),
	 ('Rose');
INSERT INTO public.knowledge_vegetal ("name",image,"comments",category_id,wiki) VALUES
	 ('Passiflore','Passiflora_caerulea_makro_close-up.jpg','Passiflora est un genre de plantes, les passiflores, de plus de 530 espèces de la famille des Passifloraceae.
Ce sont des plantes grimpantes aux fleurs spectaculaires, mais leur abondance n''est garantie que dans les régions au climat doux.',7,'https://www.wikiwand.com/fr/Passiflore'),
	 ('Coquelicot','fleur-rouge-coquelicot-1200x900.jpg','',7,'https://www.wikiwand.com/fr/Coquelicot'),
	 ('Cèdre atlas','cedre-bleu-de-l-atlas.jpg','',8,'https://www.wikiwand.com/fr/Cedrus_atlantica'),
	 ('Mousse commune','polytrichum-commune-600x450.jpg','',4,'https://www.wikiwand.com/fr/Bryophyta'),
	 ('Lys','lilies.jpg','Plusieurs couleurs possibles.',7,'https://www.wikiwand.com/fr/Lys'),
	 ('Magnolia','magnolia-arbre.jpg','',1,'https://www.wikiwand.com/fr/Magnolia'),
	 ('Sapin','5edf8c390479b_19_coupe_sapin_de_noel_de_l_lys_e_montsauche-00_01_26_02-4527673.jpg','',8,''),
	 ('Rose','Lions_Rose_1.jpg','',7,'');
INSERT INTO public.knowledge_vegetal_color (vegetal_id,color_id) VALUES
	 (1,1),
	 (1,3),
	 (2,4),
	 (3,1),
	 (4,5),
	 (5,4),
	 (5,6),
	 (6,3),
	 (6,7),
	 (7,5);
INSERT INTO public.knowledge_vegetal_color (vegetal_id,color_id) VALUES
	 (8,3),
	 (8,6);