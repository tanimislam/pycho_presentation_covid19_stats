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
