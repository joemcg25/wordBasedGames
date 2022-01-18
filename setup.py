#Describes the metadata about your package#
import setuptools
setuptools.setup(
    name="wordBasedGames",
    version="1.0.0",
    description="Games with words",
    packages=setuptools.find_packages("src"),
    package_dir={'':"src"})