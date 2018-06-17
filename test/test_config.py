#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import stat


def test_dl_path_invalid_program_exit():
    # Note: we assume that the download path as set in the settings doesn't
    # exist yet.
    process = subprocess.run(["python3", "hb-downloader.py"])
    assert process.returncode != 0, (
            "hb-downloader.py did not exit when an invalid download location "
            "was supplied")


def test_dl_path_validation():
    download_location = "./dl-folder"
    from humble_downloader.config_data import ConfigData
    from humble_downloader.configuration import Configuration
    Configuration.load_configuration("hb-downloader-settings.yaml")
    ConfigData.download_location = download_location
    validation_status, message = Configuration.validate_configuration()
    assert not validation_status, (
            "validate_configuration did not fail when download folder did "
            "not exist")
    os.makedirs(download_location)
    os.chmod(download_location, 0)
    validation_status, message = Configuration.validate_configuration()
    assert not validation_status, (
            "validate_configuration did not fail when download folder had "
            "wrong permissions")
    os.chmod(download_location, stat.S_IRUSR | stat.S_IWUSR)
    validation_status, message = Configuration.validate_configuration()
    assert not validation_status, (
            "default configuration invalid after setting up download folder")
    os.rmdir(download_location)
