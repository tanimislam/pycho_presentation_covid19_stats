README: Working on Creating Movies from region
===============================================
Step #1: creating the Blue Ridge Health District (BRHD) health region.

.. code-block:: console

   covid19_create_region -c Charlottesville Albemarle Nelson Greene Louisa Fluvanna -s Virginia -p brhd -n "Blue Ridge Health District"

This will create ``brhd.json`` when you choose ``y`` at the prompt.

Step #2: now create the collection of images (PNG and PDF) and movies.

.. code-block:: console

   srun -N4 covid19_region_updates -r brhd.json -i

There are *eighteen* files that are created.


