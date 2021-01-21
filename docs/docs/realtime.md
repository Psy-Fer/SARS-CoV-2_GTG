# Real-time monitoring

Using RAMPART, we can monitor the sequencing depth in real time for each sample across all amplicons.

This allows the user to know when they have enough depth and coverage, and stop the run, for rapid turn around times, and for re-using flowcells.

The documentation for RAMPART is located here:

**RAMPART: [artic-network/rampart](https://github.com/artic-network/rampart)**

Here is how we set it up and run it for modified protocols.

### Installation

Please see Intallation page for conda and repository setup.

For use, please refer to the relevent protocol.

## Protocol files

### ARTIC V3

Each protocol with different primer/amplicon sets, will need their own configuration files to work with RAMPART (and the ARTIC analysis pipeline too).

For RAMPART, the default files for artic V3 files are located in (path depends on install location of ncov2019 git)

    --protocol ~/artic-ncov2019/rampart/

it contains the following files:

    genome.json
    primers.json
    protocol.json
    README.md
    references.fasta

If the reference is the same as used here, then you can simply copy genome.json references.fasta to your new protocol folder. Otherwise you will need to build these yourself. (shoot me a message and I can help)

for primers.json, copy the main structure, but replace the values with your amplicon [start,stop] positions

    {
    "name": "nCoV2019 primer scheme v1.0",
    "amplicons": [
        [30, 410],
        [320, 726],
        [642, 1028],
        [943, 1337],
        [1242, 1651],
        [1573, 1964],
        [1875, 2269],
        ...

Notice that each primer is overlapping a bit here, so you are placing them as A/B/A/B or 1/2/1/2...

The protocol.json is where you can place some information about the protocol and various thresholds for depth/coverage

    {
    "name": "ARTIC nCoV2019 protocol v1.0",
    "description": "Amplicon based sequencing of novel coronavirus 2019 (nCoV2019).",
    "url": "http://artic.network/",
    "displayOptions": {
        "coverageThresholds": {
            ">200x": 200, ">100x": 100, ">20x": 20, "0x": 0
            }
        }
    }

### Eden 2.5kb

Download RAMPART protocol files

    cd
    git clone https://github.com/Psy-Fer/SARS-CoV-2_GTG.git

protocol located in

    --protocol ~/SARS-CoV-2_GTG/protocols/Kirby/V1/




### Midnight 1.2kb

Download RAMPART protocol files (similar to Eden method above)

    cd
    git clone https://github.com/Psy-Fer/SARS-CoV-2_GTG.git

protocol located in

    --protocol ~/SARS-CoV-2_GTG/protocols/Midnight/V1/


## Experiment files

Two fies are needed for any experiment.

`run_configuration.json` and `cmd.txt`

### run_configuration.json


A title, followed by details for each sample.

For **ALL** protocols with **Native** barcodes, it would look something like this:

    {
      "title": "SARS-CoV-2 kirby_artic-4 nCoV_694,699,706,707,711,712,690,708,660,673,NegRT",
      "samples": [
        {
          "name": "nCoV_694",
          "description": "",
          "barcodes": [ "NB01" ]
        },
        {
          "name": "nCoV_699",
          "description": "",
          "barcodes": [ "NB02" ]
        },
        {
          "name": "nCoV_706",
          "description": "",
          "barcodes": [ "NB03" ]
        },
        {
          "name": "nCoV_707",
          "description": "",
          "barcodes": [ "NB04" ]
        },
        {
          "name": "nCoV_711",
          "description": "",
          "barcodes": [ "NB05" ]
        },
        {
          "name": "nCoV_712",
          "description": "",
          "barcodes": [ "NB06" ]
        },
        {
          "name": "nCoV_690",
          "description": "",
          "barcodes": [ "NB07" ]
        },
        {
          "name": "nCoV_708",
          "description": "",
          "barcodes": [ "NB08" ]
        },
        {
          "name": "nCoV_660",
          "description": "",
          "barcodes": [ "NB09" ]
        },
        {
          "name": "nCoV_673",
          "description": "",
          "barcodes": [ "NB10" ]
        },
        {
          "name": "nCoV_NegRT",
          "description": "",
          "barcodes": [ "NB11" ]
        }
      ]
    }


for For **ALL** protocols with **Rapid** barcodes, it would look something like this:


    {
      "title": "SARS-CoV-2 kirby-41",
      "samples": [
        {
          "name": "nCoV_1634",
          "description": "",
          "barcodes": [ "BC01" ]
        },
        {
          "name": "nCoV_1646",
          "description": "",
          "barcodes": [ "BC02" ]
        },
        {
          "name": "nCoV_1645",
          "description": "",
          "barcodes": [ "BC03" ]
        },
        {
          "name": "nCoV_1628",
          "description": "",
          "barcodes": [ "BC04" ]
        },
        {
          "name": "nCoV_1664",
          "description": "",
          "barcodes": [ "BC05" ]
        },
        {
          "name": "nCoV_1644",
          "description": "",
          "barcodes": [ "BC06" ]
        },
        {
          "name": "nCoV_1641",
          "description": "",
          "barcodes": [ "BC07" ]
        },
        {
          "name": "nCoV_1638",
          "description": "",
          "barcodes": [ "BC08" ]
        },
        {
          "name": "nCoV_1642",
          "description": "",
          "barcodes": [ "BC09" ]
        },
        {
          "name": "nCoV_1647",
          "description": "",
          "barcodes": [ "BC10" ]
        },
        {
          "name": "nCoV_1648",
          "description": "",
          "barcodes": [ "BC11" ]
        }

      ]
    }


for For **ALL** protocols with **ONE SAMPLE**/NO barcodes, it would look something like this:

    {
      "title": "SARS-CoV-2 kirby-47"
    }


### cmd.txt

This file is just a text file to keep track of the command being run.

You need to parse the `fastq_pass` folder to RAMPART.

For **ARTIC** with **NATIVE** barcodes:

    rampart --verbose --protocol ~/artic-ncov2019/rampart/ --ports 4010 4011 --basecalledPath /data/PLPL172071/Kirby_ARTIC_V3_690-712/20200828_0046_1C_PAF09161_1c3442d1/fastq_pass/


for **Eden** with **NATIVE** barcodes:

    rampart --verbose --protocol ~/SARS-CoV-2_GTG/protocols/Kirby/V1/ --ports 4010 4011 --basecalledPath /data/PLPL172071/Kirby_ARTIC_V3_690-712/20200828_0046_1C_PAF09161_1c3442d1/fastq_pass/


for **Midnight** with **NATIVE** barcodes:

    rampart --verbose --protocol ~/SARS-CoV-2_GTG/protocols/Midnight/V1/ --ports 4010 4011 --basecalledPath /data/PLPL172071/Kirby_ARTIC_V3_690-712/20200828_0046_1C_PAF09161_1c3442d1/fastq_pass/


for **Eden** with **RAPID** barcodes:

it's the same as above, but with added flags to parse through to porechop
`--annotationOptions require_two_barcodes="False" barcode_set="rapid"`

    rampart --verbose --protocol /home/prom/SARS-CoV-2_GTG/protocols/Kirby/V1/ --ports 4010 4011 --basecalledPath /data/PQPR302183/kirby_artic_2/20201218_0548_1G_PAF28510_509ee0c7/fastq_pass/ --annotationOptions require_two_barcodes="False" barcode_set="rapid"


for **Midnight** with **RAPID** barcodes:

    rampart --verbose --protocol /home/prom/SARS-CoV-2_GTG/protocols/Midnight/V1/ --ports 4010 4011 --basecalledPath /data/PQPR302183/kirby_artic_2/20201218_0548_1G_PAF28510_509ee0c7/fastq_pass/ --annotationOptions require_two_barcodes="False" barcode_set="rapid"


If you have a single sample with no barcoding, use the matching protocol, but the results will be in the "unassigned" group within RAMPART


Executing the commands with & and screen is advised. (see tutorial for more information)
