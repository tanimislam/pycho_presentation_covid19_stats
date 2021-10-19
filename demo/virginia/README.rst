.. include:: ../demo_urls.rst

INSTRUCTIONS
=============
This consists of four sections, and instructions to generate the COVID-19 cumulative case and death summary figures and incident data, and MP4_ movies, for |virginia|. I assume that you have `installed covid19_stats <https://tanimislam.github.io/covid19_stats/installation.html>`_ and updated the COVID-19 database by running,

.. code-block:: console

   covid19_update_database

We generate the figures, incident data, and MP4_ movies by running `covid19_state_summary <https://tanimislam.github.io/covid19_stats/cli/covid19_state_summary.html>`_. Its main help screen is,

.. code-block:: console

   usage: covid19_state_summary [-h] [-d DIRNAME] [--info]
				[-n {Alabama,Alaska,Arizona,Arkansas,California,Colorado,Connecticut,Delaware,District of Columbia,Florida,Georgia,Hawaii,Idaho,Illinois,Indiana,Iowa,Kansas,Kentucky,Louisiana,Maine,Maryland,Massachusetts,Michigan,Minnesota,Mississippi,Missouri,Montana,Nebraska,Nevada,New Hampshire,New Jersey,New Mexico,New York,North Carolina,North Dakota,Ohio,Oklahoma,Oregon,Pennsylvania,Puerto Rico,Rhode Island,South Carolina,South Dakota,Tennessee,Texas,Utah,Vermont,Virginia,Washington,West Virginia,Wisconsin,Wyoming}]
				[-M MAXNUM] [-y]
				{m,s,mcd} ...

   positional arguments:
     {m,s,mcd}             Choose one of three options: (m) make a movie of the COVID-19 cumulative stats for the state; (s) dumps summary plots of last incident date, and cumulative covid-19
			   stats, of a state; and (mcd) make a movie of either "CASES" or "DEATHS" in the state.
       m                   Make a movie of the COVID-19 cases and deaths trend for the specific state.
       s                   Make a summary plot, and incident data file, of COVID-19 cases and deaths trend, for the specific state.
       mcd                 Make a large-sized movie of either "CASES" or "DEATHS" for given state.

   optional arguments:
     -h, --help            show this help message and exit
     -d DIRNAME, --dirname DIRNAME
			   The directory into which to store the resulting files. Default is /g/g12/islam5/.local/src/covid19_stats/docsrc.
     --info                If chosen, then print out INFO level logging statements.
     -n {Alabama,Alaska,Arizona,Arkansas,California,Colorado,Connecticut,Delaware,District of Columbia,Florida,Georgia,Hawaii,Idaho,Illinois,Indiana,Iowa,Kansas,Kentucky,Louisiana,Maine,Maryland,Massachusetts,Michigan,Minnesota,Mississippi,Missouri,Montana,Nebraska,Nevada,New Hampshire,New Jersey,New Mexico,New York,North Carolina,North Dakota,Ohio,Oklahoma,Oregon,Pennsylvania,Puerto Rico,Rhode Island,South Carolina,South Dakota,Tennessee,Texas,Utah,Vermont,Virginia,Washington,West Virginia,Wisconsin,Wyoming}
			   Make movies or other summary data for a state. Default is "New York".
     -M MAXNUM, --maxnum MAXNUM
			   The limit of cases/deaths to visualize. Default is a plausible amount for the chosen state. You should use a limit larger (by at least 2, no more than 10) than the
			   maximum number of cases recorded for a county in that state.
     -y, --yes             If chosen, then do not confirm --maxnum.

Here are the four demonstrations.

summary
----------
Run this command,

.. code-block:: console

   covid19_state_summary -n Virginia -y s

This generates these *seven* files.

.. list-table::
   :widths: auto

   * - File GENERATED
     - WHAT IT IS
   * - ``covid19_virginia_LATEST.pkl.gz``
     - Serialized incident data for COVID-19 cases for |virginia|. See `get_incident_data <https://tanimislam.github.io/covid19_stats/api/api.html?highlight=get_incident_data#covid19_stats.engine.core.get_incident_data>`_ to see the structure of this data.
   * - ``covid19_virginia_cases_LATEST.png``
     - The cumulative *latest* COVID-19 cases for |virginia| as a PNG_.
   * - ``covid19_virginia_cases_LATEST.pdf``
     - The cumulative *latest* COVID-19 cases for |virginia| as a PDF_.
   * - ``covid19_virginia_death_LATEST.png``
     - The cumulative *latest* COVID-19 deaths for |virginia| as a PNG_.
   * - ``covid19_virginia_death_LATEST.pdf``
     - The cumulative *latest* COVID-19 deaths for |virginia| as a PDF_.
   * - ``covid19_virginia_cds_LATEST.png``
     - The plot showing the cumulative COVID-19 cases and deaths for |virginia| as a PNG_.
   * - ``covid19_virginia_cds_LATEST.pdf``
     - The plot showing the cumulative COVID-19 cases and deaths for |virginia| as a PDF_.

cases
------
Run this command,

.. code-block:: console

   covid19_state_summary -n virginia -y  mcd -n richmond -d cases

This generates ``covid19_virginia_cases_LATEST.mp4``, an MP4_ movie of the COVID-19 trend of cases for |virginia|. If you have mp4info_, you see it has this metadata,

.. code-block:: console

   mp4info version 2.0.0
   covid19_virginia_cases_LATEST.mp4:
   Track   Type    Info
   1       video   H264 High@4, 71.400 secs, 214 kbps, 2010x858 @ 5.000000 fps
    Name: virginia, CASES, 26-02-2021
    Artist: Tanim Islam
    Encoded with: Lavf57.56.101
    Release Date: 26-02-2021
    Album: STATE

deaths
-------
Run this command,

.. code-block:: console

   covid19_state_summary -n Virginia -y mcd -d deaths

This generates ``covid19_virginia_deaths_LATEST.mp4``, an MP4_ movie of the COVID-19 trend of deaths for |virginia|. If you have mp4info_, you see it has this metadata,

.. code-block:: console

   mp4info version 2.0.0
   covid19_virginia_deaths_LATEST.mp4:
   Track   Type    Info
   1       video   H264 High@4, 71.400 secs, 141 kbps, 2010x858 @ 5.000000 fps
    Name: virginia, DEATHS, 26-02-2021
    Artist: Tanim Islam
    Encoded with: Lavf57.56.101
    Release Date: 26-02-2021
    Album: STATE

quad
------
I call this *quad* because this movie has four quadrants: summary on upper left, animated trend lines of cases and deaths on lower left, animation of cumulative cases on lower right, and animation of cumulative deaths on upper right.

Run this command,

.. code-block:: console

   covid19_state_summary -n Virginia -y m

This generates ``covid19_virginia_LATEST.mp4``, an MP4_ *quad* movie of the COVID-19 trend of cases and deaths for |virginia|. If you have mp4info_, you see it has this metadata,

.. code-block:: console

   mp4info version 2.0.0
   covid19_virginia_LATEST.mp4:
   Track   Type    Info
   1       video   H264 High@5, 71.400 secs, 221 kbps, 2156x1166 @ 5.000000 fps
    Name: virginia, ALL, 26-02-2021
    Artist: Tanim Islam
    Encoded with: Lavf57.56.101
    Release Date: 26-02-2021
    Album: STATE
