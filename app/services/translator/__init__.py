"""Initializes the translater. it downloads and installs the model used for translation."""


import argostranslate.package


argostranslate.package.update_package_index()

av_packages = argostranslate.package.get_available_packages()

for pair in av_packages:
    if pair.from_code == "de" and pair.to_code == "en":
        package = pair
        argostranslate.package.install_from_path(package.download())
        break
