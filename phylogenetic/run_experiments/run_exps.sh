#!/bin/bash

date

rm k_centers_1.txt
rm k_centers_2.txt
rm k_random_1.txt
rm k_random_2.txt 
rm k_pc_1.txt
rm k_pc_2.txt

touch k_centers_1.txt
touch k_centers_2.txt
touch k_random_1.txt
touch k_random_2.txt 
touch k_pc_1.txt
touch k_pc_2.txt

bash experiment_general.sh 500 kcenters_ ../cluster/k_centers.py >> ../run_experiments/k_centers_1.txt
bash experiment_general.sh 550 kcenters_ ../cluster/k_centers.py >> ../run_experiments/k_centers_2.txt
bash experiment_general.sh 500 kmedoids_random_ ../cluster/k_medoids_random.py >> ../run_experiments/k_random_1.txt
bash experiment_general.sh 550 kmedoids_random_ ../cluster/k_medoids_random.py >> ../run_experiments/k_random_2.txt
bash experiment_general.sh 500 kmedoids_pointcollect_ ../cluster/k_medoids_pointcollect.py >> ../run_experiments/k_pc_1.txt
bash experiment_general.sh 500 kmedoids_pointcollect_ ../cluster/k_medoids_pointcollect.py >> ../run_experiments/k_pc_2.txt

date 