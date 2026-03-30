# Generating-vortex-beam-by-BIC-of-Photonics-crystal-in-momentum-space

# Reproduction of the Supporting-Information FDTD Simulation from Shi and Zi (*Nature Photonics*, 2020)

This repository contains a modified script for reproducing the FDTD simulation reported in the supporting information of a 2020 *Nature Photonics* paper by **Lei Shi**, **Jian Zi**, and co-workers.

The current version is mainly intended for **academic reproduction, personal learning, and visualization**. The code is based on an open-source script shared by another developer, and I have only made **simple modifications** for my own testing and plotting workflow. At present, I cannot confidently identify the original author of that script. If someone points out the exact source, I will gladly add the proper name and attribution.

---

## Overview

This project is used to simulate the optical response of a finite photonic-crystal slab under beam excitation and to visualize the resulting field distributions.

Depending on the simulation settings and post-processing steps, the script can be used to inspect:

- near-field distributions,
- beam propagation patterns,
- side-view field evolution,
- intensity maps on selected planes,
- and other related optical features.

This type of calculation is useful for studying structured-light generation, finite-size photonic-crystal effects, and polarization-related optical responses.

---

## Operating Environment

This workflow is intended to run in a **Linux-like environment**.

Recommended options:

- **native Linux** (strongly recommended),
- **Ubuntu / Debian**,
- **WSL / WSL2** on Windows.

A Linux environment is strongly preferred because scientific simulation packages such as **Meep** and their numerical dependencies are generally easier to install and manage there than in a native Windows environment.

---

## Environment Preparation

Before installing Meep, it is strongly recommended to **install Miniconda3 first** and create a dedicated Python environment for this project.

This is important because Meep and its dependencies are usually easier to manage through Conda than through a mixed system-level Python installation.

### Install Miniconda3

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
