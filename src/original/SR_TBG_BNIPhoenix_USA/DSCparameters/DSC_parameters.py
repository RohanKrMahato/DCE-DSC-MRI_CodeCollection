#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 11:35:54 2021

authors: Sudarshan Ragunathan, Laura C Bell
@email: sudarshan.ragunathan@barrowneuro.org
@institution: Barrow Neurological Institute, Phoenix, AZ, USA
@lab: Translational Bioimaging Group (TBG)

DESCRIPTION
-----------
This function computes the following DSC metrics:
    CBF : numerically calculated as the maximum value of the tissue residue function  𝑅(𝑡) , where  𝑅(𝑡)  is related to the tissue concentration  𝐶(𝑡) , and the AIF  𝐶𝑎(𝑡)  by:  𝐶(𝑡)  =  𝐹.𝐶𝑎(𝑡)∗𝑅(𝑡) 
    CBV : numerically calculated as the area under the curve of the  Δ𝑅∗2  time curve
    MTT : numerically calculated as the ratio of CBV and CBF based on the Central Volume Theorem
INPUTS:

OUTPUTS;

"""
import numpy as np

def DSCparameters(dR2s_tumor, dR2s_AIF, residualFunction, TR):
    CBF = np.amax(residualFunction) * 60 * 100
    CBV = np.trapz(dR2s_tumor) / np.trapz(dR2s_AIF) * 100 
    MTT = CBV / CBF * 60 
    return CBF, CBV, MTT    