#!/bin/bash

path_to_traces="traces"
path_to_results="ChampSim/results_30M"



cd ChampSim
./build_champsim.sh bimodal no ipcp ipcp ipcp lru 1
cd ..
for file in "$path_to_traces"/*
do
  file="${file#$path_to_traces/}"
  echo "$file"
  cd ChampSim/
  ./run_champsim.sh bimodal-no-ipcp-ipcp-ipcp-lru-1core 30 30 $file 
  cd ..
done
