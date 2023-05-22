# Tool for modelling magnetic spin waves
Programming project in Advanced Scientific Programming

Magetic waves can be created by interactions between atomistic spin. This tool will model and simulate the behaviour of the magnetic spin waves and how it depend on given parameters

## Theoretical background
In a magentic matrial, each atom generate a magentic moment, also know as a spin. This spin can be described as a vector with a certain magnitude and direction. The atomistic spins in a matrial will interact, where the interaction can be described by a model called the Heisenberg exchange interaction, given by

*likning*

(skrive noe om parameterne)These interactions is the basis of a magnetic spin waves. When the spins are set into motion, the time evolution of the precession can be described by a differential equation called Landau-Lifshitz-Gilbert equation given by

*likning*

where S is the spin vector. To solve this equation, a numerical solver must be implemented. 

## Introductory questions

### Goal of the project
This project will develop a tool tp study how different parameters of the spin configuration affect the magentic wave. The parameters are;
- Heisenberg coupling constant
- Uniaxial anisotropy constant
- Temperature
- Magentic field
Furthermore, the tool will vizualize the beviour of the spin wave

### Potential users of the project
This tool can be used of anyone interessted in physics, and especially within magnetic spin waves. 

### Success of the project
In the end of june, the goal is that the tool will be able to input a set of parameters for the spin system (listed above) and produce a simulation of the spin such that one is able to study the impact of the different paramteres on the system. 


