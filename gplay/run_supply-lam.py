#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os, os.path

cmd = 'fastlane supply -j ../../lam-ho-77ce15030701.json -a beta -p com.senspark.goldminerclassic --skip_upload_apk true --skip_upload_images true --skip_upload_screenshots true'
print cmd
os.system(cmd)