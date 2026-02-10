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