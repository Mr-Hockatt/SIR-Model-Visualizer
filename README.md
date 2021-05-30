# SIR-Model-Visualizer
Covid-19 SIR Model Visualizer with modifiable parameters such as recovery rate, infection rate and initial infected population.</br>
This project was created as part of my <b>Mathematical Methods</b> class on my 4th semester of Mechatronics Engineering.


![model_graph](https://user-images.githubusercontent.com/53312754/120086451-acba6b80-c0a4-11eb-9cd0-52b4c8b3465a.png)

## Features
<ul>
  <li>Numerical solution of the SIR model by Runge Kutta integration method</li>
  <li>Modifiable parameters (recovery rate, infection rate, initial infected population)</li>
  <li>Numerical Solution of the SIR model with the given parameters</li>
  <li>Data visualization of the model solution (S, I and R curves)</li>
  <li>Table presentation of the numerical solution</li>
  <li>CSV storage of the numerical solution</li>
</ul>

The main window is a simple GUI created with Tkinter and the plotting happens with Matplotlib

![gui](https://user-images.githubusercontent.com/53312754/120086455-bb088780-c0a4-11eb-9ef6-8d604231522d.jpg)

The table shows a preview of the numerical solution of the SIR model. Complete data is stored on a .csv file for whatever purposes needed.

![calculation_table](https://user-images.githubusercontent.com/53312754/120086717-0459d680-c0a7-11eb-8fb6-8f610789f635.jpg)

## Requirements
<ul>
  <li><b>CSV</b></li>
  <li><b>Drawnow</b> for graphing purposes.</li>
  <li><b>Matplotlib</b></li>
  <li><b>Numpy</b></li>
  <li><b>PIL</b> (Python Imaging Library)</li>
  <li><b>Threading</b></li>
  <li><b>Tkinter</b></li>
</ul>

## Keep in mind (Disclaimer)
Although this project was made for Russia's population (approximately 146M at the time of making) this parameter can be easily modified in the <b>Main Program.py</b> file, line 114 under the variable <b>N</b>. The rest stays the same and works fine.
