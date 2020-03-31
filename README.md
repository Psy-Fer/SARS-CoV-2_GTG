# SARS-CoV-2_GTG
Genomic Tech's COVID sequencing


RAMPART version in artic protocol doesn't have remote browser fix
Use RAMPART install


### Comparing references

Checking the reference used is the same, and if not, how they differ

```
pip3 install edlib

python3 compare_ref.py -r1 base_reference.fasta -r2 new_reference.fasta
```

### RAMPART

```

rampart --verbose --protocol /home/grid/SARS-CoV-2_GTG/protocols/Kirby/V1/ --ports 3000 3001 --basecalledPath /data/FLFL030920/FLFL030920/20200330_0557_X2_ACW369_55e7e4ce/fastq_pass/

```

## Analysis

### Nanopolish

```
conda activate artic-ncov2019

mkdir asm
cd asm

artic gather --min-length 2300 --max-length 2700 --prefix kirby-3 --directory /data/FLFL030920//FLFL030920/20200330_0557_X2_ACW369_55e7e4ce/

artic demultiplex --threads 4 kirby-3_fastq_pass.fastq

cd ..

for bc in {01..09}; do mkdir barcode; cd barcode; artic minion --normalise 200 --threads 4 --scheme-directory ~/SARS-CoV-2_GTG/protocols/Kirby/schemes --read-file ../asm/kirby-3_fastq_pass-NB.fastq --fast5-directory ../fast5_pass --sequencing-summary ../asm/kirby-3_sequencing_summary.txt nCoV-2019/V1 kirby-3; cd ../;  done

for file in barcode*; do tar -cf kirby-3_samples_11-19_nanopolish_.tar ; done

rsync --progress ./*.tar kyle:/volume3/EXT2_Projects/SARS-CoV-2/kirby/kirby-3/
```


### Medaka

```
conda activate artic-ncov2019-medaka

mkdir asm

artic gather --min-length 2300 --max-length 2700 --prefix kirby-3 --directory /data/FLFL030920//FLFL030920/20200330_0557_X2_ACW369_55e7e4ce/

artic demultiplex --threads 4 kirby-3_fastq_pass.fastq

cd ..

for bc in {01..09}; do mkdir barcode${bc}; cd barcode${bc}; artic minion --minimap2 --medaka --normalise 200 --threads 4 --scheme-directory ~/Dropbox/Bioinformatics/tools/repos/SARS-CoV-2_GTG/protocols/Kirby/schemes --read-file ../asm/kirby-3_fastq_pass-NB${bc}.fastq nCoV-2019/V1 kirby-3; cd ../; done

for file in barcode*; do tar -cf kirby-3_samples_11-19_medaka_.tar ; done

rsync --progress ./*.tar kyle:/volume3/EXT2_Projects/SARS-CoV-2/kirby/kirby-3/
```
