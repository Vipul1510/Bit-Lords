# Evaluations
<p> We evaluated few of the exisiting prefetchers along with IPCP prefetcher. Implementation of these prefetchers was already present in prefetcher folder of Champsim. 

Evaluated prefetchers:
1. IPCP
2. berti
3. next_line
4. sangam
5. no prefetcher 

Keep prefetchers of all above mentioned prefetchers in Champsim/prefetcher folder.
Run ./build_champsim and ./run_champsim with appropriate arguments( 30M instructions and warmup 30M instructions). Save results for each prefetcher. Using results.py you can get all IPC values in 1 file.
For each prefetcher collect results in seperate files (filename should be prefetcher name and keep everything in a folder named Evalutions_results) and then run plot.py outside the folder.
You will get a plot and a file.

Evaluations_results.png : It contains histograms and dashed lines. Dashed lines are the Cumulative IPC of the prefetcher

evaluations.txt : It contains Cumulative IPC of the all prefetchers calculated using geometric mean