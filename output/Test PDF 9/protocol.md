# Contribution of the nos-pdt Operon to Virulence Phenotypes in Methicillin-Sensitive Staphylococcus aureus

## Objective
To investigate the role and regulation of the nitric oxide synthase (saNOS) enzyme encoded by the nos gene and its co-transcribed downstream gene pdt, encoding prephenate dehydratase (PDT), in methicillin-sensitive Staphylococcus aureus (MSSA), focusing on their contribution to oxidative stress resistance, phenylalanine biosynthesis, carotenoid pigmentation, intracellular nitric oxide (NO) production, and virulence phenotypes.

## Materials
- Staphylococcus aureus strains:
  - UAMS-1 (wild-type MSSA osteomyelitis clinical isolate)
  - KR1010 (UAMS-1 nos::erm insertion mutant)
  - KR1013 (UAMS-1 Δpdt deletion mutant)
  - Complemented strains (nos::erm mutant complemented with pMKnos; pdt mutant complemented with pMKpdt)
- Escherichia coli DH5α and RN4220 strains
- Plasmids pTR27, pKR13, pMKnos, pMKpdt, pCRBlunt, pCR2.1, pBSK, pBT2, pMK4
- Antibiotics:
  - Chloramphenicol (Cm) 2 mg/ml or 5 mg/ml or 10 mg/ml
  - Erythromycin (Erm) 2 mg/ml or 10 mg/ml
  - Ampicillin (Amp) 50 mg/ml
  - Kanamycin (Km) 50 mg/ml
- Culture media:
  - Tryptic Soy Agar (TSA)
  - Tryptic Soy Broth (TSB)
  - Chemically defined media (CDM), with and without phenylalanine
  - Luria-Bertani (LB) broth
- Glycerol (50% vol/vol) for stock cultures
- Fluorescent dye:
  - 4-Amino-5-methylamino-2',7'-difluorofluorescein (DAF-FM) diacetate
- NO donors and scavengers:
  - Diethylamine NONOate (DEA/NO) 100 mM
  - Diethylamine (DEA) 100 mM
  - 2-(4-carboxyphenyl)-4,5-dihydro-4,4,5,5-tetramethyl-1H-imidazolyl-1-oxy-3-oxide monopotassium salt (cPTIO) 150 mM
- Chemicals for pigment extraction:
  - Methanol
- Hydrogen peroxide (H2O2) 250 mM for oxidative stress assays
- Molecular biology reagents:
  - PCR primers (see Table 2)
  - Enzymes for restriction digestion and ligation (e.g., BamHI, EcoRI, HindIII, ClaI, SmaI)
  - DNA extraction and purification kits
  - qRT-PCR reagents and kits
  - TURBO DNA-free kit for DNA removal
  - iScript Reverse Transcriptase kit
  - iQ SYBR Green Supermix
- Mouse model:
  - Female CD-1 Swiss mice, 6 weeks old

## Procedure

### 1. Bacterial Strain Growth and Maintenance
1. Streak S. aureus strains from frozen stocks onto TSA and incubate at 37°C overnight (24 hours).
2. Culture single colonies overnight aerobically in TSB with shaking at 250 RPM.
3. Use appropriate selective antibiotics in broth or agar at the specified concentrations if required.
4. Maintain glycerol stock cultures at -80°C by mixing overnight cultures 1:1 with sterile 50% glycerol.

### 2. Creation of Mutant Strains
#### nos::erm Insertion Mutant (KR1010)
1. Amplify nos gene from S. aureus genomic DNA using primers nos1-F and nos1-R.
2. Clone PCR product into pCR2.1 (TA cloning vector).
3. Introduce internal BglII site into cloned nos allele 232 bp downstream of start codon by site-directed mutagenesis.
4. Insert erm resistance cassette into BglII site.
5. Clone erm-inserted nos allele into temperature-sensitive shuttle vector pBT2.
6. Transform pTR27 (pBT2 with mutant allele) into RN4220 by electroporation.
7. Transduce plasmid into UAMS-1 by phage transduction.
8. Grow at non-permissive temperature (43°C) on TSA + 10 mg/ml Erm to promote chromosomal integration.
9. Perform serial passage at 30°C without antibiotics, plating on TSA + 10 mg/ml Erm at days 3–5 to select for plasmid excision and replacement.
10. Screen colonies for Erm resistance and Cm sensitivity.
11. Confirm gene replacement by PCR and Southern blotting.

#### Δpdt Deletion Mutant (KR1013)
1. Amplify ~1.2 kb upstream and ~1.0 kb downstream flanking regions of pdt gene using primers pdt1-F/pdt1-R and pdt2-F/pdt2-R.
2. Clone each PCR product into pCRBlunt vector and sequence verify.
3. Excise inserts with HindIII-XbaI.
4. Perform triple ligation with digested pBT2 vector (HindIII-XbaI) and flanking fragments.
5. Transform into E. coli DH5α and select transformants.
6. Move construct into S. aureus RN4220 by electroporation.
7. Phage transduce into UAMS-1.
8. Perform allelic exchange via temperature shift and serial passage as for nos mutant.
9. Screen isolated colonies on TSA with and without 5 mg/ml Cm for sensitivity.
10. Confirm deletion by PCR using nos2-F and pdt2-R primers.

### 3. Creation of Complementation Plasmids
1. For pMKnos:
   - PCR amplify 1.6 kb fragment spanning 564 bp upstream of nos start codon through entire nos ORF using nos2-F and nos2-R primers.
   - Clone into pCRBlunt, verify by sequencing.
   - Excise fragment by BamHI and EcoRI and ligate into BamHI-EcoRI digested pMK4 shuttle vector.
   - Move into RN4220 and then relevant S. aureus strains by electroporation/phage transduction.

2. For pMKpdt:
   - PCR amplify 1.6 kb nos promoter region and pdt ORF in two overlapping fragments using primers nos3-F/nos3-R (promoter) and pdt3-F/pdt3-R (pdt ORF).
   - Clone fragments into pCRBlunt, sequence verify.
   - Ligation of promoter and pdt insert into pMK4 vector via BamHI-SmaI and SmaI-EcoRI sites.
   - Transform into RN4220 and then mutants.

### 4. Growth Experiments and RNA Isolation
1. Dilute overnight cultures of UAMS-1 to an OD_600 of 0.05 in TSB.
2. Grow cultures aerobically (1:10 volume-to-flask ratio, 250 RPM) or under low oxygen (7:10 volume-to-flask ratio, static, 0 RPM) at 37°C.
3. Collect samples at 2, 6, and 12 hours for RNA isolation.
4. Lyse cells using FASTPREP system and purify RNA with Qiagen RNeasy kit.
5. Treat RNA with TURBO DNase.
6. Perform mock qRT-PCR without reverse transcriptase to confirm absence of genomic DNA.
7. Convert 0.75 µg RNA to cDNA using iScript Reverse Transcriptase kit.

### 5. Quantitative Real-Time PCR (qRT-PCR) Analysis
1. Perform qRT-PCR using iQ SYBR Green Supermix and gene-specific primers (Table 2) in triplicate technical replicates.
2. Use sigA gene as housekeeping reference.
3. Analyze relative fold-change by Livak 2^-ΔΔCt method.
4. Assess co-transcription of nos and pdt by RT-PCR spanning junction using primer nos5-F and pdt5-R.
5. Confirm no amplification in RT- controls.

### 6. Phenylalanine Biosynthesis Assay
1. Grow wild-type, nos mutant, pdt mutant, and complement strains overnight in TSB + 5 mg/ml Cm.
2. Harvest, wash, and resuspend cells in CDM with or without phenylalanine.
3. Inoculate at OD_600 = 0.02 into 96-well plates with respective CDM.
4. Grow statically at 37°C.
5. Measure OD_600 every 2 hours for 24 hours.
6. Perform serial dilutions and track plating for CFU counts as needed.

### 7. Hydrogen Peroxide Sensitivity Assay
1. Grow planktonic cultures aerobically to mid-exponential phase (OD_600 ~0.5).
2. Treat cultures with 250 mM H_2O_2 for 2 hours.
3. Determine viability by CFU plating pre- and post-treatment.
4. Compare survival between wild-type, nos mutant, pdt mutant, and complemented strains.

### 8. Carotenoid Pigment Assay
1. Grow strains on TSA + 5 mg/ml Cm plates at 37°C for 48 hours.
2. Scrape cells and wash twice with dH_2O by centrifugation (3 min, 13,000 RPM).
3. Resuspend pellet in 420 µl methanol, vortex for 10 seconds.
4. Take 20 µl aliquot for OD_465 measurement in 650 µl methanol.
5. Normalize absorbance by relative OD_600 of corresponding culture.
6. Perform in triplicate with at least 3 independent experiments.

### 9. Detection of Intracellular NO/RNS Using DAF-FM Diacetate
1. Harvest S. aureus cells from TSA plates (26-hour or 28-hour cultures) or broth cultures.
2. Resuspend cells in HBSS buffer containing 5 mM DAF-FM diacetate.
3. Incubate for 1 hour at 37°C.
4. Wash cells by centrifugation and resuspend in HBSS alone or HBSS with:
   - 100 mM DEA (NO donor control)
   - 100 mM DEA/NO (NO donor)
   - 150 mM cPTIO (NO scavenger)
5. Immediately transfer 200 µl aliquots in triplicate or quadruplicate to 96-well plates.
6. Measure fluorescence (excitation 485 nm, emission 516 nm) and OD_600 in fluorescence plate reader at 37°C.
7. Calculate relative fluorescence units normalized to OD_600.
8. Compare between wild-type, nos mutant, and complemented strains.

### 10. Murine Model of Sepsis
1. Prepare bacterial suspensions of UAMS-1 (wild-type) and KR1010 (nos mutant) in PBS at 1 × 10^9 CFU/ml.
2. Inject 100 µl (1 × 10^8 CFU) via tail vein into 6-week-old female CD-1 Swiss mice, n=9 per group.
3. Monitor mice for mortality and morbidity over 7 days, recording pre-moribund signs.
4. Euthanize mice that reach pre-moribund state or at 7 days endpoint.
5. Harvest liver, kidneys, heart, and lungs.
6. Homogenize organs and enumerate bacterial loads by CFU plating.
7. Analyze data for bacterial burden and survival differences.

## Notes
- Nos and pdt are co-transcribed in S. aureus and form a unique operon among staphylococci.
- The nos mutant has a partial polar effect reducing pdt expression by ~3-fold in low-oxygen TSB cultures.
- saPDT is confirmed as necessary for growth in phenylalanine-deficient chemically defined media.
- The nos mutant shows increased carotenoid pigmentation despite reduced resistance to oxidative stress.
- Intracellular NO/RNS detection with DAF-FM diacetate is sensitive and specific under tested conditions.
- Oxidative stress resistance by saNOS contributes significantly to virulence in a murine sepsis model.
- All experiments involving animals were performed according to institutional and national guidelines with approved protocols.

## Review Checklist
- [x] Growth conditions verified (temperature, CO2/O2, time)
- [x] Media composition and volumes verified
- [x] Mixing parameters verified (rpm/RCF, time)
- [x] Incubation times verified
- [x] Centrifugation settings verified (RCF, time, temp)
- [x] Step order confirmed against source
- [x] Any ambiguous values flagged with [CHECK]

## Review Flags

## Critical Parameters Checklist (from the protocol)

- Temperatures: 37°C incubation for bacterial growth and mouse model; 43°C non-permissive temperature for plasmid integration; 55°C for pigment extraction step
- Times:  
  - Overnight growth on TSA plates: 24 h  
  - Planktonic cultures: variable sampling at 2, 6, 12 h  
  - Induction of second recombination event: 3–5 days with periodic subcultures every 24 h  
  - Hydrogen peroxide treatment: 2 h  
  - DAF-FM staining: 1 h incubation, fluorescence measured after 30–90 min  
  - Pigment extraction: vortex 10 s, incubation 5 min at 55°C  
  - Murine infection monitoring: 7 days or until pre-moribund state  
- Volumes:  
  - Glycerol stocks: 1:1 mixing of culture and 50% glycerol  
  - 1 ml aliquots used for suspensions for pigment assays, phenylalanine biosynthesis inocula, and other measurements  
  - 200 µl aliquots used for fluorescence plate assays in 96-well plates  
  - Plate volumes: 96-well plates for growth assays and fluorescence readings  
- Concentrations:  
  - Antibiotics: chloramphenicol 2, 5, or 10 mg/ml; erythromycin 2 or 10 mg/ml; ampicillin 50 mg/ml; kanamycin 50 mg/ml  
  - Hydrogen peroxide: 250 mM for oxidative stress assays  
  - DAF-FM diacetate: 5 mM staining concentration  
  - DEA/NO and DEA controls: 100 mM  
  - cPTIO (NO scavenger): 150 mM  
- rpm/RCF:  
  - Aerobic planktonic culture: 250 rpm  
  - Low-oxygen static culture: 0 rpm  
  - Centrifugation: 13,000 rpm for 2–3 min for cell harvesting and washing steps  
- CO2/O2:  
  - Aerobic conditions (~air levels O2) with shaking (250 rpm)  
  - Low-oxygen defined as static culture with increased volume-to-flask ratio (7:10 volume-to-flask), no shaking (0 rpm)  
- Mouse infections: 1 × 10^8 CFU per mouse via tail vein injection (100 µl of 1 × 10^9 CFU/ml suspension); n=9 mice per group  

## Potential Missing Parameters (compare to source)

- Exact flask sizes or volumes for planktonic cultures are not specified beyond volume-to-flask ratios; no flask volume given (source says 1:10 or 7:10 volume-to-flask ratio but no flask absolute volumes detailed)  
- Temperature of centrifugation steps (likely room temperature but not explicitly stated)  
- Specific source or detailed composition of chemically defined media (CDM) used, only generally referenced from literature  
- No explicit details in protocol for CHROMATOGRAPHIC or other methods used for metabolite confirmation (phenylpyruvate, etc.) [CHECK] (likely not in source)  
- Details of PCR cycling parameters, enzyme concentrations, and thermocycler conditions omitted  
- Details of mouse housing environment (temperature, humidity, light-dark cycles) are omitted but only broadly referenced as standard conditions  
- Exact OD600 values used to initiate some experiments (e.g., H2O2 assays are mid-exponential phase but exact OD range not specified beyond approximate 0.5 in source)  
- No explicit information on incubation times during phage transduction or electroporation efficiencies—assumed standard  
- The fluorescence measurement intervals and specifics of fluorimeter settings (gain, sensitivity) not exhaustively listed (except EX/EM wavelengths)  
- The sequence or source of primers (sequences provided in source but not in protocol)  

## Possible Hallucinations / Unsupported Claims

- None detected.  
- The generated protocol does not add unsubstantiated claims or steps; all protocol sections are supported by detailed descriptions in the source text.  
- Interpretation statements (e.g., "saNOS is not required for activity of saPDT") are omitted from protocol and only present in discussion, which is appropriate.  

## Step Order / Omission Risks

- No major step order changes apparent; protocol follows source descriptions for mutant creation, growth assays, complementation, RNA work, and mouse model.  
- The use of RNAse-free conditions and rigorous RNA QC (e.g., RIN values) is not explicitly stated but typically implied; possible risk if omitted.  
- The protocol simplifies detailed screening and confirmation assays (Southern blotting, PCR screening) to brief steps—may risk skipping confirmation details if blindly followed.  
- The timing and temperature conditions during plasmid integration and excision steps in mutant construction appear consistent with source.  
- DAF-FM staining steps are appropriately detailed, though details about photobleaching avoidance during fluorescence measurement are not discussed—[CHECK].  
- Because partial polarity of nos::erm insertion mutant onto pdt is noted in source, the use of complemented strains is important; the protocol includes these but does not explicitly caution about this phenomenon—should be flagged as potential risk for experimenter.  
- The growth assays in chemically defined media use static conditions in microplates per source, which the protocol reflects; no oxygen control other than static conditions—possible variability in low-oxygen condition control if not carefully monitored—[CHECK].  

# Summary

The generated protocol accurately reflects the detailed experimental procedures, conditions, and parameters described in the source text. The critical numeric parameters such as temperature, time, media conditions, antibiotic concentrations, rpm, and fluorescence measurement settings are all well covered. Minor potential omissions pertain to some procedural details standard in molecular biology work but not always specified in source, including exact flask volumes during TSB growth, PCR thermocycling parameters, centrifugation temperatures, and mouse housing details. No unsupported or hallucinated claims are included in the protocol, which attentively sticks to methods present in the source. Slight caution is advised regarding the partial polar effect of the nos mutation on pdt expression, and the necessity of complementation controls to confirm phenotypes. Overall, the protocol is trustworthy with minor points for confirmation and attention during execution.
