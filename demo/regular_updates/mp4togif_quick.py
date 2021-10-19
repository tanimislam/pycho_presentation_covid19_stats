#!/usr/bin/env python3

import os, sys, numpy, logging, time, glob
from pathos.multiprocessing import Pool, ThreadPool, cpu_count
from nprstuff.core.convert_image import mp4togif
from mpi4py import MPI
from argparse import ArgumentParser

def _get_min_time0( ):
    time0_arr = numpy.array([ time.time( ) ])
    time0_min = time0_arr.copy( )
    MPI.COMM_WORLD.Allreduce( time0_arr, time0_min, MPI.MIN )
    return time0_min[ 0 ]

def find_regions_toprocess( region_names, doc_dir_name = 'docs' ):
    assert( os.path.isdir( doc_dir_name ) )
    all_valid_names_dict = dict(
        map(lambda fname:
            ( os.path.basename( fname ).split('_')[1].strip( ), fname ),
            filter(lambda fname: 'deaths' not in fname and 'cases' not in fname,
                   glob.glob( os.path.join( doc_dir_name, 'covid19_*_LATEST.mp4' ) ) ) ) )
    region_names_proc = sorted(
        set( region_names ) & set( all_valid_names_dict ) )
    return list( map(lambda region_name: all_valid_names_dict[ region_name ],
                     region_names_proc ) )

def find_extra_regions_toprocess( region_names, name = 'cases', doc_dir_name = 'docs' ):
    assert( name in ( 'cases', 'deaths' ) )
    all_valid_names_dict = dict(
        map(lambda fname:
            ( os.path.basename( fname ).split('_')[1].strip( ), fname ),
            glob.glob( os.path.join(
                doc_dir_name, 'covid19_*_%s_LATEST.mp4' % name ) ) ) )
    region_names_proc = sorted(
        set( region_names ) & set( all_valid_names_dict ) )
    return list( map(lambda region_name: all_valid_names_dict[ region_name ],
                     region_names_proc ) )

def _scale( region_mp4_file ):
    if 'conus' in os.path.basename( region_mp4_file ): return 0.15
    return 0.3
    
def main( ):
    rank = MPI.COMM_WORLD.Get_rank( )
    time0 = _get_min_time0( )
    parser = ArgumentParser( )
    parser.add_argument( '--region', metavar='region', type=str, nargs='*',
                        help = 'regions to choose to create animated GIFs from MP4 files.' )
    parser.add_argument( '-d', '--dir', dest='dirname', type=str, action='store', default = 'docs',
                        help = 'Name of the directory that has all the COVID-19 summary files. Default is docs.' )
    #
    args = parser.parse_args( )
    dirname = os.path.expanduser( args.dirname )
    assert( os.path.isdir( dirname ) )
    #
    region_mp4_files = find_regions_toprocess( args.region, doc_dir_name = dirname )
    region_mp4_cases_files = find_extra_regions_toprocess(
        args.region, name = 'cases', doc_dir_name = dirname )
    region_mp4_death_files = find_extra_regions_toprocess(
        args.region, name = 'deaths', doc_dir_name = dirname )
    scales = list(map(_scale, region_mp4_files ) )
    scales += [ 1.0 ] * ( len( region_mp4_cases_files ) + len( region_mp4_death_files ) )
    region_mp4_files += region_mp4_cases_files
    region_mp4_files += region_mp4_death_files
    nprocs = min( MPI.COMM_WORLD.Get_size( ), len( region_mp4_files ) )
    if rank >= nprocs: return
    #
    ## now do the thing...
    region_mp4_files_rank = region_mp4_files[rank::nprocs]
    scales_rank = scales[rank::nprocs]
    _ = list(map(lambda tup: mp4togif( tup[0], scale = tup[1] ),
                 zip( region_mp4_files_rank, scales_rank ) ) )
    if rank != 0: return
    print( 'processed all %d MP4 files in %0.3f seconds.' % (
        len( region_mp4_files ), time.time( ) - time0 ) )

if __name__=='__main__':
    main( )
