# Staphylococcus aureus Nitric Oxide Synthase (saNOS) Modulates Aerobic Respiratory Metabolism and Cell Physiology

## Objective
Investigate the role of saNOS in S. aureus aerobic physiology by examining its effect on aerobic respiratory function, endogenous reactive oxygen species (ROS) levels, cell morphology, gene expression, and metabolite profiles during growth without exogenous stress.

## Materials
- S. aureus strains:
  - UAMS-1 wild-type
  - UAMS-1 nos mutant
  - UAMS-1 nos complement strain
  - LAC-13C wild-type and nos::erm mutant (plasmid-cured derivative of CA-MRSA strain LAC)
- Growth media:
  - Tryptic soy broth with glucose (TSB+G; 14 mM glucose)
  - Tryptic soy broth without glucose (TSB-G)
  - Luria Broth (LB) without glucose [data not shown]
- Chemicals and reagents:
  - DPTA NONOate (NO donor)
  - Carboxy-2′,7′-dichlorofluorescein (CM-H2DCFDA) fluorescent ROS indicator
  - MitoSOX Red (superoxide-specific stain)
  - Amplex Red catalase activity kit (Life Technologies)
  - 3,3′-diethyloxacarbocyanine iodide (DiOC2(3)) membrane potential carbocyanine dye
  - 5-cyano-2,3-ditolyl tetrazolium chloride (CTC)
  - Thioridizine HCl (TZ) NADH dehydrogenase inhibitor
  - Phosphate Buffered Saline (PBS)
  - Lysostaphin
  - DNase I
  - Various reagents for RNA extraction, quantitative PCR, and metabolomics [LC/MS/MS]
- Equipment:
  - Erlenmeyer flasks (500 ml)
  - Shaker incubator (37 °C, 250 rpm)
  - Spectrophotometer (OD600 measurements)
  - Flow cytometer (FACSort)
  - Plate reader (Synergy HT)
  - Scanning Electron Microscope (SEM)
  - Clark-type oxygen electrode (TBR-4100)
  - IonTorrent PGM platform (for RNAseq)
  - LC/MS/MS equipment for metabolomics analysis

## Procedure

### Bacterial Growth Conditions
1. Streak strains from −80°C stocks on TSA with appropriate antibiotics; incubate 24 h at 37°C.
2. Inoculate single colonies into overnight cultures in TSB+G with antibiotics; incubate 15 h, 37 °C, 250 rpm.
3. For aerobic growth:
   - Inoculate 40 ml TSB+G or TSB-G in 500 ml flasks (1:12.5 volume-to-flask ratio) to OD600 = 0.05.
   - Incubate at 37 °C with shaking at 250 rpm.
4. For NO complementation, add DPTA NONOate to 100 µM final concentration at inoculation from 150 mM stock (prepared in 0.01 M NaOH, stored at −80°C ≤ 2 weeks).

### Growth Monitoring
1. Grow cells aerobically in TSB-G or TSB+G.
2. Measure OD600 and determine CFU/ml every 2 hours by serial dilution and track plating.
3. Perform assays as biological triplicates.

### Scanning Electron Microscopy (SEM)
1. Harvest 10 ml cultures at 6 h from TSB-G aerobic growth by centrifugation (3901 × g, 3 min, RT).
2. Wash pellets with 1× PBS; fix in Trumps fixative (4% formalin, 2% glutaraldehyde in 0.2 M sodium cacodylate buffer) for 15 min at RT.
3. Store fixed cells at 4°C until sample processing.
4. Wash and post-fix with 2% osmium tetroxide; dehydrate in graded ethanol series; critical point dry.
5. Mount on specimen stubs; sputter coat with gold/palladium.
6. Image at 50,000× magnification.
7. Measure cell length using ImageJ on 12–14 fields of view; analyze length differences statistically.

### RNAseq Analysis and qRT-PCR Confirmation
1. Harvest total RNA from 4 h aerobic TSB-G cultures for each strain.
2. Extract RNA using RNeasy kit; treat with Turbo DNA-free DNase.
3. Verify RNA integrity (RIN ≥ 9.9).
4. Deplete rRNA using RiboZero Magnetic Kit and MicrobExpress Bacterial mRNA Enrichment Kit.
5. Pool RNA from 3 biological replicates per strain.
6. Prepare libraries using Ion Total RNAseq v2 Kits.
7. Sequence on IonTorrent PGM with Ion 318 Chip v2.
8. Map reads to S. aureus MRSA252 genome reference; filter rRNA reads.
9. Determine differentially expressed genes with:
   - ≥ 80% unique mapping reads,
   - RPKM ≥ 50 in ≥ 1 strain,
   - Fold change ≥ 2.
10. Validate selected genes by qRT-PCR (3 independent RNA isolations).

### Intracellular ROS and Superoxide Measurements
1. Grow cultures in TSB-G or TSB+G aerobically to 3 h.
2. For intracellular ROS:
   - Harvest 1.9 ml culture; centrifuge at 3901 × g RT.
   - Wash with 1 ml HBSS; resuspend in 1 ml HBSS with 10 µM CM-H2DCFDA.
   - Incubate 60 minutes at 37 °C; wash once; resuspend in HBSS.
   - Dispense 200 µl triplicates into black 96-well plates.
   - Measure fluorescence (Ex: 485 ± 20 nm; Em: 516 ± 20 nm) and OD600.
3. For superoxide:
   - Harvest 10 ml culture; centrifuge and resuspend in 5 µM MitoSOX Red (prepared from 5 mM stock in PBS).
   - Incubate 10 min at 37 °C, wash once.
   - Dispense 200 µl triplicates into 96-well plates.
   - Measure fluorescence (Ex: 500 ± 27 nm; Em: 600 ± 40 nm) and OD600.
4. Normalize fluorescence to OD600.

### Catalase Activity Assay
1. Harvest 5 ml from 3 h TSB-G aerobic cultures; centrifuge at 3901 × g, 5 min, 4 °C.
2. Store pellets at −80 °C until assay.
3. Thaw and resuspend pellets in 1 ml 0.1 M Tris-HCl pH 7.0.
4. Lyse cells with bead-beating, centrifuge at 13,000 × g, 4 °C to obtain cytosolic protein.
5. Quantify protein by BCA assay.
6. Measure catalase activity using Amplex Red kit:
   - Use 1:1000 diluted protein.
   - Incubate with H2O2, Amplex Red, and horseradish peroxidase.
   - Read fluorescence (Ex: 540 ± 25 nm; Em: 600 ± 40 nm) after 1 h.
7. Determine activity from standard curve; normalize to protein.

### Membrane Potential Measurement
1. Harvest 1 ml from 3 h aerobic cultures in TSB+G or TSB-G by centrifugation.
2. Wash cell pellets with 1× PBS; resuspend 25 µl cells in 2 ml PBS containing 30 µM DiOC2(3).
3. Include 5 µM CCCP control for depolarization.
4. Incubate briefly; analyze 50,000 cells by flow cytometry.
5. Calculate red:green fluorescence ratio (increased ratio indicates increased membrane potential).
6. For NO complementation, add 100 µM DPTA NONOate at inoculation.

### Respiratory Activity (CTC Staining)
1. Harvest 2 ml of 3 h aerobic cultures; wash cells; resuspend in PBS with 4.5 mM CTC.
2. Transfer 200 µl triplicates to 96-well black plates.
3. Incubate at 37 °C; measure fluorescence (Ex: 485 ± 20 nm; Em: 645 ± 40 nm) every 10 min for 120 min.
4. Normalize fluorescence at 70 min to OD600.

### Oxygen Consumption Measurement
1. Harvest 25 ml from 3 h aerobic TSB-G cultures; centrifuge at 3901 × g, 5 min, RT.
2. Resuspend pellets in 1 ml aerated PBS at 37 °C.
3. Measure oxygen consumption using Clark-type electrode at 37 °C.
4. Use slope of linear consumption period (~2 min); normalize to CFU/ml.

### NADH Dehydrogenase Inhibition and Effects on ROS and Aconitase
1. Inoculate cultures with 15 µM Thioridizine HCl (TZ) inhibitor at time zero.
2. Grow aerobically 3 h in TSB-G.
3. Measure intracellular ROS as described above with CM-H2DCFDA stain.
4. Isolate proteins for aconitase assay using Cayman Chemicals Aconitase Assay Kit:
   - Resuspend 18 ml cultures in aconitase buffer; add lysostaphin and DNase I.
   - Incubate 30 min 37 °C; centrifuge; freeze proteins.
   - Dilute samples 1:4; monitor NADPH production at 340 nm every minute for 60 min at 37 °C.
   - Include no substrate controls; calculate activity from absorbance change.
   - Normalize activity to total protein concentration.

### Metabolite Sampling and Targeted Metabolomics
1. Harvest 40 ml cultures after 4 h aerobic growth in TSB-G by centrifugation (3901 × g, 10 min, 4 °C).
2. Collect and freeze 2 × 1 ml supernatant samples as extracellular media (EXM).
3. Wash cell pellets twice with PBS at 4 °C; pellet and flash-freeze.
4. Lyophilize pellets and EXM samples overnight.
5. Homogenize cell pellets with 400 µl 50:50 acetonitrile/0.3% formic acid at 4 °C via bead-beating.
6. Reconstitute EXM in 400 µl 50:50 acetonitrile/0.3% formic acid.
7. Quantify protein from an aliquot of PBS-washed cell pellet homogenate by BCA assay.

### Organic Acids Quantitation
1. Spike 50 µl cell homogenate or EXM with 10 µl heavy isotope-labeled internal standards.
2. Add 50 µl 0.4 M O-benzylhydroxylamine and 10 µl 2 M 1-ethyl-3-(3-dimethylaminopropyl)carbodiimide.
3. Incubate 10 min at RT; extract with 600 µl ethyl acetate and 100 µl water.
4. Dry 100 µl organic layer; reconstitute in 1 ml 50:50 methanol/water.
5. Separate via UPLC on Waters BEH C18 column at 45 °C; elute with 0.1% formic acid in water/acetonitrile gradient.
6. Quantify by LC/MS/MS using multiple reaction monitoring.
7. Normalize intracellular metabolites to protein; extracellular concentrations reported in µM.

### Amino Acids Quantitation
1. Spike 100 µl homogenate or EXM with 10 µl heavy isotope-labeled amino acid internal standards.
2. Add 800 µl ice-cold methanol; centrifuge at 18,000 × g, 5 min, 10 °C.
3. Dry 100 µl supernatant; reconstitute in 80 µl borate buffer + 20 µl MassTrak AAA reagent.
4. Derivatize at 55 °C for 10 min.
5. Separate on Waters AccQ-Tag column at 55 °C using proprietary eluents gradient.
6. Quantify by LC/MS/MS; normalize to protein for cells, report µM for EXM.

### Pyridine Nucleotides and Adenosine Phosphates Quantitation
1. Spike 100 µl homogenate with 10 µl heavy isotope-labeled internal standards.
2. Adjust pH to ~4 with 100 µl 1 M ammonium formate; centrifuge at 18,000 × g, 5 min, 10 °C.
3. Filter clarified homogenate through 3K Omega Filter Plate.
4. Separate on Thermo Hypercarb or HSS T3 columns at temperatures 30–40 °C, with ammonium acetate/acetonitrile gradients.
5. Quantify via LC/MS/MS; normalize to protein concentrations.

## Notes
- NO donor DPTA NONOate and NADH dehydrogenase inhibitor thioridizine HCl were added at inoculation unless otherwise specified.
- RNA integrity verified by RIN of 9.9 before sequencing.
- SEM cell length measurements performed on multiple fields and statistically analyzed (Holm-Sidak test).
- Membrane potential and respiratory activity assays include appropriate controls (CCCP and NO donor).
- All metabolite quantifications include internal heavy isotope-labeled standards.
- Data normalization and statistical testing followed standard procedures.

## Review Checklist
- [ ] Growth conditions verified (temperature 37 °C, shaking 250 rpm, aerobic culture, inoculum OD600 = 0.05)
- [ ] Media composition and volumes verified (TSB ± 14 mM glucose, 40 ml culture in 500 ml flask)
- [ ] Mixing parameters verified (250 rpm shaking)
- [ ] Incubation times verified (3–6 h for various assays; 24 h for growth curves)
- [ ] Centrifugation settings verified (generally 3901 × g for 3–10 min at RT or 4 °C; 13,000 × g for protein preparations)
- [ ] Step order confirmed against source
- [ ] Any ambiguous values flagged with [CHECK] (none detected)

## Review Flags

# Review Report: Staphylococcus aureus Nitric Oxide Synthase (saNOS) Modulates Aerobic Respiratory Metabolism and Cell Physiology Protocol

---

## Critical Parameters Checklist (from the protocol)

- Temperature:
  - Bacterial growth: 37 °C
  - SEM fixation steps: room temperature and 4 °C
  - RNA extraction: not specified precisely, but standard kits used
  - Metabolite extraction and LC/MS: 4 °C or room temperature depending on step
- Growth times:
  - Overnight cultures: ~15 h
  - Aerobic cultures (assay time points): 3 h, 4 h, 6 h, up to 24 h (growth curves)
- Growth volumes and vessels:
  - 40 ml culture in 500 ml Erlenmeyer flasks (1:12.5 volume:flask ratio)
  - For some assays smaller aliquots (e.g., 1 ml, 2 ml) taken
- Shaking speed: 250 rpm
- Inoculum density: OD600 = 0.05
- Medium:
  - TSB + glucose (14 mM)
  - TSB – glucose
  - LB – glucose (mentioned but no data shown)
- NO donor (DPTA NONOate): final 100 µM from 150 mM stock in 0.01 M NaOH, stored −80°C ≤2 weeks
- Fluorescent dyes:
  - CM-H2DCFDA: 10 µM stain, incubation 60 min at 37 °C
  - MitoSOX Red: 5 µM stain, incubation 10 min at 37 °C
  - DiOC2(3): 30 µM stain for membrane potential
  - CTC: 4.5 mM stain, kinetics over 120 min at 37 °C
- Centrifugation:
  - 3901 × g for 3–10 min (culture harvest)
  - 13,000 × g (protein preparations)
- Catalase assay:
  - Protein diluted 1:1000
  - Incubation with Amplex Red for 1 hr at room temp (fluorescence readout)
- Flow cytometry events: 50,000 per sample
- Oxygen consumption:
  - Measured by Clark electrode, ~2 min linear rate, normalized to CFU/ml
- NADH dehydrogenase inhibitor (Thioridizine HCl): 15 µM, added at inoculation
- RNA sequencing:
  - RNA quality RIN = 9.9 minimum
  - rRNA depletion: RiboZero + MicrobExpress kits
  - Minimum gene expression RPKM ≥ 50
  - Fold change cutoff: ≥ 2
- Metabolomics:
  - Cell pellets: 40 ml culture lyophilized
  - Internal standards: heavy isotope-labeled compounds for organic acids, amino acids, NADH/NAD+, ATP/ADP etc.
  - Extraction solvents: 50:50 acetonitrile/0.3% formic acid for metabolites
  - UPLC column temp: 45 °C (organic acids), 55 °C (amino acids)
  - Quantitative LC/MS/MS with multiple reaction monitoring

---

## Potential Missing Parameters (compare to source)

- SEM fixation:
  - Although protocol states fixation in Trumps fixative for 15 min at RT, the source also indicates microwave-assisted processing (Pelco BioWave Pro); this is not detailed in the protocol (power settings, duration missing).
- RNA extraction:
  - Source mentions pooling RNA from 3 biological replicates prior to library construction; the protocol does mention pooling but without explicit timing or replicate handling details.
- Flow cytometry:
  - No mention of compensation or gating strategy details; source references prior publications but not fully detailed here.
- Oxygen consumption:
  - Protocol states normalization to CFU/ml but centrifugation resuspension volume handling not fully detailed for normalization steps.
- Metabolomics:
  - The extraction procedure mentions lyophilizing overnight but the protocol does not specify exact lyophilization time or vacuum pressure [CHECK].
  - Internal standard concentrations and detailed source of isotope-labeled standards are summarized but not fully enumerated.
  - Gradient details of LC/MS solvent system are truncated in source and summarized in protocol; full gradient specifics are missing [CHECK].
- Catalase activity:
  - Protocol mentions 1:1000 dilution of protein but source also highlights controls and hydrogen peroxide concentration specifics (not detailed here).
- NADH dehydrogenase inhibition:
  - Protocol uses 15 µM Thioridizine, source corresponds; however, duration of treatment only "added at inoculation" given — downstream timing for specific assays (ROS measurement timing) may benefit from clarification.
- Cell lengths measured from SEM:
  - Statistical analysis method is mentioned briefly (Holm-Sidak test) but exact sample size of cells quantified not fully listed (protocol says 12–14 fields; source states 12–14 fields; cell counts per field not specified).
  
---

## Possible Unsupported Claims

- None detected. All procedural steps and parameters appear directly supported or consistent with the source text and citations.

---

## Step Order / Omission Risks

- The protocol overall follows the source text's experimental flow well.
- Some minor risks:

  - The SEM protocol omits mention of microwave-assisted processing parameters which influence fixation quality.

  - RNA pooling prior to library prep is mentioned but potential batch effects related to pooling are not addressed.

  - Metabolomics extraction details such as exact lyophilization duration and LC gradient program details are missing, which could affect reproducibility [CHECK].

  - No explicit mention of negative controls or validation steps for flow cytometry dyes (e.g., no stain controls, dead cell exclusion), which usually are important given dye sensitivities [CHECK].

- The protocol appears to mix some measurement times (e.g., for ROS 3 h harvest, but growth curves collected up to 24 h). This is not a risk per se, but users must be aware to select correct time points relevant for their assay.

---

# Summary

The generated protocol comprehensively captures the critical numeric parameters and methodological steps from the source text with good fidelity. Minor parameters related to specialized equipment settings (microwave-assisted fixation), precise lyophilization settings, full LC gradient conditions, and flow cytometry gating are not fully specified and should be considered as potential gaps for strict reproducibility. No unsupported claims or major procedural omissions were detected. Protocol users should apply standard good practices for flow cytometry controls and metabolomics to mitigate these minor risks.
