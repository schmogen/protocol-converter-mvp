# Role of Staphylococcus aureus Nitric Oxide Synthase (saNOS) in Aerobic Respiratory Metabolism and Cell Physiology

## Objective
To investigate the contribution of Staphylococcus aureus nitric oxide synthase (saNOS) to aerobic respiratory metabolism, endogenous reactive oxygen species (ROS) levels, and cellular physiology in the absence of exogenous stress.

## Materials
- Staphylococcus aureus strains: UAMS-1 wild-type, nos::erm mutant, and nos complement strains
- Tryptic soy broth (TSB) with and without glucose (TSB+G and TSB-G)
- Luria broth (LB) without glucose [data not shown]
- DPTA NONOate (NO donor; Cayman)
- CM-H2DCFDA (carboxy-2′,7′-dichlorofluorescein; ROS indicator; Life Technologies)
- MitoSOX Red (superoxide indicator; Life Technologies)
- DiOC2(3) (3,3′-diethyloxacarbocyanine iodide; membrane potential dye; Invitrogen)
- 5-Cyano-2,3-ditolyl tetrazolium chloride (CTC)
- Thioridizine HCl (TZ; NADH dehydrogenase inhibitor)
- Amplex Red Catalase Activity Kit (Life Technologies)
- Lysostaphin (Sigma)
- DNAse I (Qiagen)
- RNA extraction kits: RNeasy (Qiagen), Turbo DNA-free kit (Ambion), RiboZero Magnetic Kit (Epicentre), MicrobExpress Bacterial mRNA Enrichment Kit (Life Technologies)
- IonTorrent PGM platform reagents for RNAseq
- Scanning electron microscopy materials: Trump’s fixative, osmium tetroxide, ethanol, critical point drier, gold/palladium sputter coater
- 96-well tissue culture plates, microplate reader (Biotek Synergy HT)
- Flow cytometer (BD FACSort)
- Clark-type oxygen electrode (TBR-4100, World Precision Instruments)
- Liquid chromatography-tandem mass spectrometry (LC/MS/MS) setup for metabolomics

## Procedure

### Bacterial Growth Conditions
1. Streak S. aureus strains from frozen stocks to TSA plates with antibiotics (as necessary), incubate 24 h at 37 °C.
2. Pick single colony to inoculate overnight cultures in TSB+G with antibiotics (as appropriate), grow 15 h at 37 °C, 250 rpm.
3. For aerobic experiments, dilute overnight cultures into TSB+G or TSB-G to OD600 = 0.05 in 500 ml flasks (40 ml culture per flask), grow at 37 °C with shaking at 250 rpm.
4. When required, add 100 µM DPTA NONOate to sterile media immediately before inoculation.
5. Monitor growth by OD600 and CFU/ml at indicated timepoints.

### Growth Curve Analysis
1. Inoculate bacterial cultures as above in TSB-G or TSB+G.
2. Grow aerobically for 24 h.
3. Measure OD600 and determine CFU/ml by serial dilution and plating every 2 hours.

### Scanning Electron Microscopy (SEM)
1. Grow cultures aerobically in TSB-G to stationary phase (6 h).
2. Harvest 10 ml cultures by centrifugation at 3901 × g for 3 min at room temperature.
3. Wash pellets in 1× PBS and resuspend in 1.2 ml Trump’s fixative; incubate 15 min at room temperature.
4. Store at 4 °C until preparation.
5. Wash, postfix with 2% buffered osmium tetroxide, dehydrate in graded ethanol series, critical point dry.
6. Mount on aluminum stubs, sputter coat with gold/palladium.
7. Visualize using field-emission SEM at 50,000× magnification.
8. Measure cell lengths using ImageJ software from 12–14 fields.

### RNAseq Transcriptome Analysis
1. Grow wild-type and nos mutant strains aerobically in TSB-G to late exponential phase (4 h).
2. Extract total RNA using RNeasy kit; remove genomic DNA with Turbo DNA-free kit.
3. Verify RNA integrity (RIN ≥ 9.9) using Agilent Bioanalyzer.
4. Remove rRNA with RiboZero Magnetic Kit and MicrobExpress Bacterial mRNA Enrichment Kit.
5. Pool RNA from three independent cultures for each strain.
6. Construct RNAseq libraries using Ion Total RNAseq v2 Kit.
7. Sequence using IonTorrent PGM platform with Ion 318 Chip v2.
8. Map reads to MRSA252 genome (NC_002952.2).
9. Calculate RPKM values and normalize by quantile normalization.
10. Identify differentially expressed genes with criteria:
    - ≥80% unique read mapping
    - RPKM ≥ 50 in at least one dataset
    - Fold-change ≥ 2.0
11. Confirm select genes by qRT-PCR.

### Intracellular ROS and Superoxide Measurement
1. Grow strains in TSB-G or TSB+G aerobically for 3 h.
2. Harvest 19 ml (ROS) or 10 ml (superoxide) cultures by centrifugation.
3. Wash pellets in HBSS (ROS) or PBS (superoxide).
4. Resuspend:
   - For ROS: in HBSS with 10 µM CM-H2DCFDA; incubate 60 min at 37 °C.
   - For superoxide: in PBS with 5 µM MitoSOX Red; incubate 10 min at 37 °C.
5. Wash, aliquot 200 µl in triplicate into black 96-well plates.
6. Measure fluorescence and OD600 using Biotek Synergy HT (wavelengths: CM-H2DCFDA EX 485±20 nm, EM 516±20 nm; MitoSOX EX 500±27 nm, EM 600±40 nm).
7. Calculate RFU/OD600 for each sample.

### Catalase Activity Assay
1. Harvest cells from 3 h TSB-G cultures (5 ml) by centrifugation.
2. Store pellets at −80 °C.
3. Lyse pellets by mechanical disruption in 0.1 M Tris-HCl, pH 7.0.
4. Measure protein concentration by BCA assay.
5. Use Amplex Red Catalase Activity Kit; incubate samples with 50 µM H2O2, 50 µM Amplex Red, and 0.2 U/ml horseradish peroxidase for 1 h at room temperature.
6. Measure fluorescence (EX 540±25 nm, EM 600±40 nm).
7. Calculate catalase activity from standard curve, normalize to protein.

### Membrane Potential Measurement
1. Grow cultures aerobically in TSB-G or TSB+G for 3 h.
2. Harvest 1 ml, wash in 1× PBS.
3. Stain with 30 µM DiOC2(3) in 1× PBS.
4. Include CCCP (5 µM) as depolarizing control.
5. Incubate and analyze by flow cytometry (BD FACSort), recording red and green fluorescence.
6. Calculate red:green fluorescence ratio for 50,000 events.

### Respiratory Dehydrogenase Activity (CTC Staining)
1. Harvest 2 ml mid-log phase cultures.
2. Wash and resuspend in PBS containing 4.5 mM CTC.
3. Incubate at 37 °C; record fluorescence (EX 485±20 nm, EM 645±40 nm) every 10 min for 2 hours.
4. Normalize to initial OD600 and report fold change relative to wild-type.

### Oxygen Consumption Measurement
1. Harvest 25 ml aerobic TSB-G cultures at 3 h by centrifugation.
2. Resuspend pellets in 1 ml aerated, pre-warmed PBS at 37 °C.
3. Measure oxygen consumption at 37 °C using Clark-type oxygen electrode.
4. Determine rate from linear consumption phase, normalize to CFU/ml.

### NADH Dehydrogenase Inhibition and ROS Measurement
1. Add 15 µM thioridizine HCl (TZ) to cultures at inoculation.
2. Grow aerobically in TSB-G for 3 h.
3. Perform ROS measurements as above with CM-H2DCFDA.

### Aconitase Activity Assay
1. Harvest 18 ml aerobic TSB-G cultures at 3 h.
2. Lyse in assay buffer with lysostaphin and DNAse I at 37 °C for 30 min.
3. Clarify lysates by centrifugation.
4. Assay aconitase activity using Cayman Chemicals Aconitase Assay Kit by monitoring NADPH production at 340 nm at 37 °C.
5. Normalize activity to protein concentration.

### Metabolomics Sample Preparation and Analysis
1. Harvest 40 ml late exponential (4 h) TSB-G cultures.
2. Centrifuge to separate cell pellets and extracellular media (EXM).
3. Wash cell pellets twice with ice-cold PBS; freeze pellets and EXM immediately in liquid nitrogen and store at −80 °C.
4. Lyophilize samples overnight.
5. Extract metabolites from lyophilized pellets with 50:50 acetonitrile/0.3% formic acid, homogenize at 4 °C.
6. Reconstitute EXM lyophilizates in same solvent.
7. Quantify protein from aliquot for normalization.
8. Perform derivatization and LC/MS/MS for:
   - Organic acids using O-benzylhydroxylamine and carbodiimide derivatization.
   - Amino acids using MassTrak AAA Derivatization Kit.
   - Pyridine nucleotides and adenosine phosphates with isotope-labeled internal standards.
9. Use multiple reaction monitoring and appropriate columns for separation.
10. Normalize intracellular metabolites to total protein and extracellular metabolites to concentration (µM).

## Notes
- DPTA NONOate stock: 150 mM in 0.01 M NaOH, stored at −80 °C for ≤2 weeks.
- For SEM, measure cell lengths from longitudinal diameter using ImageJ.
- RNA integrity number of 9.9 or higher is required before sequencing.
- ROS and superoxide staining require careful control of incubation times and temperatures.
- Thioridizine HCl specifically inhibits NADH dehydrogenase without affecting other respiratory substrates.
- Multiple metabolic and gene expression changes occur in the nos mutant, indicating modulation of respiratory function and adaptation.