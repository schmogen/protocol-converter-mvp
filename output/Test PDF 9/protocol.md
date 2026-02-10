# Contribution of the nos-pdt Operon to Virulence Phenotypes in Methicillin-Sensitive Staphylococcus aureus

## Objective
To investigate the genetic and functional roles of the nos and pdt genes in Staphylococcus aureus strain UAMS-1, including their contribution to oxidative stress resistance, phenylalanine biosynthesis, carotenoid pigmentation, intracellular nitric oxide (NO) levels, and virulence.

## Materials
- Staphylococcus aureus strains: UAMS-1, nos::erm mutant (KR1010), pdt deletion mutant (KR1013), complement strains
- Escherichia coli strain DH5α
- Plasmids: pTR27, pKR13, pMKnos, pMKpdt, pCRBlunt, pCR2.1, pBSK, pBT2, pMK4
- Media and buffers: Tryptic soy broth (TSB), tryptic soy agar (TSA), chemically-defined media (CDM) with and without phenylalanine, Luria-Bertani (LB) broth, HBSS buffer
- Antibiotics: Chloramphenicol (5 mg/ml or 10 mg/ml), erythromycin (2 mg/ml or 10 mg/ml), ampicillin (50 mg/ml), kanamycin (50 mg/ml)
- Chemicals and reagents: 
  - 4-Amino-5-Methylamino-2',7'-Difluorofluorescein (DAF-FM) diacetate
  - Diethylamine NONOate (DEA/NO)
  - 2-(4-carboxyphenyl)-4,5-dihydro-4,4,5,5-tetramethyl-1H-imidazolyl-1-oxy-3-oxide, monopotassium salt (cPTIO)
  - Methanol
  - Hydrogen peroxide (250 mM)
- Kits: iScript Reverse Transcriptase Kit; iQ SYBR Green Supermix; TURBO DNA-free Kit; Qiagen RNeasy minikit
- Equipment: Electroporator, microplate reader, centrifuge, incubators (37°C), qPCR thermocycler

## Procedure

### 1. Bacterial Growth Conditions
1.1 Grow planktonic S. aureus cultures either:
- Aerobically with 1:10 volume-to-flask ratio, shaking at 250 rpm; or
- Under low-oxygen conditions with 7:10 volume-to-flask ratio, static (0 rpm).

1.2 Streak S. aureus from frozen stock onto TSA plates for 24 hours at 37°C, followed by overnight aerobic growth in TSB.

1.3 Include antibiotics in media as needed:
- Chloramphenicol: 5 or 10 mg/ml
- Erythromycin: 2 or 10 mg/ml
- Ampicillin (for E. coli): 50 mg/ml
- Kanamycin (for E. coli): 50 mg/ml

### 2. Mutant and Complementation Strain Construction

#### 2.1 Creation of nos::erm Insertion Mutant (KR1010)
- Amplify the nos gene and clone into pCR2.1.
- Introduce internal BglII site by site-directed mutagenesis.
- Insert 1.1 kb BamHI fragment harboring erm resistance cassette into nos gene.
- Clone modified nos::erm allele into temperature-sensitive shuttle vector pBT2 to create pTR27.
- Transform pTR27 into S. aureus RN4220, followed by phage transduction into UAMS-1.
- Select for integration at 43°C on TSA + 10 mg/ml erythromycin.
- Induce plasmid loss by passaging at 30°C in TSB without antibiotic, then select for erythromycin resistance and chloramphenicol sensitivity.
- Confirm mutant by PCR and Southern blot.

#### 2.2 Creation of pdt Deletion Mutant (KR1013)
- PCR amplify ~1.2 kb upstream and ~1.0 kb downstream pdt regions.
- Clone separately into pCRBlunt, confirm inserts by sequencing.
- Ligate upstream and downstream flanking regions into temperature-sensitive vector pBT2 to create pKR13.
- Introduce pKR13 into S. aureus RN4220 and then transduce into UAMS-1.
- Select for double crossover deletion mutants by serial passage and antibiotic screening.
- Confirm deletion by PCR.

#### 2.3 Construction of Complementation Plasmids
- Amplify full nos gene with 564 bp upstream region and clone into pMK4 to create pMKnos.
- Amplify full pdt gene with 564 bp upstream region and clone into pMK4 to create pMKpdt.
- Transform plasmids into corresponding mutant strains.

### 3. RNA Isolation and Quantitative Real-Time PCR
- Isolate total RNA from cultures at specified growth phases using FASTPREP system and Qiagen RNeasy minikit.
- Treat RNA with TURBO DNA-free Kit to remove DNA contamination.
- Verify RNA integrity by mock qRT-PCR lacking reverse transcriptase.
- Synthesize cDNA using iScript Reverse Transcriptase Kit.
- Perform qRT-PCR using gene-specific primers for nos, pdt, crtN, asp23, purH, sigA (housekeeping gene).
- Use SYBR Green chemistry on EcoReal-Time PCR system.
- Normalize to sigA and calculate relative expression via 2^-ΔΔCt method.

### 4. Co-transcription PCR Assay
- Generate cDNA from RNA isolated from 6-hour low-oxygen cultures using gene-specific primer annealing to the 3’ end of pdt.
- Perform PCR with primers spanning nos start codon to pdt stop codon.
- Include no-RT controls to exclude genomic DNA contamination.
- Visualize PCR products by agarose gel electrophoresis.

### 5. Growth Experiments in Different Media
- Inoculate overnight cultures of strains in TSB or CDM, with or without phenylalanine.
- Set starting OD600 = 0.02 or 0.05 as indicated.
- Grow statically in 96-well polystyrene plates at 37°C.
- Measure OD600 every 2 hours up to 24 hours using microplate reader.

### 6. Hydrogen Peroxide Sensitivity Assay
- Grow strains aerobically to mid-exponential phase (OD600 ~0.3–0.5) in LB.
- Adjust cultures and expose to 250 mM H2O2 for 2 hours at 37°C.
- Determine surviving CFU by serial dilution and plating.

### 7. Carotenoid Pigment Assay
- Grow strains on TSA + 5 mg/ml chloramphenicol at 37°C for 48 hours.
- Scrape cells, wash twice in distilled water by centrifugation.
- Extract pigments by resuspending in 420 µl methanol and vortexing.
- Remove 20 µl for OD measurement, then incubate remaining 400 µl at 55°C for 5 min.
- Measure absorbance of supernatants at 465 nm.
- Normalize absorbance to relative OD600 of cell suspension.

### 8. Intracellular Nitric Oxide/Reactive Nitrogen Species Detection
- Harvest cells from static 7-hour biofilms or 26-hour TSA plates.
- Incubate cell suspensions in HBSS containing 5 mM DAF-FM diacetate at 37°C for 1 hour.
- Wash cells and resuspend in HBSS.
- Optional treatments during DAF-FM staining:
  - DEA (NO donor) 100 mM
  - DEA/NO 100 mM
  - cPTIO (NO scavenger) 150 mM
- Measure fluorescence (excitation 485 nm, emission 516 nm) in microplate reader.
- Normalize fluorescence to OD600.

### 9. Murine Model of Sepsis
- Thaw and prepare mid-log phase cultures of UAMS-1 wild-type and nos mutant strains at 1×10^9 CFU/ml in PBS.
- Inject female CD-1 Swiss mice (n=9 per group) intravenously via tail vein with 1×10^8 CFU (100 µl).
- Monitor mice for 7 days or until pre-moribund endpoints.
- Record and calculate mortality rates.
- Euthanize and harvest liver, kidneys, heart, and lungs.
- Homogenize organs and enumerate bacterial burden by CFU plating.

## Notes
- Antibiotic concentrations and growth conditions must be strictly followed.
- Confirm removal of DNA contamination during RNA extraction prior to qRT-PCR.
- Include proper controls for fluorescent NO detection assays to discriminate between NO and related reactive nitrogen species.
- Partial polar effects on downstream gene expression in mutants must be considered when interpreting phenotypes.
- For animal studies, ensure compliance with institutional animal care and use protocols.

## Review Checklist
- [ ] Growth conditions verified (temperature, CO2/O2, time)
- [ ] Media composition and volumes verified
- [ ] Mixing parameters verified (rpm/RCF, time)
- [ ] Incubation times verified
- [ ] Centrifugation settings verified (RCF, time, temp)
- [ ] Step order confirmed against source
- [ ] Any ambiguous values flagged with [CHECK]

## Review Flags

## Critical Parameters Checklist (from the protocol)

- Temperatures: 37°C incubation throughout; 43°C for plasmid integration; 30°C for plasmid loss; 55°C for pigment extraction step.
- Times:
  - TSA streak: 24 h + overnight
  - Growth monitoring: OD measurements every 2 h up to 24 h; 4.75–5 h for H2O2 assay; 48 h plates for pigment assay; 7 h biofilms for NO assay; 26 h TSA plates for NO assay; 7 day murine infection.
  - DAF-FM staining: 1 h at 37°C
  - H2O2 treatment: 2 h at 37°C
  - Methanol pigment extraction vortex 10 sec, incubate 5 min at 55°C.
- Volumes:
  - Shake flask ratios: aerobic 1:10 volume-to-flask; low-oxygen 7:10 volume-to-flask.
  - 1 ml culture sampling in various assays.
  - 200 µl aliquots for 96-well plate assays.
  - 420 µl methanol for pigment extraction.
- Concentrations:
  - Antibiotics: chloramphenicol 5 or 10 mg/ml; erythromycin 2 or 10 mg/ml; ampicillin and kanamycin 50 mg/ml each (for E. coli).
  - H2O2: 250 mM for oxidative stress assay.
  - DAF-FM diacetate: 5 mM.
  - DEA and DEA/NO: 100 mM.
  - cPTIO: 150 mM.
- Shaking speed: 250 rpm for aerobic growth.
- Static growth for low oxygen (0 rpm).
- OD600 starting points for growth curves: 0.02 or 0.05 as indicated.

## Potential Missing Parameters (compare to source)

- Initial OD600 for seeding cultures in growth/assays occasionally unspecified or variable between 0.02 and 0.05; clarification would be prudent.
- Exact centrifugation speeds/times for general harvesting steps frequently omitted or only general (e.g., 3 min at 13,000 rpm); RCF not specified—could vary by centrifuge model.
- Incubation temperature for plating serial dilutions sometimes unspecified.
- For mutant construction, some molecular cloning enzymatic reaction timings are not detailed but may be standard; e.g., time for ligations “several hours,” room temperature incubation.
- No experimental details on atmosphere (e.g., % O2, CO2) beyond static or shaking and flask ratios.
- Buffer compositions other than commercially named (e.g., HBSS) or chemical suppliers are missing full composition or catalog info.
- DAF-FM diacetate concentration used for plate assays (5 mM) is high relative to typical use (usually µM range); source indicates 5 mM but may warrant [CHECK].
- For NO detection, incubation details using DEA/NO and duration unspecified beyond 1-hour DAF-FM staining.
- Temperature and time for DNA digestion with Turbo DNase not fully described.
- No specification of animal housing conditions beyond standard laboratory.
- No mention of randomization or blinding in animal experiments.

## Possible Unsupported Claims

- The protocol states that saPDT "does not appear to function in an antioxidant capacity" based on H2O2 assay; however, the source indicates only “under the in vitro conditions tested,” hence the statement should be qualified to avoid overgeneralization.
- The claim that "endogenous NO levels on TSA plates appear upregulated" is based on DAF-FM assay showing ~35% decrease in nos mutant fluorescence; however, source states other cellular NO/RNS sources may contribute, so causality of saNOS solely responsible is not fully supported.
- The suggestion that carotenoid pigmentation increase in nos mutant is "solely due to loss of saNOS function" is not fully supported because pdt role is not ruled out conclusively in all contexts; polar effect could confound phenotype.
- The assumption that DAF-FM diacetate staining directly measures NO specifically, while source indicates reaction with RNS can occur, thus the protocol should qualify this as indirect detection.
- Statements about in vivo relevance of saNOS in MSSA virulence are based on murine sepsis model results but do not address partial polar effects on pdt expression in nos mutant; this caveat should be made explicit.
- The statement "Increased pigmentation is not due to altered expression of several pigment-related genes" is based on qPCR of only three genes and under specific growth conditions; full regulatory network changes are not excluded.

## Step Order / Omission Risks

- The protocol appears complete and generally consistent with source text step order.
- Potential omission: lack of explicit step describing verification of RNA integrity and absence of DNA contamination before qRT-PCR; only mock PCR mentioned.
- Complementation strain creation steps do not explicitly mention selecting for plasmid maintenance in complemented mutants during assays (e.g., antibiotic presence during phenotypic tests).
- In DAF-FM NO detection assays for plate-grown cells, no step describes adjusting for cell density differences explicitly before fluorescence normalization [CHECK].
- No mention of pre-staining washing steps to remove extracellular DAF-FM diacetate which may influence fluorescence background.
- Animal experiments lack detail about euthanasia method timing after pre-moribund state observed; humane endpoints criteria are summarized but specific handling steps may help reproducibility.
- No mention of negative controls or mock stains in fluorescence assays beyond stated reagents; could be emphasized for clarity.

---

Overall, the generated protocol reproduces the key experimental parameters and is consistent with the source text but some numeric details and caveats present in the source are not fully reflected. The claims should be qualified with regard to assay limitations and possible polar effects in mutants. Some minor procedural clarifications and explicit steps could reduce risk of variability.
