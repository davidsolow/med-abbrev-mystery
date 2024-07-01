# med-abbrev-mystery

In the healthcare industry, technical naming and acronyms are frequently used for brief and efficient documentation. Often these terms have similar or even identical spellings that can be misinterpreted. While the risks of misinterpretation vary by domain, they can be serious and even life threatening in the case of prescriptions and diagnoses7. Given this, improving the interpretability of patient notes, prescriptions, and other data on Electronic Medical Record (EMR) or other critical healthcare systems by disambiguating shared abbreviations can further improve patient outcomes.

In this project, we plan to build a Named Entity Recognition model that disambiguates medical acronyms to be used to pretrain additional models with the intention to apply these to downstream medical tasks such as patient note capture, prescription, and diagnosis.

To do this, we will use the MeDAL dataset to pre-train a model that can generalize medical terminology and acronyms. The MeDAL dataset includes content of over 14 million medical paper abstracts with locations of abbreviations and corresponding long-forms of the abbreviations. We will then fine-tune this model on real clinical text using the MIMIC-III dataset, which consists of clinical notes containing medication and diagnostic information. This fine-tuned model will discriminate acronyms in the context of clinical notes specifically.

Our experimentation will include all combinations of the following models (9 in total):
Pre-training Models:
BlueBERT
MS_BERT
BioBERT 
Fine Tuning Models:
LSTM w/o Self-attention
LSTM w/ Self-attention
ELECTRA small discriminator
Overview of Pretrain Steps: 

Pre Training task: BERT will predict the expansion of a given abbreviation
BERT as base model
Pool the final hidden states of the span of text corresponding to the abbreviation.
Add an output layer that predicts the correct expansion from the list of all possible ≠≠expansions.
Cross entropy loss with Adam 
Downstream Task i.e. predicting mortality:
Fine tune on MIMIC 3 dataset, load pretrained BERT model 
Final layer would be binary classification: mortality prediction outcome 0 alive and outcome 1 deceased
MIMIC dataset: collect discharge summaries and create a binary label for mortality if not already existent 
Fine tune BERT model on MIMIC III using binary cross-entropy loss

References:
Kevin Clark, Minh-Thang Luong, Quoc V. Le, and Christopher D. Manning. 2020. ELECTRA: Pretraining Text Encoders as Discriminators Rather Than Generators.
Irene Li, Michihiro Yasunaga, Muhammed Yavuz Nuzumlalı, Cesar Caraballo, Shiwani Mahajan, Harlan Krumholz, and Dragomir Radev. 2019. A Neural Topic-Attention Model for Medical Term Abbreviation Disambiguation.
Marta Skreta, Aryan Arbabi, Jixuan Wang, and Michael Brudno. 2019. Training without training data: Improving the generalizability of automated medical abbreviation disambiguation.
Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, and Illia Polosukhin. 2017. Attention Is All You Need.
Zhi Wen, Xing Han Lu, Siva Reddy. MeDAL: Medical Abbreviation Disambiguation Dataset for Natural Language Understanding Pretraining.
Elias Hossain, Rajib Rana, Niall Higgins, Jeffrey Soar, Prabal Datta Barua, Anthony R Pisani, Kathryn Turner. 2023. Natural Language Processing in Electronic Health Records in relation to healthcare decision-making: A systematic review.
Areej Jaber and Paloma Martínez. 2022. Disambiguating Clinical Abbreviations Using a One-Fits-All Classifier Based on Deep Learning Techniques.
