"""
Credit to https://gist.github.com/ian-whitestone/a3452fe38fda9025631045381a18a6df
Read accompanying blog post: https://ianwhitestone.work/Zappa-Zip-Callbacks
"""
import os
import re
import shutil
import tarfile
import zipfile


def remake_archive(temp_unarchive_path, archive_path, archive_format, excludes):
    """Re-create the archive using the list of regex excludes. Modified from
    zappa's core.py:
    https://github.com/Miserlou/Zappa/blob/746385d9483a536b6c363bab0a15fec1d27818e7/zappa/core.py#L690-L759

    Args:
        temp_unarchive_path (str): Full path to dir with unarchived contents
        archive_path (str): Full path to the archive file to create
        archive_format (str): type of archive...must be zip or tarball
        excludes (list): list of regex patterns for files to exclude
    """

    if archive_format == "zip":
        print("Re-packaging project as zip.")

        try:
            compression_method = zipfile.ZIP_DEFLATED
        except ImportError:  # pragma: no cover
            compression_method = zipfile.ZIP_STORED
        archivef = zipfile.ZipFile(archive_path, "w", compression_method)
    elif archive_format == "tarball":
        print("Re-packaging project as gzipped tarball.")
        archivef = tarfile.open(archive_path, "w|gz")

    for root, dirs, files in os.walk(temp_unarchive_path):

        for filename in files:

            filepath = os.path.join(root, filename)
            if any(re.search(exclude_regex, filepath) for exclude_regex in excludes):
                continue

            # Make sure that the files are all correctly chmodded
            # Related: https://github.com/Miserlou/Zappa/issues/484
            # Related: https://github.com/Miserlou/Zappa/issues/682
            os.chmod(filepath, 0o755)

            if archive_format == "zip":
                # Actually put the file into the proper place in the zip
                # Related: https://github.com/Miserlou/Zappa/pull/716
                zipi = zipfile.ZipInfo(
                    os.path.join(
                        root.replace(temp_unarchive_path, "").lstrip(os.sep), filename
                    )
                )
                zipi.create_system = 3
                zipi.external_attr = 0o755 << int(16)  # Is this P2/P3 functional?
                with open(filepath, "rb") as f:
                    archivef.writestr(zipi, f.read(), compression_method)
            elif archive_format == "tarball":
                tarinfo = tarfile.TarInfo(
                    os.path.join(
                        root.replace(temp_unarchive_path, "").lstrip(os.sep), filename
                    )
                )
                tarinfo.mode = 0o755

                stat = os.stat(filepath)
                tarinfo.mtime = stat.st_mtime
                tarinfo.size = stat.st_size
                with open(os.path.join(root, filename), "rb") as f:
                    archivef.addfile(tarinfo, f)

    archivef.close()


def unpack_archive(source, destination):
    print(f"Unpacking {source} to {destination}")
    shutil.unpack_archive(source, destination)


def main(zappa):
    """Clean up zappa package before deploying to AWS

    Args:
        zappa (ZappaCLI): ZappaCLI object from zappa/cli.py. Automatically
            gets passed in by callback initiation:
            https://github.com/Miserlou/Zappa/blob/746385d9483a536b6c363bab0a15fec1d27818e7/zappa/cli.py#L1939-L1980
    """
    print("Running zappa package cleaner")

    zip_filename = zappa.zip_path
    stage_settings = zappa.zappa_settings.get(zappa.api_stage, {})
    excludes = stage_settings.get("regex_excludes", None)
    if not excludes:
        raise Exception(f"No regex_excludes provided for stage: {zappa.api_stage}")

    if zip_filename.endswith(".tar.gz"):
        archive_format = "tarball"
        extension = ".tar.gz"
    elif zip_filename.endswith(".zip"):
        archive_format = "zip"
        extension = ".zip"
    else:
        raise Exception("Archive extension must be .zip or .tar.gz")

    zip_filepath = os.path.join(os.getcwd(), zip_filename)
    temp_unarchive_path = os.path.join(os.getcwd(), zip_filename.replace(extension, ""))

    unpack_archive(zip_filepath, temp_unarchive_path)
    remake_archive(temp_unarchive_path, zip_filepath, archive_format, excludes)
    print(f"Removing {temp_unarchive_path}")
    shutil.rmtree(temp_unarchive_path)