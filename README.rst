COVID19_Stats: Experiences Visualizing and Deploying Data from the NY Times COVID-19 Database
===============================================================================================
Here, I present a regular update work flow, compiling and updating summary COVID-19 cases and deaths, animations and figures, for 26 US regions (metropolitan statistical areas, states, and CONUS).

The repos are in Google Colab Jupyter notebooks, here:

* `MSA cases and deaths <https://colab.research.google.com/drive/1yBs35ikyNMvuP2kEx1FDIgTO-Zsselhy?usp=sharing>`_.

* `state and CONUS cases and deaths <https://colab.research.google.com/drive/11Mhwu3Gj3VVQEpLzlZVCclMmn5Nx3YJL?usp=sharing>`_.

Demonstrations live in the ``demo`` subdirectory. each demonstration is its own directory within ``demo``, and each demonstration has its own ``README.rst``. Here are the three directories with description.

1. ``richmond``: demonstration of COVID-19 cases and deaths output for the `Richmond, VA, MSA <https://en.wikipedia.org/wiki/Richmond,_Virginia>`_.

2. ``virginia``: demonstration of COVID-19 cases and deaths output for `Virginia <https://en.wikipedia.org/wiki/Virginia>`_.

3. ``conus``: demonstration of COVID-19 cases and deaths output for the `CONUS <https://en.wikipedia.org/wiki/Contiguous_United_States>`_.

4. ``regular_updates``: example scripts that describe a work flow where I use 9 nodes to *daily* update the COVID-19 case and death summaries of 26 regions in the United States.

A *new* subdirectory, ``brhd``, demonstrates new functionality to create summary COVID-19 visualizations for a custom region. The demonstration region is the ``Blue Ridge Health District``, and contains these six counties:

* Charlottesville

* Albemarle County

* Nelson County

* Greene County

* Louisa County

* Fluvanna County
   
You can generate the ``README.html`` from the ``README.rst`` in each of the demonstration subdirectories by running this command,

.. code-block:: console

   rst2html README.rst > README.html

