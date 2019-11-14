# Elegoo Mars Utility

Simple tool to post-process CBDDLP files from ChiTuBox.

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/E1E2181LU)

## Usage

If you are a Windows user, there pre-built GUI available at the [release
page](https://github.com/yaqwsx/ElegooMarsUtility/releases). Just download it
and run it. There might be a false positive alarm by your anti-virus software.
Please add an exception or follow the installation procedure below (it does not
trigger false positives, however, it is slightly complicated).

If you use Linux, please follow the installation procedure using PIP below.

## Installation

First, you have to install bleeding edge version of the pyphotonfile library as
it has not been published yet in the repository:

```
pip install git+https://github.com/fookatchu/pyphotonfile@master
```

Then you can install the utility by pip

```
pip install ElegooMarsUtility
```

## Usage

The tool has several commands to transform your sliced images. The list of the
commands follows:

## xycompensate

This command can compensate for exposure bleeding and the elephant foot of the
first layers by slightly shrinking the footprint of the layers. The bleeding
leads to slightly larger components (and smaller holes).

Arguments:
- `-c`, `--compensation` - the amount of compensation for regular layers. The
  unit is a single pixel. You have to find the correct amount empirically by
  printing a test object and measuring it
- `-f`, `--firstCompensation` - the amount of compensation for the first layers.
  Argument is the same as in the previous case.
- `-o`, `--output` - filename for the resulting file
- `--debugShow` - shows side by side each compensated layer