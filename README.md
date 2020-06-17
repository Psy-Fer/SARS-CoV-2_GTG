# SARS-CoV-2_GTG
Genomic Tech's COVID sequencing

This is a living git, that will change over time as we test out various methods.
We are mostly using a 14 primer scheme, which requires some changes to the artic protocol

Also included are some handy commands for running analyses on multiple barcodes at once.
We are doing both nanopolish and medaka for all runs. So far, so good.

Please let me know if anything is unclear, or you have suggestions or questions.


## Making custom primer scheme

Working from the original artic-network protocol, we need TWO folders of files.
The first, is the protocol folder, in this case `protocols/Kirby/V1`
The second, is the schemes folder, in this case `protocols/Kirby/schemes/nCoV-2019/V1`

The First, is used with RAMPART in order to align and display the data with your custom primer set.

The second, is used with the artic bioinformatic analysis SOP after sequencing.

#### Building the RAMPART protocol

If the reference is the same as used here, then you can simply copy
`genome.json`
`references.fasta`
to your new protocol folder. Otherwise you will need to build these yourself.
(shoot me a message and I can help)

for `primers.json`, copy the main structure, but replace the values with your amplicon [start,stop] positions

```
"amplicons": [
    [31, 2592],
    [1876, 4450],
    [4295, 6873],
    ...
```

Notice that each primer is overlapping a bit here, so you are placing them as A/B/A/B or 1/2/1/2...

The protocol.json is where you can place metadata for the run. I simply use this to name it.
Fill in as you please

#### Building the artic protocol

Again, if the reference is the same, nothing needs to be changed for
`nCoV-2019.reference.fasta` file

Then, if your primer bed file looks like This

```
MN908947.3	31	2592	A1
MN908947.3	1876	4450	B1
MN908947.3	4295	6873	A2
MN908947.3	6287	8851	B2
MN908947.3	8596	11074	A3
MN908947.3	10363	12802	B3
MN908947.3	12711	15246	A4
MN908947.3	14546	17152	B4
MN908947.3	16847	19278	A5
MN908947.3	18897	21455	B5
MN908947.3	21358	23847	A6
MN908947.3	23123	25673	B6
MN908947.3	25602	28172	A7
MN908947.3	27447	29866	B7


```

Then your `nCoV-2019.scheme.bed` looks like this:

```
MN908947.3	31	54	nCoV-2019_1_LEFT	nCoV-2019_1
MN908947.3	2569	2592	nCoV-2019_1_RIGHT	nCoV-2019_1
MN908947.3	1876	1897	nCoV-2019_2_LEFT	nCoV-2019_2
MN908947.3	4429	4450	nCoV-2019_2_RIGHT	nCoV-2019_2
MN908947.3	4295	4321	nCoV-2019_3_LEFT	nCoV-2019_1
MN908947.3	6847	6873	nCoV-2019_3_RIGHT	nCoV-2019_1
MN908947.3	6287	6310	nCoV-2019_4_LEFT	nCoV-2019_2
MN908947.3	8828	8851	nCoV-2019_4_RIGHT	nCoV-2019_2
...
```
Where you count up each pair in the 4th column, and 1 and 2 stand in for A and B in the 5th column.

(Let me know if this isn't clear, or you have a better way of explaining it)


## RAMPART

RAMPART version in artic protocol doesn't have remote browser fix
Use RAMPART install for v1.1

### Native barcodes

NB01, NB02, etc...

```
rampart --verbose --protocol /home/grid/SARS-CoV-2_GTG/protocols/Kirby/V1/ --ports 3000 3001 --basecalledPath /data/name/name/20200330_0557_X2_ACW369_55e7e4ce/fastq_pass/
```

### Rapid barcodes

BC01, BC02, etc...

```
rampart --verbose --protocol /home/grid/SARS-CoV-2_GTG/protocols/Kirby/V1/ --ports 5000 5001 --basecalledPath /data/name/name/20200401_0106_X5_ACL109_433d9d25/fastq_pass/ --annotationOptions require_two_barcodes="False" barcode_set="rapid"

```


## Analysis

### Nanopolish

```
conda activate artic-ncov2019

mkdir asm
cd asm

artic gather --min-length 2300 --max-length 2700 --prefix name --directory /data/name/name/20200330_0557_X2_ACW369_55e7e4ce/

artic demultiplex --threads 4 name_fastq_pass.fastq

cd ..

for bc in {01..09}; do mkdir barcode${bc}; cd barcode${bc}; artic minion --normalise 200 --threads 4 --scheme-directory ~/SARS-CoV-2_GTG/protocols/Kirby/schemes --read-file ../asm/name_fastq_pass-NB${bc}.fastq --fast5-directory ../fast5_pass --sequencing-summary ../asm/name_sequencing_summary.txt nCoV-2019/V1 name; cd ../;  done


```

### Under development
#### Rapid barcodes

This is still in testing, use native barcodes

```

porechop --verbosity 2 --untrimmed -i "name_fastq_pass.fastq" -b ./ --rapid_barcodes --discard_middle --barcode_threshold 80 --threads 4 --check_reads 10000 --barcode_diff 5 > name_fastq_pass.fastq.demultiplexreport.txt

for file in BC*.fastq; do mv $file name_fastq_pass-${file}; done

```


### Medaka

```
conda activate artic-ncov2019-medaka

mkdir asm

# directory is an example, but should point to the folder with the sequencing_summary.txt

artic gather --min-length 2300 --max-length 2700 --prefix name --directory /data/name/name/20200330_0557_X2_ACW369_55e7e4ce/

artic demultiplex --threads 4 name_fastq_pass.fastq

cd ..

for bc in {01..09}; do mkdir barcode${bc}; cd barcode${bc}; artic minion --minimap2 --medaka --normalise 200 --threads 4 --scheme-directory ~/SARS-CoV-2_GTG/protocols/Kirby/schemes --read-file ../asm/name_fastq_pass-NB${bc}.fastq nCoV-2019/V1 name; cd ../; done

```



### Comparing references

Checking the reference used is the same, and if not, how they differ

```
pip3 install edlib

python3 compare_ref.py -r1 base_reference.fasta -r2 new_reference.fasta
```

# Scratch space


New commands - experimental

    artic gather --min-length 300 --max-length 2700 --prefix PQPR071978 --directory /data/PQPR071978/20200527_0703_3D_PAE51904_eb3de804/ --fast5-directory /data/PQPR071978/20200527_0703_3D_PAE51904_eb3de804/

    # Native
    artic demultiplex --threads 32 PQPR071978_fastq_pass.fastq

    # Rapid
    porechop --verbosity 2 --untrimmed -i "PQPR071978_fastq_pass.fastq" -b ./ --rapid_barcodes --discard_middle --barcode_threshold 80 --threads 32 --check_reads 10000 --barcode_diff 5 > PQPR071978_fastq_pass.fastq.demultiplexreport.txt

    # Nanopolish
    RUN=PQPR071978 && for bc in {01..12}; do mkdir barcode${bc}; cd barcode${bc}; artic minion --normalise 200 --threads 32 --scheme-directory /directflow/KCCGGenometechTemp/projects/jamfer/SARS-CoV-2/SARS-CoV-2_GTG/protocols/Kirby/schemes --read-file ../../base/${RUN}_fastq_pass-BC${bc}.fastq --fast5-directory ../../${RUN}/*/fast5_pass --sequencing-summary ../../${RUN}_summary.txt nCoV-2019/V1 ${RUN}; cd ../; done
    
    # Medaka
    RUN=PQPR071978 && for bc in {01..12}; do mkdir barcode${bc}; cd barcode${bc}; artic minion --minimap2 --medaka --normalise 200 --threads 32 --scheme-directory /directflow/KCCGGenometechTemp/projects/jamfer/SARS-CoV-2/SARS-CoV-2_GTG/protocols/Kirby/schemes --read-file ../../base/${RUN}_fastq_pass-BC${bc}.fastq nCoV-2019/V1 ${RUN}; cd ../; done




## Acknowledgements

This is the joint work of our lab:

[Garvan Institute](https://www.garvan.org.au/): Ira Deveson, Jillian Hammond, Igor Stevanovski, Hasindu Gamaarachchi, from the Genomic Technologies team.

UNSW/Kirby Institute: Rowena Bull

PoW:

SYD/WIMR: John-Sebastian Eden

(need to add in others)

## License

[The MIT License](https://opensource.org/licenses/MIT)
