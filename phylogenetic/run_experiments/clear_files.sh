#!/bin/bash


# Change into experiment directory
cd /home/jsung/Documents/SummerResearch2016/phylogenetic/run_experiments

# Resetting the files 
rm experiment_info/kcenters_info.out
rm experiment_info/kcenters_result.out
touch experiment_info/kcenters_info.out
touch experiment_info/kcenters_result.out

rm experiment_info/km_random_info.out
rm experiment_info/km_random_result.out
touch experiment_info/km_random_info.out
touch experiment_info/km_random_result.out

rm experiment_info/km_pc_info.out
rm experiment_info/km_pc_result.out
touch experiment_info/km_pc_info.out
touch experiment_info/km_pc_result.out

# Alert done!
echo "beep boop == Reset all files for experiments! :) == beep boop"