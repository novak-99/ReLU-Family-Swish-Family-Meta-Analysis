# Meta-analysis on Swish and ReLU Activation Function Families
Analyzing why the Swish activation function family has made accuracy imrpovements over the ReLU activation function family.

## Overview

This can be seen in comparisons of smoothness, self-gatededness, saturation, preconditioning, and empirics. 

### Smoothness Comparisons 

The Swish (left) vs ReLU (right) activation landscapes. 

![silu_landscape](https://github.com/novak-99/ReLU-Family-Swish-Family-Meta-Analysis/assets/78002988/4e1f4c1f-e4ab-4557-8e8f-f39684de5948)
![relu_landscape](https://github.com/novak-99/ReLU-Family-Swish-Family-Meta-Analysis/assets/78002988/cd5d040d-753b-429b-a050-8ca9dd88f1f2)

### Convergence Comparisons

The percentage of times that global optima were attained by Swish and ReLU.

| Number of Layers | Swish | ReLU |
| ------------- |:-------------:| -----:|
| 1 | 60.39% ± 5.00% | 41.02% ± 4.65% |
| 2 | 34.82% ± 5.04% | 20.06% ± 3.99% |
| 3 | 16.92% ± 3.74% | 8.76% ± 2.46% |

### Empirical Comparisons (MNIST)

![mnist_acc](https://github.com/novak-99/ReLU-Family-Swish-Family-Meta-Analysis/assets/78002988/a4f3ac23-2e6d-416e-8866-04030f083191)

## Download 

The paper can be downloaded [here](https://github.com/novak-99/ReLU-Family-Swish-Family-Meta-Analysis/files/13200124/Swish_Fam_vs_ReLU_Fam.pdf).

