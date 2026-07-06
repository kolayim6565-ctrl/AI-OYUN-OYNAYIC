[app]
title = Yapay Zeka Oyun Asistanı
package.name = oyunasistani
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3, kivy, opencv-python-headless, numpy
orientation = portrait
osx.kivy_version = 2.1.0
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
services = OyunAsistani:service.py

[buildozer]
log_level = 2
warn_on_root = 1
