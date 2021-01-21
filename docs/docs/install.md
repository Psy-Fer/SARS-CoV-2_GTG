# Installation

Installation instructuons for both the ARTIC analysis pipeline, as well as RAMPART for real-time monitoring.

# Linux

## miniconda

Visit https://docs.conda.io/en/latest/miniconda.html and download the appropriate binary. Most likely that will be the following:

`Python 3.8	Miniconda3 Linux 64-bit`

Command line download:

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

Output example:

    --YYYY-MM-DD HH:MM:SS--  https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    Resolving repo.anaconda.com (repo.anaconda.com)... xxx.xxx.xxx.x, xxx.xxx.xxx.x, yyyy:yyyy::yyyy:yyyy, ...
    Connecting to repo.anaconda.com (repo.anaconda.com)|xxx.xxx.xxx.x|:xxx... connected.
    HTTP request sent, awaiting response... 200 OK
    Length: 94235922 (90M) [application/x-sh]
    Saving to: 'Miniconda3-latest-Linux-x86_64.sh’

    Miniconda3-latest-L 100%[===================>]  89.87M  5.41MB/s    in 17s     

    YYYY-MM-DD HH:MM:SS (5.36 MB/s) - 'Miniconda3-latest-Linux-x86_64.sh’ saved [94235922/94235922]

Modify the shell file with execute permissions

    chmod +x Miniconda3-latest-Linux-x86_64.sh

run the shell file

    ./Miniconda3-latest-Linux-x86_64.sh

    Welcome to Miniconda3 py38_4.9.2

    In order to continue the installation process, please review the license
    agreement.
    Please, press ENTER to continue
    >>>

Press ENTER

The Lisence information will apper. Press SPACE multiple times to scroll to the bottom.

__insert lisence image__

    Last updated September 28, 2020


    Do you accept the license terms? [yes|no]
    [no] >>>

type `yes` and hit ENTER

    Do you accept the license terms? [yes|no]
    [no] >>> yes

    Miniconda3 will now be installed into this location:
    /home/jamfer/miniconda3

      - Press ENTER to confirm the location
      - Press CTRL-C to abort the installation
      - Or specify a different location below

    [/home/jamfer/miniconda3] >>>

either hit enter to install to the default /HOME/USER/miniconda3 folder, or enter your own directory. For example, enter `./miniconda3` to build in the current directory

    ...
    six                pkgs/main/linux-64::six-1.15.0-py38h06a4308_0
    sqlite             pkgs/main/linux-64::sqlite-3.33.0-h62c20be_0
    tk                 pkgs/main/linux-64::tk-8.6.10-hbc83047_0
    tqdm               pkgs/main/noarch::tqdm-4.51.0-pyhd3eb1b0_0
    urllib3            pkgs/main/noarch::urllib3-1.25.11-py_0
    wheel              pkgs/main/noarch::wheel-0.35.1-pyhd3eb1b0_0
    xz                 pkgs/main/linux-64::xz-5.2.5-h7b6447c_0
    yaml               pkgs/main/linux-64::yaml-0.2.5-h7b6447c_0
    zlib               pkgs/main/linux-64::zlib-1.2.11-h7b6447c_3


    Preparing transaction: done
    Executing transaction: done
    installation finished.
    Do you wish the installer to initialize Miniconda3
    by running conda init? [yes|no]
    [no] >>>

type `yes` and enter (we will fix the problems this causes in a moment)

    ...
    Preparing transaction: done
    Executing transaction: done
    installation finished.
    Do you wish the installer to initialize Miniconda3
    by running conda init? [yes|no]
    [no] >>> yes
    ./Miniconda3-latest-Linux-x86_64.sh: 494: ./Miniconda3-latest-Linux-x86_64.sh: [[: not found
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/condabin/conda
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/bin/conda
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/bin/conda-env
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/bin/activate
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/bin/deactivate
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/etc/profile.d/conda.sh
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/etc/fish/conf.d/conda.fish
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/shell/condabin/Conda.psm1
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/shell/condabin/conda-hook.ps1
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/lib/python3.8/site-packages/xontrib/conda.xsh
    no change     /home/jamfer/data/SARS-CoV-2/docs/miniconda3/etc/profile.d/conda.csh
    modified      /home/jamfer/.bashrc

    ==> For changes to take effect, close and re-open your current shell. <==

    If you'd prefer that conda's base environment not be activated on startup,
       set the auto_activate_base parameter to false:

    conda config --set auto_activate_base false

    Thank you for installing Miniconda3!


**Close terminal and open again**

    which conda

mine says

    /home/jamfer/data/SARS-CoV-2/docs/miniconda3/condabin/conda

which is where I just installed it.

We now need to remove the automatic conda init from ~/.bashrc so it does not interfere with other environments.

open the ~/.bashrc file and find the conda init commands

    cat ~/.bashrc

    ...

    # >>> conda initialize >>>
    # !! Contents within this block are managed by 'conda init' !!
    __conda_setup="$('/home/jamfer/data/SARS-CoV-2/docs/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
    if [ $? -eq 0 ]; then
        eval "$__conda_setup"
    else
        if [ -f "/home/jamfer/data/SARS-CoV-2/docs/miniconda3/etc/profile.d/conda.sh" ]; then
            . "/home/jamfer/data/SARS-CoV-2/docs/miniconda3/etc/profile.d/conda.sh"
        else
            export PATH="/home/jamfer/data/SARS-CoV-2/docs/miniconda3/bin:$PATH"
        fi
    fi
    unset __conda_setup
    # <<< conda initialize <<<



Yours will look slightly different due to different paths.
We need to copy this information into a separate shell file, then remove this from `~/.bashrc` .

copy everything similar to above

then copy into a file called something like `~/conda_init.sh`

and remove the same section from `~/.bashrc`

**Close and open terminal again**

To activate conda, we can now run

    source ~/conda_init.sh

## ARTIC and RAMPART

Download the repo from github

    cd
    git clone https://github.com/artic-network/artic-ncov2019.git
    cd artic-ncov2019
    conda env remove -n artic-ncov2019
    conda env create -f environment.yml

__insert image of venv installing__




Other Operating Systems will work, but may need system specific changes to installation method. Let us know if you would like this extended to other Operating Systems.
