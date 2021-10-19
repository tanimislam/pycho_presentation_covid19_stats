.. include:: ../demo_urls.rst

INSTRUCTIONS
=============
This consists of four sections, and instructions to generate the COVID-19 cumulative case and death summary figures and incident data, and MP4_ movies, for the |conus|. I assume that you have `installed covid19_stats <https://tanimislam.github.io/covid19_stats/installation.html>`_ and updated the COVID-19 database by running,

.. code-block:: console

   covid19_update_database

We generate the figures, incident data, and MP4_ movies by running `covid19_create_movie_or_summary <https://tanimislam.github.io/covid19_stats/cli/covid19_create_movie_or_summary.html>`_. Its main help screen is,

.. code-block:: console

   usage: covid19_create_movie_or_summary [-h] [-d DIRNAME] [--info] {M,m,s,mcd} ...

   positional arguments:
     {M,m,s,mcd}           Choose one of three options: (M) summarizes stats from metros; (m) make a movie of a metro region; and
			   (s) dumps summary plots of last incident date, and cumulative covid-19 stats, of a metro region.
       M                   If chosen, then list all the metropolitan areas through which we can look.
       m                   Make a movie of the COVID-19 cases and deaths trend for the specific Metropolitan Statistical Area
			   (MSA).
       s                   Make a summary plot, and incident data file, of COVID-19 cases and deaths trend, for the specific
			   Metropolitan Statistical Area (MSA).
       mcd                 Make a large-sized movie of either "CASES" or "DEATHS" for given MSA or CONUS.

   optional arguments:
     -h, --help            show this help message and exit
     -d DIRNAME, --dirname DIRNAME
			   The directory into which to store the resulting files. Default is /usr/WS2/islam5/covid19_data/nyc.
     --info                If chosen, then print out INFO level logging statements.

Here are the four demonstrations.

summary
----------
Run this command,

.. code-block:: console

   covid19_create_movie_or_summary s --conus -y

This generates these *seven* files.

.. list-table::
   :widths: auto

   * - FILE GENERATED
     - WHAT IT IS
   * - ``covid19_conus_LATEST.pkl.gz``
     - Serialized incident data for COVID-19 cases for the |conus|. See `get_incident_data <https://tanimislam.github.io/covid19_stats/api/api.html?highlight=get_incident_data#covid19_stats.engine.core.get_incident_data>`_ to see the structure of this data.
   * - ``covid19_conus_cases_LATEST.png``
     - The cumulative *latest* COVID-19 cases for the |conus| as a PNG_.
   * - ``covid19_conus_cases_LATEST.pdf``
     - The cumulative *latest* COVID-19 cases for the |conus| as a PDF_.
   * - ``covid19_conus_death_LATEST.png``
     - The cumulative *latest* COVID-19 deaths for the |conus| as a PNG_.
   * - ``covid19_conus_death_LATEST.pdf``
     - The cumulative *latest* COVID-19 deaths for the |conus| as a PDF_.
   * - ``covid19_conus_cds_LATEST.png``
     - The plot showing the cumulative COVID-19 cases and deaths for the |conus| as a PNG_.
   * - ``covid19_conus_cds_LATEST.pdf``
     - The plot showing the cumulative COVID-19 cases and deaths for the |conus| as a PDF_.

cases
------
Run this command,

.. code-block:: console

   covid19_create_movie_or_summary mcd --conus -d cases -y

This generates ``covid19_conus_cases_LATEST.mp4``, an MP4_ movie of the COVID-19 trend of cases for the |conus|. If you have mp4info_, you see it has this metadata,

.. code-block:: console

   mp4info version 2.0.0
   covid19_conus_cases_LATEST.mp4:
   Track   Type    Info
   1       video   H264 High@4.2, 80.600 secs, 380 kbps, 2010x1056 @ 5.000000 fps
    Name: conus, CASES, 26-02-2021
    Artist: Tanim Islam
    Encoded with: Lavf57.56.101
    Release Date: 26-02-2021
    Album: CONUS

deaths
-------
Run this command,

.. code-block:: console

   covid19_create_movie_or_summary mcd --conus -d deaths -y

This generates ``covid19_conus_deaths_LATEST.mp4``, an MP4_ movie of the COVID-19 trend of deaths for the |conus|. If you have mp4info_, you see it has this metadata,

.. code-block:: console

   mp4info version 2.0.0
   covid19_conus_deaths_LATEST.mp4:

   Track   Type    Info
   1       video   H264 High@4.2, 80.600 secs, 279 kbps, 2010x1056 @ 5.000000 fps
    Name: conus, DEATHS, 26-02-2021
    Artist: Tanim Islam
    Encoded with: Lavf57.56.101
    Release Date: 26-02-2021
    Album: CONUS

quad
------
I call this *quad* because this movie has four quadrants: summary on upper left, animated trend lines of cases and deaths on lower left, animation of cumulative cases on lower right, and animation of cumulative deaths on upper right.

Run this command,

.. code-block:: console

   covid19_create_movie_or_summary m --conus -y

This generates ``covid19_conus_LATEST.mp4``, an MP4_ *quad* movie of the COVID-19 trend of cases and deaths for the |conus|. If you have mp4info_, you see it has this metadata,

.. code-block:: console

   mp4info version 2.0.0
   covid19_conus_LATEST.mp4:
   Track   Type    Info
   1       video   H264 High@5, 80.600 secs, 270 kbps, 1908x1166 @ 5.000000 fps
    Name: conus, ALL, 26-02-2021
    Artist: Tanim Islam
    Encoded with: Lavf57.56.101
    Release Date: 26-02-2021
    Album: CONUS
