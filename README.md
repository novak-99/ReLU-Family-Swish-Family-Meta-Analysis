# Meta-analysis on Swish and ReLU Activation Function Families
Comparing why the Swish activation function family has made accuracy imrpovements over the ReLU activation function family.

## Overview

This can be seen in comparisons of smoothness, self-gatededness, saturation, preconditioning, and empirics. 

### Smoothness Comparisons 

The Swish (left) vs ReLU (right) activation landscapes. 

![silu_landscape](https://github.com/novak-99/ReLU-Family-Swish-Family-Meta-Analysis/assets/78002988/560360ad-9ba6-4df7-8661-19150f9a5338)
![relu_landscape](https://github.com/novak-99/ReLU-Family-Swish-Family-Meta-Analysis/assets/78002988/65f233cb-97e0-4b10-91a1-863da5b3a1af)

### Convergence Comparisons

The percentage of times that global optima were attained by Swish and ReLU

Number of Layers | #1 | #2 
1 | 60.39% ± 5.00% | 41.02% ± 4.65% 
2 | 34.82% ± 5.04% | 20.06% ± 3.99% 
3 | 16.92% ± 3.74% | 8.76% ± 2.46% 

### Empirical Comparisons (MNIST)

![mnist_acc](https://github.com/novak-99/ReLU-Family-Swish-Family-Meta-Analysis/assets/78002988/28496880-d48b-4e76-b79d-98b1bc1f1ae6)

## Download 

The paper can be downloaded [here](https://github.com/novak-99/ReLU-Family-Swish-Family-Meta-Analysis/files/13199594/Swish_Fam_vs_ReLU_Fam.pdf). 
