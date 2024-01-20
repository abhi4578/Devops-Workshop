# IUDX-Devops-Workshop

## Pre-requisites


1. Machine specs -
   - CPU - Minimum dual core
   - RAM - Minimum 8GB. 
   - Disk - Minimum 100 GB for root partition of Ubuntu/free disk space in windows
2. Preferably to have full fledged Ubuntu Operating System (OS) 22.04/20.04 Desktop. 
   The speaker will be using this and hence preferred. But not a mandatory requirement .  
   Full fledged Ubuntu OS can be installed through following ways
   - Refer [here](https://itsfoss.com/install-ubuntu/) for details to install Ubuntu  as the sole OS.
   - Refer [here](https://itsfoss.com/install-ubuntu-dual-boot-mode-windows/) for details to install Ubuntu as dual boot alongside Windows
   - Refer [here](https://ubuntu.com/tutorials/how-to-run-ubuntu-desktop-on-a-virtual-machine-using-virtualbox) for details of install Ubuntu in virtual machine using virtual box
3. Preferred mode : Install docker in full fledged Ubuntu OS.
   - Uninstall Old versions of docker by following [this](https://docs.docker.com/engine/install/ubuntu/#uninstall-old-versions) guide  
   - Install docker using apt repository by following [this](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository) guide
   - For convenience, manage docker as non root user, Refer [here](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
4. If Ubuntu cannot be installed as full fledged OS
    - On windows 
        - Install WSL2 and install Ubuntu . Refer [here](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#1-overview)
        - Install Docker Desktop with WSL2 as backend. Refer [here]([https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user](https://docs.docker.com/desktop/install/windows-install/))
     - On Mac OS
         - Install Docker Desktop on Mac. Refer [here](https://docs.docker.com/desktop/install/mac-install/)
         - Install Git
5. On  full fledged Ubuntu or WSL Ubuntu, install from default packages. Refer [here](https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-20-04#installing-git-with-default-packages).
6. On mac, install git by following on of the options in [this](https://git-scm.com/download/mac) guide
Create a docker hub account. Refer [here](https://docs.docker.com/docker-id/) for the details
