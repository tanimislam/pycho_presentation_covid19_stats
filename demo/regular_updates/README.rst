.. include:: ../demo_urls.rst

INSTRUCTIONS
==============
This contains example code used by additional executables, in a *currently* private repository, to use nine nodes of a supercomputer to *daily* update the COVID-19 cumulative cases and deaths of 26 regions in the United States. Funny cartoon shown below!

.. image:: https://tanimislam.github.io/covid19_stats/_images/daily_update_five_steps.png
   :width: 100%
   :align: center

There are three files in here.

* ``covid19_movie_updates.bash`` is the main SLURM_ script to update the data. I include the anonymized script code below,

  .. code-block:: console

     #!/bin/bash -l
     #SBATCH --nodes=9
     #SBATCH --partition=PARTITION
     #SBATCH --account=ACCOUNT
     #SBATCH --time=4:00:00
     #SBATCH --job-name="COVID_MOVIE_UPDATES"
     #SBATCH --output="COVID_MOVIE_UPDATES.out"
     #SBATCH --error="COVID_MOVIE_UPDATES.err"
     #SBATCH --comment "just run the problem, see description"

     update_date=$(date +"%d-%m-%Y")
     #
     ## first update database
     covid19_update_database
     #
     ## now generate the COVID-19 cases and deaths, movies and figures, for regions (MSAs, CONUS, states)
     srun -N9 covid19_movie_updates --region nyc bayarea dc richmond losangeles neworleans chicago seattle houston dallas albuquerque newhaven sacramento conus --state California Virginia Texas Florida "New York" Pennsylvania Indiana Michigan Hawaii "New Mexico" "New Jersey" Connecticut --topN=50 --dirname=docs --info
     #
     ## create the GIFs of some regions
     srun -N9 python3 mp4togif_quick.py --region nyc chicago seattle bayarea dc richmond sacramento conus virginia texas florida california -d docs

     #
     ## copy the png, mp4, gifs, json into the website covid19movies, then GIT PUSH
     git stage docs
     git commit -a -m "update of covid19movies at $update_date"
     git push
     #
     ## now update the README.rst, Sphinx, and push up
     /bin/bash covid19_update_docs.bash

  SLURM_ is a job scheduler for supercomputers. To run this command, run it with the sbatch_ command to submit this supercomputing task to the job scheduler,

  .. code-block:: console

     sbatch covid19_movie_updates.bash

* ``covid19_update_docs.bash`` updates `covid19_stats`_\ 's README with the newest COVID-19 data. It is called by ``covid19_movie_updates.bash``. I include the anonymized script below,

  .. code-block:: console

     #!/bin/bash -l

     update_date=$(date +"%d-%m-%Y")
     repodir=REPODIR
     #
     ## now update the README.rst, Sphinx, and push up
     covid19_update_readme -d $repodir -j docs/covid19_topN_LATEST.json
     #
     cwd=$(pwd)
     cd $repodir/docsrc
     make deploy
     cd $cwd
     #
     git -C $repodir pull
     git -C $repodir stage README.rst docs docsrc
     git -C $repodir commit -a -m "update README.rst and Sphinx at $update_date."
     git -C $repodir push

* ``mp4togif_quick.py`` uses mp4togif_ at a low level to create `animated GIF`_\ s of 12 regions.
