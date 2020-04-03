# SARS-CoV-2_GTG
Genomic Tech's COVID sequencing

This is a living git, that will change over time as we test out various methods.
We are mostly using a 14 primer scheme, which requires some changes to the artic protocol

Also included are some handy commands for running analyses on multiple barcodes at once.
We are doing both nanopolish and medaka for all runs. So far, so good.

Please let me know if anything is unclear, or you have suggestions or questions.





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


## Acknowledgements

This is the joint work of our lab:

[Garvan Institute](https://www.garvan.org.au/): Ira Deveson, Jillian Hammond, Igor Stevanovski, Hasindu Gamaarachchi, from the Genomic Technologies team.

UNSW/Kirby Institute: Rowena Bull

PoW:

SYD/WIMR:

(need to add in others)

## License

[The MIT License](https://opensource.org/licenses/MIT)
