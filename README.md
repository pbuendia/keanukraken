# keanukraken
A tool for viewing the contents of metagenomic samples from a Kraken2 report file. See Keanu for Blast here: https://github.com/IGBB/keanu

## Files in this repository
* format_input.py: takes a file that contains a single BLAST query and taxon ID per line and formats it correctly as input for Keanu
  * format is `contig_query_name  taxonID_1 [counts], taxonID_2 [count], ...`
* make_db.py: creates Keanu taxonomy database and merged/deleted database from [NCBI taxonomy database ](ftp://ftp.ncbi.nih.gov/pub/taxonomy). Select the taxdmp file and decompress it.
* keanu.py: creates the visualization from a Kraken2 report file or by taking the output of format_input.py and make_db.py and parsing them
  * output based on http://bl.ocks.org/mbostock/raw/4339083/ or http://bl.ocks.org/vpletzke/raw/c5716da6a021005e7167a9504c6849b2/

## Running Keanu

### Assembly

In order to reduce sequence duplication, the reads can be assembled with some assembler. [ABySS](https://github.com/bcgsc/abyss) was used as Keanu was develeoped. This step is optional.

### Kraken2

[Kraken 2](https://ccb.jhu.edu/software/kraken2/) is the newest version of Kraken, a taxonomic classification system using exact k-mer matches to achieve high accuracy and fast classification speeds

### Keanu for Kraken2

#### Making the database
The following command is used to create the `taxonomy.dat` and `merged_deleted.dat` databases necessary for running Keanu. There are no optional parameters. The input files - names.dmb, nodes.dmp, delnodes.dmp, and merged.dmp - come from the taxdmp file located at the NCBI Taxonomy FTP site: ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/

`python make_db.py -names names.dmp -nodes nodes.dmp -out_db taxonomy.dat -deleted delnodes.dmp -merged merged.dmp -out_md_db merged_deleted.dat`

#### Running Keanu for Kraken
The following commands are used to create the interactive visualizations based on the input dataset. The first command produces a [bilevel partition graph](http://bl.ocks.org/vpletzke/raw/c5716da6a021005e7167a9504c6849b2/) and the second produces a [collapsible tree](http://bl.ocks.org/mbostock/raw/4339083/).

KeanuKraken has 2 input formats which are specified with the flag:

`-in_format {kraken,blast}, --input_format {kraken,blast}`

with 2 choices to run with a kraken-report or Blast file. For the Blast option, see https://github.com/IGBB/keanu 

Kraken format requires the column numbers for the taxon count and the taxon id. Example for kraken report with report-minimizer-data columns: -col_taxid 7 -col_ct 3.

To provide a kraken_report as input and create a bilevel graph:

`python keanu.py -db taxonomy.dat -md_db merged_deleted.dat -in example/kraken-report -view bilevel -out example/microbiome_bilevel.html --input_format kraken -col_taxid 7 -col_ct 3`

To provide a kraken_report as input and create a taxonomy tree:

`python keanu.py -db taxonomy.dat -md_db merged_deleted.dat -in example/kraken-report -view tree -out example/microbiome_tree.html --input_format kraken -col_taxid 7 -col_ct 3`

To provide a kraken_report as input and create a combined graph:

`python keanu.py -db taxonomy.dat -md_db merged_deleted.dat -in example/kraken-report -view combine -out example/microbiome_combined.html --input_format kraken -col_taxid 7 -col_ct 3`


## Citation

The paper describing the original Keanu can be found [here](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-019-2629-4).

