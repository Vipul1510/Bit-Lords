# Bit-Lords

### Team Members:
| Name    | Roll Number |
| ----------- | ----------- |
| Jennisha Agrawal  | 210050074|
| Patil Vipul Sudhir   | 210050115|
|  Hari Prakash Reddy       | 210050119 |

### Contents of enhancement :
Each enhancement folder contains results of changed IPCP code using traces given `README` file of each enhancement

### Steps to run the code :

- Download [ChampSim repository](https://drive.google.com/drive/folders/1L3CAX_D21_fQOBHmW4UwZIjNKF2Oo4j0?usp=share_link)
- Download `script.sh` and place it in `champsim` folder.
- Download `results.py` and `plot_generator.py` and place it in `champsim/ChampSim` folder.
- Each enhancement folder contains 3 files named `ipcp.l1d_pref`, `ipcp.l2c_pref`, `ipcp.llc_pref`. Place them inside `ChampSim/prefetcher` folder.
- Each enhancement folder also contains a link in the traces. Download required traces from that link and place Place these files into `traces` folder.
- Run the following command in `champsim`: \
``` ./script ``` 
- Then run following command in `champsim/ChampSim` folder: \
``` python3 results.py ```
- It will create changed_ipcp.txt file which contains results.
- To generate plots using ipcp.txt and changed_ipcp.txt run following command: \
``` python3 plot_generator.py ```

### Presentation :
 Please refer to this [presentation](https://docs.google.com/presentation/d/1AM2d9zJpwczjgXRvh574nUCLLzyj63pyEr5ygZ_TsQY/edit?usp=sharing)

### References :
- [IPCP paper](https://www.cse.iitk.ac.in/users/biswap/IPCP_ISCA20.pdf)
- [IPCP presentation](https://dpc3.compas.cs.stonybrook.edu/slides/bouquet.pdf)
