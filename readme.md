## CS 598 Final Project Spring 2023
In this repository you will find our implementation of the paper *Pre-training of Graph Augmented Transformers for Medication Recommendation* by  Shang et al.
### File Structure
```
.
├── ADMISSIONS.csv
├── Ablation\ Study\ Results.ods
├── Ablation\ Study\ Results.xlsx
├── AlternateGBERTWithOncology.ipynb
├── AlternateGBERTWithOutOncology.ipynb
├── Bert.ipynb
├── DIAGNOSES_ICD.csv
├── ExtractData.ipynb
├── FineTuning.ipynb
├── GAT.ipynb
├── OntologyEmbedding.ipynb
├── PATIENTS.csv
├── PRESCRIPTIONS.csv
├── PROCEDURES_ICD.csv
├── PreTraining.ipynb
├── READ_ME.md
├── data-multi-visit.pkl
├── data-single-visit.pkl
├── edge_index.py
├── gbert-with-ontology.bin //pretrained model with ontology embeddings
└── gbert-with-out-ontology.bin //pretrained model with out ontology embeddings 
```
### Requirements
```
pytorch>=0.4
python>=3.5
torch_geometric==1.0.3
```
### Run the Code
In order to run this code, clone the repository using
```
git clone https://github.com/ap46uiuc/CS598_Final_Project.git
```
cd into the cloned repo, unzip data.zip, and run the notebook using 
```
cd CS598_Final_Project
unzip data.zip
jupyter notebook
```
Finally, open the [AlternateGBERTWithOncology.ipynb](./AlternateGBERTWithOncology.ipynb) notebook and run the cells.

(You may have to run the imported juyter notebooks first if it's unable to import modules) 
### References:
The original paper: https://github.com/jshang123/G-Bert/tree/master  
```
@article{
    shang2019pre, 
    title={Pre-training of Graph Augmented Transformers for Medication Recommendation}, 
    author={Shang, Junyuan and Ma, Tengfei and Xiao, Cao and Sun, Jimeng}, 
    journal={arXiv preprint arXiv:1906.00346}, 
    year={2019} 
}
```
